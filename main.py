import string
import itertools

password = "qwerty123"

alphabet = string.digits + string.ascii_letters + string.punctuation

curr_pass_len = 1

def string_iter(string, length):
    yield from itertools.product(string, repeat=length)

while true
    for password in string_iter(guess_password_set, guess_password_length):
    password_string = ''.join(password)
        if password_string == password:
            print("Пароль: {}".format(password_string))
            exit()
    curr_pass_len += 1