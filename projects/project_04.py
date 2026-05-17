# Caesar Cipher

def get_convert_type():
    is_invalid_type = True
    cipher_type = ""
    while is_invalid_type:
        cipher_type = input("Type 'e' to encrypt and 'd' to decrypt message : ").lower()
        is_invalid_type = cipher_type not in ["e", "d"]
        if is_invalid_type:
            print("Enter valid ciphering type!")
    return cipher_type


def get_message():
    is_invalid_type = True
    message = ""
    while is_invalid_type:
        message = input("Enter your message : ").lower()
        is_invalid_type = not message.isalpha()
        if is_invalid_type:
            print("Enter valid message letters (a-z)")
    return message


def get_shift_key():
    is_invalid_key = True
    shift_key = ""
    while is_invalid_key:
        shift_key = input("Enter key shift number : ")
        is_invalid_key = not shift_key.isnumeric()
        if is_invalid_key:
            print("Enter valid shift key")
    return int(shift_key)


def cipher(message, shift_key, cipher_type, alphabet_size=26):
    letters = []
    shift_key *= -1 if cipher_type == "d" else 1
    for letter in message:
        ascii_offset = ord("a")
        shifted = (ord(letter) - ascii_offset + shift_key) % alphabet_size
        letters.append(chr(shifted + ascii_offset))
    return "".join(letters)


def provide_space(lines_no=1):
    print("\n" * lines_no)


user_choice = True

try:
    while user_choice:
        convert_type = get_convert_type()
        provide_space()

        message = get_message()
        provide_space()

        shift_key = get_shift_key()
        provide_space()

        result = cipher(message, shift_key, convert_type)
        result_type = "Encryption" if convert_type == "e" else "Decryption"
        print(f"{result_type} Result: {result}")
        provide_space()

        user_choice = (
            True if input("Continue ciphering : (y/n) : ").lower() == "y" else False
        )
        provide_space(3 if user_choice else 0)

except KeyboardInterrupt:
    print("\nCiphering interrupted!")
