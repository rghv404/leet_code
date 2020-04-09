'''
Given a valid (IPv4) IP address, return a defanged version of that IP address
A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''

# well looks simple enought, replace each occurence of '.' with '[.]'

import re
# works in O(2*m+n) time and constant space wher m is the size of the pattern beig replaced so essentailly O(n)

def defangIPaddr(address: str) -> str:
	if not str:
		return
	patt = re.compile('[.]') # re.compile('\.')
	return patt.sub('[.]', address)


add = "192.168.0.1"
res = defangIPaddr(add)
print(res)