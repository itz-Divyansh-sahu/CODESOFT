import string
import secrets

def GeneratePassword(len):
    # Character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    # Secure Password Generation
    password = ''.join(secrets.choice(characters) for _ in range(len))
    print("Generated Password: "+password)
