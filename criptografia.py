import rsa

def generate_keys():
    return rsa.newkeys(512)
    
def key_to_bytes(key: rsa.PrivateKey):
    my_key = key.save_pkcs1()
    return my_key.decode()