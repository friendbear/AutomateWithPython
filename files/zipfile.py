import zipfile, os

example_zip = zipfile.ZipFile('example.zip')
example_zip.namelist()
spam_info = example_zip.getinfo('spam.txt')

spam_info.file_size()
spam_info.compress_size()
example_zip.close()

