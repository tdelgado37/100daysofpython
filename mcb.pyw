#! python
# mcb.pyw - saves and loads pieces of text to the clipboard.
#Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> 0 loads keyword to clipboard
#       py.exe mcb.pyw list - loads all keywords to clipboard
#       py.exe mcb.pyw delete - deletes all keywords from clipboard
#       py.exe mcb.pyw delete <keyword> - deletes keyword from clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in mcbShelf.keys():
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
