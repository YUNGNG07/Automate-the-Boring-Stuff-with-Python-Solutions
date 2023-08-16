import re

length = re.compile('.{8,}')
lower_case = re.compile('[a-z]+')
upper_case = re.compile('[A-Z]+')
digit = re.compile('[\d]+')

regex_list = [length, lower_case, upper_case, digit]

def validate_pass(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Sorry, your password is not strong enough.')
            break
        else:
            regex_count += 1
            continue
    if regex_count is 4:
        print('Congratulations! Your password is strong enough.')

if __name__ == '__main__':
    password = input()
    validate_pass(password)
