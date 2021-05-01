import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result_2 = re.search(regex, "A completely different string that also has numbers [34567]")
print(result_2[1])


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))

