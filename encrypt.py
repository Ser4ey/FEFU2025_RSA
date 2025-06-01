from rsa_algorithm import RSAAlgorithm
from TextCoder import TextCoder

def get_start_end():
    # Ввод нижней границы (start)
    while True:
        try:
            start = int(input("Введите нижнюю границу для p и q: "))
            break
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

    # Ввод верхней границы (end)
    while True:
        try:
            end = int(input("Введите верхнюю границу для p и q: "))
            if end > start:
                break
            else:
                print("Ошибка: Верхняя граница должна быть больше нижней. Попробуйте снова.")
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

    return start, end


def main():
    start = 2**7
    end = 2**10
    # start, end = get_start_end()

    print(f"[*] Данные для RSA генерируются...")
    p, q, n, e, d = RSAAlgorithm.generate_keys(start, end)
    print()


    text_coder = TextCoder(n)
    print()
    message = input("Введите сообщение:")

    # кодируем сообщение
    encoded_message = text_coder.text_to_numbers(message)
    print(f"\n[+] Кодирование и шифрование сообщения:")
    print(f"Закодированное сообщение: {encoded_message}")

    # шифруем сообщение
    encrypted_message = ",".join(str(RSAAlgorithm.encrypt(int(i), e, n)) for i in encoded_message.split(","))
    print(f"Зашифрованное сообщение: {encrypted_message}")


    print(f"\n[+] Дешифрование и декодирование сообщения:")
    # дешифруем сообщение
    decrypted_message = ",".join(str(RSAAlgorithm.decrypt(int(i), d, n)) for i in encrypted_message.split(","))
    print(f"Расшифрованное сообщение: {decrypted_message}")

    # Декодируем сообщение
    decoded_message = text_coder.numbers_to_text(decrypted_message)
    print(f"Декодированное сообщение: {decoded_message}")

    # Данные для отправки
    print(f"\n[+] Данные для отправки:")
    print(f"Сообщение: {encrypted_message}")
    print(f"Открытый ключ (e, n) = ({e}, {n})")


if __name__ == "__main__":
    main()
