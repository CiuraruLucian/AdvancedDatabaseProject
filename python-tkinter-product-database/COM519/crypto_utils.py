# Fernet is used for symmetric encryption and decryption
from cryptography.fernet import Fernet, InvalidToken

# Encryption key used for securing product names
KEY = b'Rk6M9ZmaWpo7DnFXkowIYPPucMW32CB0wIR_RxDuPlg='

# Create encryption cipher
cipher = Fernet(KEY)


# Encrypts plain text and returns encrypted bytes
def encrypt_text(text: str) -> bytes:
    return cipher.encrypt(text.encode())


# Decrypts encrypted text safely
def decrypt_text(token):
    try:
        return cipher.decrypt(token).decode()
    except (InvalidToken, TypeError):
        # Returns original value if decryption fails
        return token
