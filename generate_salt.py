import os
import secrets

def generate_salt_file(filename: str = "salt.txt") -> None:
    """
    Generates a cryptographically secure 32-byte salt and saves it to a file.
    """
    # Generate a secure random 32-byte salt
    salt = secrets.token_bytes(32)
    
    # Save to file
    with open(filename, "wb") as f:
        f.write(salt)
    
    print(f"Salt generated and saved to '{filename}'")
    print(f"Salt length: {len(salt)} bytes")

def load_salt(filename: str = "salt.txt") -> bytes:
    """
    Loads the salt from the specified file.
    """
    try:
        with open(filename, "rb") as f:
            salt = f.read()
        return salt
    except FileNotFoundError:
        raise FileNotFoundError(f"Salt file '{filename}' not found. Run generate_salt_file() first.")

if __name__ == "__main__":
    # Generate the salt file
    generate_salt_file()
    
    # Verify it can be loaded
    salt = load_salt()
    print(f"Verification: Loaded salt with {len(salt)} bytes")
