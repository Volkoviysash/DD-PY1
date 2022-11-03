from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


def get_random_password(n: int = 8) -> str:
    population = ascii_uppercase + ascii_lowercase + digits #создаcт один лист со всеми возможными символами
    return ''.join(sample(population, n))


print(get_random_password())
print(get_random_password(13))
print(get_random_password(1))
print(get_random_password(0))
