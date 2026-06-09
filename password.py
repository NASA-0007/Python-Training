def password(passw):
    if (len(passw)<8):
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in passw):
        print("Password must contain at least one digit.")
        return False
    if not any(char.isupper() for char in passw):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in passw):
        print("Password must contain at least one lowercase letter.")
        return False 
    if " " in passw:
        print("Password must not contain spaces.")
        return False

    if not any(not char.isalnum() for char in passw):
        print("Password must contain at least one special character.")
        return False
    
    return True


while(True):
    passw = input("Enter a password: ")
    if password(passw):
        print("Password is valid.")
        break
    else:
        print("Password is not valid.")
