import heapq
from collections import Counter
from collections import namedtuple
from struct import *  
import pickle


# класс для ветвей дерева - внутренних узлов; у них есть потомки
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        # обход дерева
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# класс для листьев дерева, у него нет потомков, но есть значение символа
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"
        code[self.char] = acc or "0"


# функция кодирования строки в коды Хаффмана
def huffman_encode(s):
    h = []  # очередь

    # построим очередь
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    # построим очередь с приоритетами
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна сумме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}  # словарь кодов символов
    if h:  # если строка существует
        # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        [(_freq, _count, root)] = h
        # обойдем дерева от корня и заполним словарь
        root.walk(code, "")

    return code


def main():
    input_file = open("HUFFMAN/original.txt", "r")
    # input_file = open("HUFFMAN/The two brothers.txt", "r")

    output_file = open("HUFFMAN/compressed.huff", "wb")
    dictionary_file = open("HUFFMAN/dictionary.pkl", "wb")

    s = input_file.read() # чтение исходного файла

    code = huffman_encode(s)  # получаем словарь
    encoded = "".join(code[ch] for ch in s)  # закодируем каждый символ

    print(encoded)
    # выведем число символов и длину закодированной строки
    print(len(code), len(encoded))
    for ch in sorted(code):
        # выведем символ и соответствующий ему код
        print("{}: {}".format(ch, code[ch]))

    len_encoded = len(encoded) # длина закодированной строки
    zero_counter = 16 - len_encoded % 16 # сколько не хватает до 16 в конце строки
    encoded += '0' * zero_counter
    for i in range(0, len(encoded), 16): # запись в файл закодированной строки
        output_file.write(pack('>H', int(encoded[i:i+16], 2)))

    # добавление в конец словаря элемента, показывающего количество незначящих нулей в конце строки
    code['zero_counter'] = zero_counter
    pickle.dump(code, dictionary_file) # запись словаря в файл
 
    input_file.close()
    output_file.close()
    dictionary_file.close()


if __name__ == "__main__":
    main()