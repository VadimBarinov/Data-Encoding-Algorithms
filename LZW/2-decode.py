from struct import *

def init_dictionary():
    # Создание и инициализация словаря
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])
    return [dictionary, dictionary_size]

def lzw_decompression(compressed_data, dictionary):
    next_code = 256
    decompressed_data = ""  # переменная для хранения восстановленного текста
    string = ""             # строка

    # Перебор индексов
    # LZW Decompression
    for code in compressed_data:
        # Если индекса нет в словаре
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        # Добавление строки по индексу
        decompressed_data += dictionary[code]
        if len(string) != 0:
            # Добавление в словарь новой строки 
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    return decompressed_data


def main():
    # Входной сжатый файл
    input_file = "LZW/compressed.lzw"
    # Максимальный размер таблицы
    n = 16                  # можно менять для достижения лучшего сжатия          
    maximum_table_size = pow(2,int(n))
    file = open(input_file, "rb")
    compressed_data = []
    
    # Чтение входного сжатого файла
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    dictionary, dictionary_size = init_dictionary()

    decompressed_data = lzw_decompression(compressed_data, dictionary)    

    # Сохранение восстановленного файла
    output_file = open("LZW/restored.txt", "w")
    for data in decompressed_data:
        output_file.write(data)
        
    output_file.close()
    file.close()


if __name__ == "__main__":
    main()
