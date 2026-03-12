#!/usr/bin/env python
from time import sleep
"""
	Print function with flush parameter
	Created by: Ādams Vilnis

	URL:
	https://www.includehelp.com/python/flush-parameters-in-python-with-print-function.aspx
"""
# output is not flushed here
print("Es mācos programmēt!", end='')
sleep(0.1)
print("Lietoju funkciju print.", end='')
sleep(0.1)
print("Ar parametru flush.", end='')

sleep(5)
print("Bye!!!")
input("Press <ENTER> to exit.")
