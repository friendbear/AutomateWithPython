import shutil, os

os.chdir('/tmp')
# shutil.copy('file1', 'file2')

# shutil.copytree('from_dir' 'to_dir')

# shutil.move('path-to-file', 'path')
# shutil.move('path-to-file', 'path-to-file2')

for filename in os.listdir():
    if filename.endswith('.tmp'):
        print(filename)
        # os.unlink(filename)
        # os.rmdir(path)
        # shutil.rmtree(path)


# See more send2trash module
