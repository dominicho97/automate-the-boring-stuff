import re




phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#look for digit/digit/digit-....
searchMatch = phoneNumRegex.search('Call me on 333-456-8228 tommorow, or at 415-555-1128') 
print(searchMatch.group())
