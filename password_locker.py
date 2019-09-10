#! python3
# password_locker.py - An insecure password locker program.

PASSWORDS = { 'email': 'fake_email@fake.com',
    'blog': 'this is a blog',
    'luggage': '12345'
}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account passwrod')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
