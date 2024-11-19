from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt_data(self, data):
        return self.cipher.encrypt(data)

    def decrypt_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data)
