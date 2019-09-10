#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
#TODO: Separate lines and add stars
lines = text.split('\n')
print(lines)
for index, line in enumerate(lines):
    line = '* ' + line
    lines[index] = line
text = '\n'.join(lines)
pyperclip.copy(text)
