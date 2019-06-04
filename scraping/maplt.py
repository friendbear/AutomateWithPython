#! python3

# open webbrowser
# ex)
# $0 870 Valencia St, San Francisco, CA 94110
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

