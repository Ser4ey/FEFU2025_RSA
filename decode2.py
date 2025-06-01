import random
import math


def gcd(a, b):
    '''НОД a и b'''
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n, k=50):
    '''Проверка числа на простоту (тест Миллера-Рабина)'''
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


def pollards_rho(n):
    '''Алгоритм Полларда для факторизации чисел:
    https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm'''
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


def factorize(n):
    '''Полная факторизация n на простые множители'''
    if is_prime(n):
        return [n]
    p = pollards_rho(n)
    q = n // p
    return [p, q]


def euler(p, q):
    '''Функция Эйлера φ(n) = (p-1)(q-1)'''
    return (p - 1) * (q - 1)


def generate_d(phi, e):
    '''Вычисление закрытого ключа d как обратного к e по модулю φ(n)'''
    return pow(e, -1, phi)


def attack_rsa(n, e, c):
    '''Атака на RSA: извлечение сообщения M из C, e, n'''
    # Шаг 1: Факторизация n
    p, q = factorize(n)
    print(f"[Атака] Найдены множители p={p}, q={q}")

    # Шаг 2: Вычисление φ(n)
    phi = euler(p, q)

    # Шаг 3: Вычисление d
    d = generate_d(phi, e)

    # Шаг 4: Дешифрование
    m = pow(c, d, n)
    return m


if __name__ == '__main__':
    n = 105029
    e = 5
    c = 54425
    # Атака
    print("\n=== Атака на RSA ===")
    recovered_message = attack_rsa(n, e, c)
    print(f"Восстановленное сообщение: {recovered_message}")