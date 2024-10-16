from struct import *  
import pickle
from encode_huffman import huffman_encode

# аргументы: (закодированная строка, словарь)
def huffman_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
    sx =[]  # инициализируем массив символов раскодированной строки
    enc_ch = ""  # инициализируем значение закодированного символа
    for ch in encoded:  # обойдем закодированную строку по символам
        enc_ch += ch  # добавим текущий символ к строке закодированного символа
        for dec_ch in code:  # постараемся найти закодированный символ в словаре кодов
            if code.get(dec_ch) == enc_ch:  # если закодированный символ найден,
                sx.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
                enc_ch = ""  # обнулим значение закодированного символа
                break
    return "".join(sx)  # вернем значение раскодированной строки

def main():
    input_file = open("HUFFMAN/compressed.huff", "rb")
    dictionary_file = open("HUFFMAN/dictionary.pkl", "rb")
    output_file = open("HUFFMAN/restored.txt", "w")

    code = pickle.load(dictionary_file)
    # нужно придумать как распаковать 
    encoded = "".join(bin(elem)[2:] for elem in input_file.read())
    encoded = encoded[:(len(encoded) - int(code['zero_counter']))]
    print(encoded)

    output_string = huffman_decode(encoded, code)

    output_file.write(output_string)

    input_file.close()
    dictionary_file.close()
    output_file.close()

if __name__ == "__main__":
    main()