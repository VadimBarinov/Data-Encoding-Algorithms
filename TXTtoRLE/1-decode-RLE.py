def restore(src):
    result = ""
    if src:
        # Номер счетчика повторений в байтовом массиве
        i = 0
        while i < len(src):
            # Если имеется 1 в верхнем бите
            if(src[i] >= 128):
                # Добавление цепочки одинаковых байтов
                result += str(chr(src[i+1])) * (src[i] - 128)
                i += 2
            # Если в верхнем бите 0
            else:
                for j in range(1, src[i] + 1):
                    # Добавление последовательности неповторяющихся байтов
                    result += str(chr(src[i+j]))
                i += src[i] + 1
                
    return result
    

if __name__ == "__main__":
    compressed = open('TXTtoRLE/1-compressed.rle', 'rb')
    string = compressed.read()
    print(string)
    restored = open('TXTtoRLE/1-restored.txt', 'w')
    restored.write(restore(string))
    compressed.close()
    restored.close()