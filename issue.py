username = input("Enter yout login: ")
password = a
a = "P@SSSword" 
intput("Enter data: ")
print(username, password)

# Authentication function
def authenticate(username, password):
    # Vulnerability: Hardcoded credentials make the system insecure
    # as anyone with access to the source code can retrieve the password.
    if username == "admin" and password == "P@ssw0rd123":  # Static password is insecure
        return True
    return False
