password = input()

if len(password) < 6:
    print("Too Short")
elif len(password) > 12:
    print("Too Long")
elif not any(char.isdigit() for char in password):
    print("Password must contain a digit")
else:
    print("Password Accepted!")
