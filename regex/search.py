import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR performing package upgrade"
#not so right way
index = log.index("[")
print(log[index+1:index+6])
#right way
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])