import hashlib
import getpass

# Store this hash somewhere secure in real use
# This is the hash of the original password (e.g., 'mypassword123')
stored_password_hash = '482c811da5d5b4bc6d497ffa98491e38'  # MD5 hash of 'password123'

# Ask user to enter password (input hidden)
entered_password = getpass.getpass("Enter your password: ")

# Hash the entered password using MD5
hashed_input = hashlib.md5(entered_password.encode()).hexdigest()

# Compare the hashes
if hashed_input == stored_password_hash:
    print("✅ Password is correct!")
else:
    print("❌ Incorrect password.")

