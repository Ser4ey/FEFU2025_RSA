import math

from tabulate import tabulate

class TextCoder:
    alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',
             'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
             'Ю', 'Я', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '!', '?', ';', ':', '(', ')',
             '"', "'", ""]

    alpha_set = set(alpha)

    code_dict = dict(zip([bin(i)[2:].rjust(7, "0") for i in range(128)], alpha))
    alpha_dict = dict(zip(alpha, [bin(i)[2:].rjust(7, "0") for i in range(128)]))

    def __init__(self, block_size=128):
        self.block_size = block_size
        self.number_of_char_in_block = int(math.log(block_size, 128))
        if self.number_of_char_in_block == 0:
            raise Exception('Размер блока n слишком маленький. Минимальный размер 128')

        print(f"[+] Кодеровщик иницилизирован. Размер блока: {block_size}. "
              f"Блок содержит символов: {self.number_of_char_in_block} ")

    def text_to_numbers(self, text):
        n = []
        for char in text:
            if not (char in self.alpha_set):
                print(f"Символа '{char}' нет в алфавите. Он будет заменён на '?'")
            n.append(TextCoder.alpha_dict.get(char, TextCoder.alpha_dict.get("?")))

        # print(len(n))
        # print(n)
        # print(self.number_of_char_in_block)

        n = ['1'*7] * (self.number_of_char_in_block - len(n) % self.number_of_char_in_block) + n
        # print(len(n))
        print(n)

        result = []

        for i in range(len(n) // self.number_of_char_in_block):
            current = []
            for j in range(self.number_of_char_in_block):
                current.append(n[i*self.number_of_char_in_block+j])
            result.append(str(int("".join(current), 2)))

        return ",".join(result)

    def number_to_text(self, number):
        b = bin(number)[2:]
        b = b.rjust(7*self.number_of_char_in_block, "0")
        step = 7
        parts = [b[i:i + step] for i in range(0, len(b), step)]
        text = [TextCoder.code_dict.get(i) for i in parts]

        return ''.join(text)

    def numbers_to_text(self, numbers: str):
        return ''.join([self.number_to_text(int(i)) for i in numbers.split(",")])


if __name__ == "__main__":
    print(f"Алфавит содержит следующие символы")
    print(TextCoder.alpha_dict)

    text = "Всем привет! Это супер алгоритм!"
    a = TextCoder(128**5)
    n = a.text_to_numbers(text)
    print(n)

    print(a.number_to_text(34359726353))
    # 575750,3735292041,818216053,16683104914,5402364149,293668753
    print(a.numbers_to_text(n))

    # table_data = [[symbol if symbol != " " else "[ПРОБЕЛ]", code] for code, symbol in TextCoder.code_dict.items()]
    # table_data[0][0] = "[ПУСТО]"
    #
    # print(tabulate(table_data, headers=["Символ", "Код"], tablefmt="grid"))

