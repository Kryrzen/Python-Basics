import hashlib

# Get User Input
text = input("Enter the word you want to hash: ")

# Generate MD5 Hash
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"MD5H Hash:{md5_hash}")

# Append to passwords.txt
with open("password.txt", "a") as file:
    file.write("\n" + text)

print(f"'{text}' has been added to password.txt")