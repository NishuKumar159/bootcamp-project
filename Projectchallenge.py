# program in python to generate hashes of string data using 3 algorithm from hashlib
# we are gonna use 3 algorithm (i.e md-5, sha-256 and sha-1) from hashlib

import hashlib

# using md-5 hash algorithm
print('md-5:', hashlib.md5('Bootcamp project'.encode('UTF-8')).hexdigest())

# using sha-256 hash algorithm
print('sha-256:', hashlib.sha256('Bootcamp project'.encode('UTF-8')).hexdigest())

# using sha-1 hash algorithm
print('sha-1:', hashlib.sha1('Bootcamp project'.encode('UTF-8')).hexdigest())

 

