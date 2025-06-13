import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from generate_salt import load_salt

# Load salt from file
SALT = load_salt()

def derive_key(secret_input: str, salt: bytes = SALT) -> bytes:
    """
    Derives a 32-byte key from the given secret input using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,  # Adjust iterations as needed
    )
    key = base64.urlsafe_b64encode(kdf.derive(secret_input.encode()))
    return key

def encrypt_backup_code(combined_secret: str, backup_code: str) -> bytes:
    """
    Encrypts the backup code using a key derived from the combined secret inputs.
    """
    key = derive_key(combined_secret)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(backup_code.encode())
    return encrypted

if __name__ == "__main__":
    # Define your secret parts (make sure they exactly match what you'll later provide)
    secret_part1 = "secret1"
    secret_part2 = "secret2"
    secret_part3 = "secret3"
    
    # Combine the secrets in a predetermined order. Here we simply concatenate them.
    combined_secret = secret_part1 + secret_part2 + secret_part3
    
    # Define your predetermined backup code
    backup_code = "BACKUPCODE-123456"
      # Encrypt the backup code using the derived key
    encrypted_backup_code = encrypt_backup_code(combined_secret, backup_code)
    
    # Save the encrypted backup code to a file
    with open("encrypted_backup_code.txt", "wb") as f:
        f.write(encrypted_backup_code)
    
    print("Encrypted backup code saved to 'encrypted_backup_code.txt'")
    print("You can now use retrieve_backup_code.py to decrypt it with your secret inputs.")
