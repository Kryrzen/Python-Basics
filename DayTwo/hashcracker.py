import hashlib

#The "stolen" hash we want to crack
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99" # MD5 for password

#Open the wordlist file
try:
    with open("password.txt", "r") as file:
        for line in file:
            word = line.strip()

            # Hash the word
            hashed_word = hashlib.md5(word.encode()).hexdigest()

            # Compare
            if hashed_word == target_hash:
                print(f"Success! Password found: {word}")
                exit()

    print("Password not found in list.")
except FileNotFoundError:
    print("Error: password.txt not found.")

    """
    Key Concepts:
    Libraries: hashlib handles encryption/hashing.
    File I/O: open("file","r") opens a file for reading
    Cleaning Data: .strip() removes hidden characters like \n.
    Encoding: .encode() converts text to bytes so it can be hashed.
    """