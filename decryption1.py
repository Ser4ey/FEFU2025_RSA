from rsa_algorithm import RSAAlgorithm
from TextCoder import TextCoder

def decrypt_message_ciphertext(ciphertext, e, n, text="Блок: 1. Текущий текст: '123' Попытка: "):
    '''
    Message = Ciphertext^e mod(n)
    '''
    for i in range(2, n+1):
        if RSAAlgorithm.decrypt(i, e, n) == ciphertext:
            print(f"Пробуем число {i} в качестве сообщения - успех!")
            print(f"[+] Сообщение успешно расшифровано!")
            return i
        print(f"Пробуем число {i} в качестве сообщения - неудача")

    print(f"[-] Не удалось расшифровать сообщение")
    return 0


if __name__ == '__main__':
    print('''Атака на RSA через перебор малых сообщений и итерационное возведение в степень e''')

    ciphertext = input("Введите зашифрованное сообщение:")
    e, n = map(int, input("Введите открытый ключ сообщение:").strip("()").split(", "))

    text_coder = TextCoder(n)

    current_text = ""
    blocks = list(map(int, ciphertext.split(",")))
    current_block = 1
    number_of_block = len(blocks)

    for block in blocks:
        t = f"Блок: {current_block}/{number_of_block}. Текущий текст: '{current_text}' Попытка: "
        decrypted_message = decrypt_message_ciphertext(block, e, n, text=t)
        current_text += text_coder.number_to_text(decrypted_message)
        current_block += 1

    print("\n\n[+] Текст полность дештфрован")
    print(f"Текст: {current_text}")

