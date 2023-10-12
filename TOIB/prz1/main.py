import string
import itertools

password = "qwer"

alphabet = string.digits + string.ascii_letters + string.punctuation

curr_pass_len = 1

def string_iter(string, length):
    yield from itertools.product(string, repeat=length)

while True:
    for password_add in string_iter(alphabet, curr_pass_len):
        password_string = ''.join(password_add)
        if password_string == password:
            print("Пароль: {}".format(password_string))
            exit()
    curr_pass_len += 1