from struct import *

# Входной файл
input_file = "original.txt"
# Максимальный размер таблицы
n = 16                  # можно менять для достижения лучшего сжатия
maximum_table_size = pow(2,int(n))      
file = open(input_file)                 
data = file.read()                      

# Создание и инициализация словаря
dictionary_size = 256                   
dictionary = {chr(i): i for i in range(dictionary_size)}    
string = ""             # строка
compressed_data = []    # переменная для хранения сжатого текста

# Перебор входных символов
# LZW 
for symbol in data:                     
    string_plus_symbol = string + symbol
    # Если встретилось в словаре
    if string_plus_symbol in dictionary: 
        # Добавление к строке нового символа 
        string = string_plus_symbol
    else:
        # Добавление в сжатый текст индекс стооки из словаря
        compressed_data.append(dictionary[string])
        # Проверка на размер словаря (должен быть меньше указанного)
        # Иначе перестает добавлять новую строку в словарь
        if(len(dictionary) <= maximum_table_size):
            # Добавление новой строки в словарь
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

# Добавление индекса последней строки в сжатый текст
if string in dictionary:
    compressed_data.append(dictionary[string])

# Сохранение в байтовом виде
out = "compressed.lzw"
output_file = open(out, "wb")
for data in compressed_data:
    output_file.write(pack('>H',int(data)))
    
output_file.close()
file.close()
