# Get User Input
password = input("ENter a password to test:")

# Measure the length
length = len(password)

# Logical Check (Minimum 8 Characters for basic security)
if length >= 12:
    print("Strength: Strong")

elif length >= 8:
    print("Strength: Medium")

else:
    print("Strength: Weak (Too short!)")


print (f"Your password is {length} chaacters long")