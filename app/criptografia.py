import rsa
from cryptography.fernet import Fernet

key = Fernet.generate_key()

publicKey, privateKey = rsa.newkeys(512)
rsa.sign()
public_byts = publicKey.save_pkcs1()
private_byts = privateKey.save_pkcs1()