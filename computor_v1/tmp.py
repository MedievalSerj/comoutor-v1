import re


res = re.search('(([0-9.]*)[ ]*\*?)?[ ]*X(\^([012]))?', '5X^0')
factor = res.group(2)
power = res.group(4)

print(f'factor: {factor}')
print(f'power: {power}')
