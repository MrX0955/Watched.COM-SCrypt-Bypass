import pyscrypt

salt = b'C1k8l0jw8g8puGRauyKjcN0ofNp' #DON'T CHANGE THIS
passwd = b'PASSWORD HERE' # ENTER UR OWN PASSWORD
key = pyscrypt.hash(passwd, salt, 1024, 1, 1, 15) # DON'T CHANGE THIS
SifreliKey = key.hex()
print(SifreliKey)
