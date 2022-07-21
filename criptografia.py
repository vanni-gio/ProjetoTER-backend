import rsa

def generate_keys():
    publicKey, privateKey = rsa.newkeys(512)
    public_byts = publicKey.save_pkcs1()
    private_byts = privateKey.save_pkcs1()
    return public_byts.decode(), private_byts.decode()