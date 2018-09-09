#!/usr/bin/env python3
#
# universe.py: Methods which describe the universe (e.g. municipal, state and federal districts) for prosecutors"""
#
# Authors:      Amuzie, Brien, Kekicheff
# On behalf of: Vera Institute of Justice
#

import warnings

class ProsecutorUniverse:
	def get_districts():
		districts = {
						"ny": "New York State",
						"ma": "Massachusetts"
					}
		return districts

	def __init__(self):
		print(ProsecutorUniverse.get_districts())		

