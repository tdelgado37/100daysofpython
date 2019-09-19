#! python
#strongPassword.py - tells if the inputed string is a strong strongPassword

import re

password = input('Enter a strong password: ')

strongPasswordRegex = re.compile(r'[A-Za-z0-9{1,}]{8,}')
results = strongPasswordRegex.search(password)

if results is None:
    print('Not a strong password, password needs some gains!')
else:
    print('That password Arnold strong!')
