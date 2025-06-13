import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
from generate_salt import load_salt

# Load salt from file (must match the one used in the encryption step)
SALT = load_salt()

def derive_key(secret_input: str, salt: bytes = SALT) -> bytes:
    """
    Derives a 32-byte key from the given secret input using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,  # Must match the iterations used during encryption
    )
    key = base64.urlsafe_b64encode(kdf.derive(secret_input.encode()))
    return key

def load_encrypted_backup_code(filename: str = "encrypted_backup_code.txt") -> bytes:
    """
    Loads the encrypted backup code from the specified file.
    """
    try:
        with open(filename, "rb") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Encrypted backup code file '{filename}' not found. Run generate.py first.")

def get_backup_code(input1: str, input2: str, input3: str) -> str:
    """
    Combines secret inputs, derives the key, and attempts to decrypt the backup code.
    """
    # Load the encrypted backup code from file
    encrypted_backup_code = load_encrypted_backup_code()
    
    # Combine inputs in the exact same order as used during encryption.
    combined_input = input1 + input2 + input3
    key = derive_key(combined_input)
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_backup_code)
        return decrypted.decode()
    except InvalidToken:
        return "Invalid inputs provided."

if __name__ == "__main__":
    # Prompt the user for the secret parts.
    user_input1 = input("Enter secret part 1: ")
    user_input2 = input("Enter secret part 2: ")
    user_input3 = input("Enter secret part 3: ")
    
    backup_code = get_backup_code(user_input1, user_input2, user_input3)
    print("Your backup code is:", backup_code)
