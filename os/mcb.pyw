#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword>
# py.exe mcb.pyw <keyword>
# py.exe mcb.pyw list

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv == 2):
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
