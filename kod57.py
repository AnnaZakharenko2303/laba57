import random

def input_matrix():
    """Ввод матрицы вручную."""
    global matrix
    rows = int(input("Введите количество строк: "))
    matrix = []
    
    for i in range(rows):
        row = list(map(int, input(f"Введите элементы строки {i + 1} (через пробел): ").split()))
        matrix.append(row)

def generate_matrix():
    """Генерация случайной матрицы."""
    global matrix
    rows = random.randint(2, 5)  # Случайное количество строк
    cols = random.randint(2, 5)  # Случайное количество столбцов
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    
    print("Сгенерированная матрица:")
    output_matrix(matrix)

def process_matrix(matrix):
    """Обработка матрицы: сортировка и добавление столбца с суммами модулей."""
    sums = [sum(abs(x) for x in row) for row in matrix]
    
    # Создаем новую матрицу с добавленным столбцом сумм
    new_matrix = [row + [sums[i]] for i, row in enumerate(matrix)]
    
    # Сортируем по убыванию суммы модулей
    new_matrix.sort(key=lambda x: x[-1], reverse=True)
    
    return new_matrix

def output_matrix(matrix):
    """Вывод матрицы."""
    if not matrix:
        print("Матрица пуста.")
        return
    
    for row in matrix:
        print("\t".join(map(str, row)))

def menu():
    """Основное меню приложения."""
    global matrix, result
    matrix = []
    result = []

    while True:
        print("\n1) Ввод матрицы вручную")
        print("2) Генерация случайной матрицы")
        print("3) Обработка матрицы")
        print("4) Вывод результата")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            input_matrix()
            result.clear()  # Сбрасываем результаты при вводе новых данных
        elif choice == '2':
            generate_matrix()
            result.clear()  # Сбрасываем результаты при генерации новых данных
        elif choice == '3':
            if not matrix:
                print("Ошибка: матрица не введена. Пожалуйста, введите данные или сгенерируйте их.")
                continue
            result = process_matrix(matrix)
            print("Матрица обработана.")
        elif choice == '4':
            output_matrix(result)
        elif choice == '0':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if name == "main":
    menu()
