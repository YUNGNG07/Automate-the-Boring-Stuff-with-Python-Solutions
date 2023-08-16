import re

phone_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone_num.search('My number is 415-555-4242')
print(f'Phone number found: {match.group()}')
