# Authentication function
def authenticate(username, password):
    # Vulnerability: Hardcoded credentials make the system insecure
    # as anyone with access to the source code can retrieve the password.
    if username == "admin" and password == "P@ssw0rd123":  # Static password is insecure
        return True
    return False

# Example function call
print(authenticate("admin", "P@ssw0rd123"))

# Hashing function for passwords
import hashlib

def hash_password(password):
    # Vulnerability: Using the MD5 hashing algorithm, which is considered weak and deprecated.
    # MD5 is vulnerable to collision attacks and should not be used for password hashing.
    return hashlib.md5(password.encode()).hexdigest()

# Example function call
print(hash_password("my_secure_password"))

# Function to list files in a directory
import os

def list_files(directory):
    # Vulnerability: Unsafe use of user input in the os.system() command.
    # This opens the door to command injection attacks if the input is not properly sanitized.
    os.system(f"ls {directory}")

# Example function call
# The input "; rm -rf /" demonstrates how a malicious user can inject commands to delete files.
list_files("; rm -rf /")

# Function to load data from a file
import pickle

def load_data(file_path):
    # Vulnerability: Unsecured deserialization of pickle data.
    # If the file contains malicious payloads, it can execute arbitrary code on deserialization.
    with open(file_path, "rb") as file:
        return pickle.load(file)

# Example function call
# If the "data.pkl" file contains malicious code, it will execute upon loading.
load_data("data.pkl")
