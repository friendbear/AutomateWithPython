
import os

# os.sep
print(os.sep)

# join
os.path.join('usr', 'bin', 'spam')

# join example
for filename in ['accounts.txt', 'details.csv', 'invite.docx']:
    print(os.path.join('~/Documents', filename))

# pwd chdir
print(os.getcwd())
os.chdir(os.path.join('/', 'tmp'))
print(os.getcwd())

# makedirs, exists, isdir, isfile
pid = os.getpid()
make_dir = os.path.join('/', 'tmp', 'python', str(pid))
os.makedirs(make_dir)
if os.path.exists(make_dir) and os.path.isdir(make_dir) and not os.path.isfile(make_dir):
    print('path created: ' + make_dir)

# abspath(path)
print(os.path.abspath('.'))

# os.path.basename, dirname, split

# os.path.getsize
