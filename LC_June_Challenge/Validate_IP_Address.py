'''
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:

Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

'''
import string
def checkIPV4(s:str)->bool:
	def otherChecks(numString:str)->bool:
		if '-' in numString: return False
		try: actualNum = int(numString)
		except:return False
		# cvhekc if actual decimel less than 256 and no leading zeroes except for single 0
		if (actualNum>=0 and actualNum<=255) and (numString[0]!= '0' or len(numString)==1): return True
		return False

	sList = s.split(".")
	print(sList)
	if not len(sList) == 4: return False
	return all(otherChecks(num) for num in sList)

def checkIPV6(s:str)->bool:
	def otherChecks(numString:str)->bool:
		if not numString or len(numString) > 4: return False
		hexSet = set(string.hexdigits)
		return all(c in hexSet for c in numString)
	# just going to split and chekc if the splits tringa re hex or not 
	sList = s.split(":")
	print(sList)
	if not len(sList) == 8: return False
	return all(otherChecks(num) for num in sList)

def validIPAddress(IP: str) -> str:
	if '.' in IP:
		if checkIPV4(IP):
			return "IPV4"
	elif ':' in IP:
		if checkIPV6(IP):
			return "IPV6"
	return "Neither"


ip = "172.16.254.01"
ip = "172.16.254.1"
ip6 = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
ip6 = "2001:0db8:85a3:0:00:8A2E:0370:7334"
ip = "0.0.0.-0"
res = validIPAddress(ip)
print(res)