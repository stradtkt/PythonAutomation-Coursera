import re

result = re.search(r"aza", "plaza")
print(result)
result_2 = re.search(r"aza", "bazaar")
print(result_2)
result_3 = re.search(r"aza", "maze")
print(result_3)
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))