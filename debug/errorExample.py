import traceback

def spam():
    bacon()

def bacon():
    raise Exception('bacon exception')

try:
    spam()
except:
    error_file = open('/tmp/errorInfo.log', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()

