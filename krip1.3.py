# Функция для шифрования текста вертикальной перестановкой
def encrypt(text, key):
    encrypted_text = ''
    for i in range(key):
        encrypted_text += text[i::key]  # Добавляем символы с заданным шагом
    return encrypted_text

# Функция для дешифровки текста вертикальной перестановкой
def decrypt(encrypted_text, key):
    decrypted_text = [''] * len(encrypted_text)  # Инициализируем список символами-разделителями
    idx = 0
    for i in range(key):
        for j in range(i, len(encrypted_text), key):
            decrypted_text[j] = encrypted_text[idx]  # Заполняем символы в соответствии с шагом
            idx += 1
    return ''.join(decrypted_text)  # Объединяем символы в строку

# Функция для построения таблицы частот биграмм
def build_frequency_table(text):
    frequency_table = {}
    for i in range(len(text) - 1):
        bigram = text[i:i+2]  # Формируем биграммы
        if bigram in frequency_table:
            frequency_table[bigram] += 1  # Увеличиваем счетчик частоты биграммы
        else:
            frequency_table[bigram] = 1  # Создаем новую биграмму в таблице частот
    return frequency_table

# Функция для создания дерева следования столбцов
def create_column_order_tree(frequency_table):
    sorted_bigrams = sorted(frequency_table.items(), key=lambda x: x[1], reverse=True)
    column_order_tree = {}
    for bigram, _ in sorted_bigrams:
        node = column_order_tree
        for char in bigram:
            if char not in node:
                node[char] = {}  # Создаем новую вершину в дереве следования столбцов
            node = node[char]
    return column_order_tree

# Функция для вывода дерева следования столбцов в консоль
def print_column_order_tree(node, depth=0):
    for char, subtree in node.items():
        print('  ' * depth + char)  # Выводим символ с отступом, зависящим от уровня глубины
        print_column_order_tree(subtree, depth + 1)  # Рекурсивно обрабатываем поддерево

# Основная функция программы
def main():
    plaintext = "soataliyev"
    key = 3

    # Шифрование
    encrypted_text = encrypt(plaintext, key)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Криптоанализ
    frequency_table = build_frequency_table(encrypted_text)
    print("Таблица частот биграмм:")
    print(frequency_table)

    column_order_tree = create_column_order_tree(frequency_table)
    print("\nДерево следования столбцов:")
    print_column_order_tree(column_order_tree)

    # Расшифровка
    decrypted_text = decrypt(encrypted_text, key)
    print(f"\nРасшифрованный текст: {decrypted_text}")

# Запуск программы при ее вызове
if __name__ == "__main__":
    main()
