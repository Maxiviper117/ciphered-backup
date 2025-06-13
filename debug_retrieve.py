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

def debug_get_backup_code(input1: str, input2: str, input3: str) -> str:
    """
    Combines secret inputs, derives the key, and attempts to decrypt the backup code with debug info.
    """
    # Load the encrypted backup code from file
    encrypted_backup_code = load_encrypted_backup_code()
    
    # Combine inputs in the exact same order as used during encryption.
    combined_input = input1 + input2 + input3
    
    print(f"Debug: Combined input: '{combined_input}'")
    print(f"Debug: Combined input length: {len(combined_input)}")
    print(f"Debug: Salt length: {len(SALT)} bytes")
    print(f"Debug: Encrypted data length: {len(encrypted_backup_code)} bytes")
    
    key = derive_key(combined_input)
    print(f"Debug: Derived key: {key}")
    
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_backup_code)
        return decrypted.decode()
    except InvalidToken as e:
        print(f"Debug: InvalidToken error: {e}")
        return "Invalid inputs provided."

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        # Test with the exact same inputs as used in generate.py
        print("Testing with hardcoded inputs from generate.py:")
        result = debug_get_backup_code("secret1", "secret2", "secret3")
        print("Result:", result)
    elif len(sys.argv) == 4:
        # Use command line arguments
        secret1 = sys.argv[1]
        secret2 = sys.argv[2]
        secret3 = sys.argv[3]
        
        print(f"Using command line arguments:")
        print(f"Secret 1: '{secret1}'")
        print(f"Secret 2: '{secret2}'")
        print(f"Secret 3: '{secret3}'")
        
        backup_code = debug_get_backup_code(secret1, secret2, secret3)
        print("Your backup code is:", backup_code)
    else:
        print("Usage:")
        print("  python debug_retrieve.py                    # Test with hardcoded secrets")
        print("  python debug_retrieve.py <s1> <s2> <s3>     # Test with provided secrets")
        print("Example: python debug_retrieve.py secret1 secret2 secret3")
        sys.exit(1)
