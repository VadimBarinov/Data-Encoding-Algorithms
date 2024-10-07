import numpy as np
from PIL import Image


def getImg(file):
    img = np.array(Image.open(file).convert('RGB'))
    return img

def listEquality(first, second):
    flag = 1
    for i in range(0, len(first)):
        if first[i] != second[i]: 
            flag = 0
    return flag
    

def rle(img, x, y):
    # Массив для результата
    result = []
    src = np.array(img).reshape(x*y, 3)
    # Текущий байт
    current = src[0]
    # Счетчик повторяющихся байтов
    counterDouble = 1
    # Последовательность неповторяющихся байтов
    subsequence = []
    subsequence.append(current)

    for e in src[1:]:
        if listEquality(e, current) and counterDouble < 127:
            counterDouble += 1
            # Добавление последовательности неповторяющихся байтов
            if (len(subsequence) > 1): 
                subsequence = subsequence[:-1]
                result.append(np.array([len(subsequence), 0, 0], dtype='uint8'))
                result += subsequence
            subsequence = []
        elif counterDouble > 1:
            # Добавление цепочки одинаковых байтов
            subsequence.append(e)
            result.append(np.array([(counterDouble + 128), 0, 0], dtype='uint8'))
            result.append(current)
            current = e
            counterDouble = 1
        else:
            if (len(subsequence) < 127):    
                subsequence.append(e)
                current = e
            else:
                # Добавление последовательности неповторяющихся байтов
                result.append(np.array([len(subsequence), 0, 0], dtype='uint8'))
                result += subsequence
                subsequence = []
                subsequence.append(e)
                current = e

    if (counterDouble > 1):
        # Добавление цепочки одинаковых байтов
        result.append(np.array([(counterDouble + 128), 0, 0], dtype='uint8'))
        result.append(current)
    else:
        # Добавление последовательности неповторяющихся байтов
        result.append(np.array([len(subsequence), 0, 0], dtype='uint8'))
        result += subsequence

    print(np.array(result, dtype="uint8"))
    return np.array(result, dtype="uint8").tobytes()


if __name__ == "__main__":

    file = 'BMPtoRLE/image.bmp'
    img = getImg(file)
    x = img.shape[1]
    y = img.shape[0]
    compressed = open('BMPtoRLE/1-compressed.rle', 'wb')
    compressed.write(rle(img, x, y))
    compressed.close()
