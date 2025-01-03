import random
import string
import secrets
import hashlib


def generate_access_token_2(lng=10):
    """
    crypto token creation by using secrets.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    token = ''.join(secrets.choice(characters) for _ in range(lng))
    return token



def generate_access_token_3(lng=32, salt_lng=10):
    """
    crypto token creation by using secrets + salt 
    using secrets and hashlib vs cryptoprediction attack.
    """

    # salt generated
    salt = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(salt_lng))
    # token generated
    raw_token = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(lng))

    # salt + token
    combined = (salt + raw_token).encode('utf-8')
    hashed_token = hashlib.sha256(combined).hexdigest()
    return hashed_token, salt


# Print
print("Token 2 (secure):", generate_access_token_2())
print("Token 3 (hashed_token, salt):", generate_access_token_2())
