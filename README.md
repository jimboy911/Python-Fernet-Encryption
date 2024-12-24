# Python-Fernet-Encryption
Python Fernet Encryption (Symmetric)

Symmetric encryption isn't the best way to store passwords but it can be used to make environment variables more secure.  i might be better off writing my code to prompt the user for their username and password for future automation work since i figured out a way to just use netmiko.  but lets try just for the fun of it.

////////

step 1 - generate_key() this generates a new fernet key which must be kept safe as it is used to decrypt the password.  if the key is lost then the password can no longer be decrypted. also if they key is lost, a hacker could use it to gain access to a secure system or impersonate other users

step 2 - encrypt(data) converts the plain text into ciphertext.  the data must be in bytes

step 3 - decrypt(token,ttl=none) - uses the key to convert the ciphertext into plain text

////////

python3 -m venv fernet_env

source fernet_env/bin/activate

pip install cryptography
