#!/usr/bin/env python3
#
# prosecutor.py: Class definitions for a prosecuting attorney
#
# Authors:      Amuzie, Brien, Kekicheff
# On behalf of: Vera Institute of Justice
#

import warnings

class Prosecutor:
	def __init__(self,
				 state,
				 district,
			     first_name,
			     last_name):
		
		# Basics
		self.state        = state
		self.district     = district
		self.first_name   = first_name
		self.last_name    = last_name
		
		# Optional contact info
		self.email        = ""
		self.phone_number = ""
		self.website       = ""
		
		# Optional political info
		self.election_year = float("nan")
		self.party         = ""
		self.terms_served  = float("nan")
		
	def __str__(self):
		return (self.state + " - " + self.district + ": " +
				self.last_name + ", " + self.first_name)
		
if __name__ == '__main__':
	print("Basic runner for prosecutor.py")
	
	p = Prosecutor("NY", "New York County", "Cyrus", "Vance")
	print(p)
		