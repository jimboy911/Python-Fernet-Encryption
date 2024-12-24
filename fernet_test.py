#fernet_test.py

from cryptography.fernet import Fernet

key = Fernet.generate_key() #this generates a long string of characters

#assign key to variable? this creates a Fernet object. i'm not exactly sure what it's used for
f = Fernet(key)

#convert plaintext to ciphertext
token = f.encrypt(b"myPassword123")

#what happens if you try to encrypt it using just the key? it doesn't work since the string isn't in bytes yet
#token_key = key.encrypt(b"myPassword123")

#what if we convert they key to bytes and then try again, it doesn't work either
#key_bytes = b"myPassword123"
#token_key = key_bytes.encrypt(b"myPassword123")

print(token)

#now decrypt the token
d = f.decrypt(token)
print(d) #it prints out the password but in bytes form
