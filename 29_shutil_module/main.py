import random,shutil,string

## Random program
def generate_random_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Define the desired length of the password
password_length = 12

# Generate and print the random password
random_password = generate_random_password(password_length)
print(f"Generated random password: {random_password}")


