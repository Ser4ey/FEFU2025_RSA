from algorithms import pollards_rho, simple_factorization, euler, generate_d
from rsa_algorithm import RSAAlgorithm
from TextCoder import TextCoder


if __name__ == '__main__':
    print('''--- Атака на RSA через фаторизацию числа n ---''')
    print("")

    ciphertext = input("Введите зашифрованное сообщение:")
    e, n = map(int, input("Введите открытый ключ:").strip().strip("()").split(", "))

    print(f"\n[*] Факторизуем число n. Это может занять много времени")

    p = pollards_rho(n)
    # p = simple_factorization(n)[0] # медленная факторизация

    print(f"\n[+] Число n факторизовано!")
    print(f"p = {p}")
    q = n // p
    print(f"q = {q}")

    phi = euler(p, q)
    print(f"phi (функция Эйлера) = {phi}")

    # d ≡ e^(-1) (mod phi)
    d = generate_d(phi, e)
    print(f'd = {d}')

    print()


    encrypted_text = [str(RSAAlgorithm.decrypt(int(i), d, n)) for i in ciphertext.split(",")]
    encrypted_text = ','.join(encrypted_text)
    print(f"Дешифрованное сообщение: {encrypted_text}")

    text_coder = TextCoder(n)
    print(f"Текст: {text_coder.numbers_to_text(encrypted_text)}")


