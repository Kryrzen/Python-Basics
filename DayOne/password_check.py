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

"""
Key Concepts
- Variables: Storing the password and its length.
- Input/Output: input() to get data and print() to show result
- Conditions: if, elif, and else to make decisions based on data.
- Built-in FUnctions: Using len() to count characters.
"""