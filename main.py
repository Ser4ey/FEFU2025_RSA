import random

from algorithms import gcd, generate_primes


def euler(p, q):
    '''Значение функции Эйлера от произведения p и q.
    Функция Эйлера определяется как количество целых чисел от 1 до n, которые
    взаимно просты с n'''
    return (p - 1) * (q - 1)

def generate_e(phi):
    '''Поиск открытой экспоненты e. Это число должно быть взаимно простым с
    значением функции Эйлера.'''
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e

def generate_d(phi, e):
    '''Поиск закрытой экспоненты d. Она является обратной к открытой экспоненте
    по модулю значения функции Эйлера.
    ed ≡ 1 (mod phi)
    d ≡ e^(-1) (mod phi)
    '''
    d = pow(e, -1, phi)
    return d


if __name__ == '__main__':
    p, q = generate_primes()
    print(f"p = {p}, q = {q}")
    n = p * q
    phi = euler(p, q)
    e = generate_e(phi)
    d = generate_d(phi, e)
    print(f'Open key: ({e}, {n})')
    print(f'Close key: ({d}, {n})')

    print(f"Введите сообщение (максимальный размер: {n}):")

    message = int(input('message:'))
    dec = pow(message, e, n)
    enc = pow(dec, d, n)
    print(f'dec: {dec}')
    print(f'enc: {enc}')





