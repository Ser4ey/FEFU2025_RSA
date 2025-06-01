import random

def gcd(a, b):
    '''НОД a и b'''
    while b != 0:
        a, b = b, a % b
    return a

def is_prime_MR(n, k=50):
    '''Функция для проверки числа на простоту на основе теста Миллера-Рабина'''
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_primes(start_num=2*5, end_num=2**12):
    '''Функция для генерации 2 простых чисел p и q'''
    p = random.randint(start_num, end_num)
    while not is_prime_MR(p):
        p = random.randint(start_num, end_num)
    q = random.randint(start_num, end_num)
    while not is_prime_MR(q) or q == p:
        q = random.randint(start_num, end_num)
    return p, q


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

def simple_factorization(n):
    '''Разложение числа на множетели'''
    A = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            A.append(i)
            n = n // i
        else:
            i += 1
    if n != 0:
        A.append(n)

    return A

def pollards_rho(n):
    '''Алгоритм Полларда для факторизации чисел:
    https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    Работает для 2^40
    '''
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    while True:
        f = lambda x: (pow(x, 2, n) + c) % n
        c = random.randint(1, n - 1)
        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d


