def rle(src):
    # Байтовый массив для результата
    result = bytearray()
    if src:
        # Текущий байт
        current = str(src[0])
        # Счетчик повторяющихся байтов
        counterDouble = 1
        # Последовательность неповторяющихся байтов
        subsequence = ""
        subsequence += current

        for e in src[1:]:
            if e == current and counterDouble < 127:
                counterDouble += 1
                # Добавление последовательности неповторяющихся байтов
                if (len(subsequence) > 1): 
                    subsequence = subsequence[:-1]
                    result.extend(bytes([len(subsequence)]))
                    result.extend((subsequence.encode('utf-8')))
                subsequence = ""
            elif counterDouble > 1:
                # Добавление цепочки одинаковых байтов
                subsequence += e
                result.extend(bytes([counterDouble + 128]))
                result.extend((current.encode('utf8')))
                current = e
                counterDouble = 1
            else:
                if (len(subsequence) < 127):    
                    subsequence += e
                    current = e
                else:
                    # Добавление последовательности неповторяющихся байтов
                    result.extend(bytes([len(subsequence)]))
                    result.extend((subsequence.encode('utf-8')))
                    subsequence = e
                    current = e

        if (counterDouble > 1):
            # Добавление цепочки одинаковых байтов
            result.extend(bytes([counterDouble + 128]))
            result.extend((current.encode('utf8')))
        else:
            # Добавление последовательности неповторяющихся байтов
            result.extend(bytes([len(subsequence)]))
            result.extend((subsequence.encode('utf-8')))

    return result


if __name__ == "__main__":

    original = open('TXTtoRLE/1-original.txt', 'r')
    string = original.read()
    compressed = open('TXTtoRLE/1-compressed.rle', 'wb')
    compressed.write(rle(string))
    original.close()
    compressed.close()
