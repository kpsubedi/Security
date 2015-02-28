import re
input_str = 'aA9'
valid = re.compile(r"^[a-zA-Z0-9]+$")
print valid.match(input_str).group()
print valid.match(input_str).groups()


