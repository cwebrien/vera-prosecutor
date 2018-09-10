#!/usr/bin/env python3
#
# prosecutorfetcher.py: Pulls the prosecutors for different districts
#
# Authors:      Amuzie, Brien, Kekicheff
# On behalf of: Vera Institute of Justice
#

import re
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
	"""
	Attempts to get the content at `url` by making an HTTP GET request.
	If the content-type of response is some kind of HTML/XML, return the
	text content, otherwise return None.
	"""
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None


def is_good_response(resp):
	"""
	Returns True if the response seems to be HTML, False otherwise.
	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 
			and content_type is not None 
			and content_type.find('html') > -1)


def log_error(e):
	"""
	It is always a good idea to log errors. 
	This function just prints them, but you can
	make it do anything.
	"""
	print(e)


class ProsecutorFetcher:
	def __init__(self,
				 state):
		"""
		A ProsecutorFetcher will pull all of the prosecutors for a particular state.
		It auto-initializes the districts within a state. Returns new ProsecutorFetcher.
		"""
		self.state          = state
		self.district_pages = self.__get_district_pages()
		
		
	def __get_district_pages(self):
		"""
		Given the state specified, pull the districts and their respective webpages.
		Returns a dictionary of district to webpage.
		"""
		return self.__get_ma_district_pages()
	
	
	def __get_ma_district_pages(cls):
		"""
		District fetcher -- Massachusetts
		Returns a dictionary of district to webpage.
		"""
		district_pages = {}
		
		raw_html = simple_get("http://www.mass.gov/mdaa/district-attorneys/by-city-or-town.html")
		bs_html  = BeautifulSoup(raw_html, "html.parser")
		links = bs_html.findAll("a", class_="titlelink")
		
		# Example link: http://www.mass.gov/mdaa/district-attorneys/offices/norfolk-da.html
		for link in links:
			uri = "http://www.mass.gov" + link["href"]
			if("district-attorneys/offices" in uri):
				# The district name is embedded in the URI, so get it and clean it up 
				district_name = uri.split("/")[-1]
				district_name = district_name.replace("-da.html", "")
				district_name = district_name.replace(".html", "")
				district_name = district_name.replace("-", " ")
				district_name = district_name.title()
				
				# Store district to district page
				district_pages[district_name] = uri
		
		return district_pages
		
		
if __name__ == '__main__':
	raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
	bs_html = BeautifulSoup(raw_html, 'html.parser')
	
	#for i, li in enumerate(bs_html.select('li')):
	#	print(i, li.text)
	
	pf = ProsecutorFetcher("MA")
	print(pf.district_pages)	

		
