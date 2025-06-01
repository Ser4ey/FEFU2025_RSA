# Алгоритм взлома 1: Дешифрование без знания d
import random


def decrypt_message_ciphertext(ciphertext, e, n):
    '''
    Message = Ciphertext^e mod(n)
    '''

    for i in range(2, n+1):
        print(i)
        current_ciphertext = pow(i, e, n)
        if current_ciphertext == ciphertext:
            print(f"[+] Сообщение успешно расшифровано!")
            print(i)
            return i


    print(f"[-] Не удалось расшифровать сообщение")
    return 0

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



def attack_rsa_direct(n, e, c, max_tries=10 ** 6):
    '''Атака на RSA через перебор малых сообщений и итерационное возведение в степень e'''
    # 3. Итерационный метод из [[2]]: строим последовательность c, c^e, c^{e^2}, ...
    print("[*] Применение итерационного метода...")
    current = c
    seen = set()
    for _ in range(1, 100):  # Ограничение на количество итераций
        current = pow(current, e, n)
        if current in seen:
            print("[-] Цикл обнаружен, метод не сработал")
            break
        seen.add(current)
        # Проверяем, не совпадает ли текущее значение с оригинальным сообщением
        if is_prime(current) and pow(current, e, n) == c:
            return current
    return None


if __name__ == '__main__':
    ciphertext = 512523088269335703714427058587535087069488175905283942039280921253299660
    e = 425121442712543174057840697192649033551840712678836525682518938915644363
    n = 862192005054067058489963761493575491985197463733230507799422584404407841

    # Тест первого алгоритма
    decrypted1 = decrypt_message_ciphertext(ciphertext, e, n)
    print(f'Decrypted by first attack: {decrypted1}')

    # decrypted1 = attack_rsa_direct(ciphertext, e, n)
    # print(f'Decrypted by 2 attack: {decrypted1}')
