from struct import *  
import pickle


# функция декодирования(закодированная строка, словарь)
def huffman_decode(encoded, code):
    sx =[] # раскодированная строка
    enc_ch = ""  # значение символа
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:  # если закодированный символ найден,
                sx.append(dec_ch)  # добавим значение символа
                enc_ch = ""  # обнулим значение закодированного символа
                break
    return "".join(sx)


def main():
    input_file = open("HUFFMAN/compressed.huff", "rb")
    dictionary_file = open("HUFFMAN/dictionary.pkl", "rb")
    output_file = open("HUFFMAN/restored.txt", "w")

    # чтение входного сжатого файла
    encoded = ""
    while True:
        rec = input_file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        # формируем входную строку
        encoded += "0" * (16 - len(bin(data)[2:])) + str(bin(data)[2:])

    code = pickle.load(dictionary_file)
    # убираем ненужные нули из конца строки
    encoded = encoded[:(len(encoded) - int(code['zero_counter']))]
    print(encoded)

    del code['zero_counter']

    output_string = huffman_decode(encoded, code)
    output_file.write(output_string)

    input_file.close()
    dictionary_file.close()
    output_file.close()


if __name__ == "__main__":
    main()