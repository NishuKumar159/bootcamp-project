
#  program in python to generate MD5 of string data

text = 'Bootcamp project'

import hashlib
m = hashlib.md5()
m.update(text.encode('UTF-8'))
print(m.hexdigest())
