#!/usr/bin/env python3
#
# main.py: Run some of our code
#
# Authors:      Amuzie, Brien, Kekicheff
# On behalf of: Vera Institute of Justice
#

from prosecutoruniverse import ProsecutorUniverse

import warnings

if __name__ == '__main__':
	print("Districts under consideration")
	print(ProsecutorUniverse.get_districts())	