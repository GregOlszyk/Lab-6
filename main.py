# Made by Greg Olszyk

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

if __name__ == '__main__':
    program_continue = True
    option = 0
    password = ""
    encoded_password = ""
    while program_continue:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            # print(encoded_password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            pass
        if option == 3:
            game_continue = False