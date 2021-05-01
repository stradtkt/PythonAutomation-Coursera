import re

print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-z]", "This is a sentence with spaces."))
print(re.findall(r"cat|dog", "I like both cats and dogs"))