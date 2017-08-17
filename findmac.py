import re
from  pprint import pprint
with open('output.txt') as f:
    data = f.read()

pattern = re.compile('NWSTCAPC07#scm (\w\w\w\w\.\w\w\w\w\.\w\w\w\w)  ser ds  \| inc FALSE\nValid        : FALSE')

test = pattern.findall(data)


print(len(test))
pprint(test)


