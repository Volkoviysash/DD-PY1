from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


def get_random_password(length=8, uppercase=True, digits=True):
    alphabet = string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    return ''.join(sample(alphabet, length))


print(get_random_password())
print(get_random_password(13))
print(get_random_password(1))
print(get_random_password(0))
