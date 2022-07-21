import random
import string
import bcrypt
# from OpenSSL import SSL

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')  

def encryot(mystr):
    hashed = bcrypt.hashpw(mystr, bcrypt.gensalt(NUM_ROUNDS, bytes(SECRET_KEY)))
    return hashed

def decrypt(hashed):
    pass

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key=''.join(random.choice(random_str) for i in range(12))
NUM_ROUNDS=12
SECRET_KEY=key
DEBUG=True
# config banco de dados