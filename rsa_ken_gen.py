from algorithms import generate_primes, euler, generate_e, generate_d

class RSAKeyGen:
    @staticmethod
    def generate_keys(start_num=2*5, end_num=2**10):
        # генерируем 2 простых числа в задном диапозоне
        p, q = generate_primes(start_num, end_num)
        n = p*q
        # print(f"Сгенерированы p и q")
        print(f"p = {p}")
        print(f"q = {q}")
        print(f"n = p*q = {n}")

        phi = euler(p, q)
        print(f"phi (функция Эйлера) = {phi}")

        e = generate_e(phi)
        d = generate_d(phi, e)
        print(f'\nОткрытый ключ (e, n) = ({e}, {n})')
        print(f'Закрытый ключ (d, n) = ({d}, {n})')

        return p, q, n, e, d


if __name__ == '__main__':
    # start = 2**5
    # end = 2**10

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

    RSAKeyGen.generate_keys(start, end)


