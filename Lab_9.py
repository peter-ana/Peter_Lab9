def main():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
    choice = input("Please enter an option: ")
    if choice == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = ""
        for digit in password:
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_password += encoded_digit
        print("Your password has been encoded and stored!")
    if choice == 2:
        print(f"The encoded password is {encoded_password}, and the original password is {password}.")
    if choice == 3: