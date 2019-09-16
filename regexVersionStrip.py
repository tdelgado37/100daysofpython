#! python3
#regexVersionStrip.py - program to recreate strip function

import re

def regexStrip(string, charactersToStrip = ' '):
    if charactersToStrip == ' ':
        regex = re.compile(r'\s')
    else:
        regex = re.compile(charactersToStrip)
    return regex.sub('',string)

string = regexStrip('this is a test','t')
print(string)
