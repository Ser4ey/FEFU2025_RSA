from tabulate import tabulate

class TextCoder:
    alpha = ['', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',
             'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
             'Ю', 'Я', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '!', '?', ';', ':', '(', ')',
             '"', "'"]

    alpha_set = set(alpha)

    alpha_dict = dict(zip([bin(i)[2:].rjust(7, "0") for i in range(128)], alpha))

    def __init__(self, block_size=128):
        self.block_size = block_size
        self.number_of_char_in_block = block_size // 128
        if self.number_of_char_in_block == 0:
            raise Exception('Размер блока n слишком маленький. Минимальный размер 128')

        print(f"[+] Кодеровщик иницилизирован. Размер блока: {block_size}. "
              f"Блок содержит: {self.number_of_char_in_block} символов")


if __name__ == "__main__":
    print(f"Алфавит содержит следующие символы")
    print(TextCoder.alpha_dict)

    table_data = [[symbol if symbol != " " else "[ПРОБЕЛ]", code] for code, symbol in TextCoder.alpha_dict.items()]
    table_data[0][0] = "[ПУСТО]"

    print(tabulate(table_data, headers=["Символ", "Код"], tablefmt="grid"))

