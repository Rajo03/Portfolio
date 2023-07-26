import re
 
pattern = re.compile(".*Delhi.*", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

import re
 
pattern = re.compile(".*Delhi.*[^ ]+@[^ ]+\.[a-z]+", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)


import re
 
pattern = re.compile(".*Delhi.*[0|+][0-9]{4,50}", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)


import re
 
pattern = re.compile(".*Delhi.*([0|+][0-9]{4,50}|[^ ]+@[^ ]+.[a-z]+)", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)