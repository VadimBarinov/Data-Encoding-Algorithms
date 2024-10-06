import numpy as np
from PIL import Image

# Нужно переделать функцию,
# чтобы преоьразовывала в многомерный массив и потом в изображение
def restore(src):

    result = []

    # Номер счетчика повторений в байтовом массиве
    i = 0
    while i < len(src):
        # Если имеется 1 в верхнем бите
        if(src[i][0] >= 128):
            # Добавление цепочки одинаковых байтов
            for j in range(0, (src[i][0] - 128)):
                result.append(src[i+1])
            i += 2
        # Если в верхнем бите 0
        else:
            for j in range(1, src[i][0] + 1):
                # Добавление последовательности неповторяющихся байтов
                result.append(src[i+j])
            i += src[i][0] + 1

    print(np.array(result))
    print(len(np.array(result)))
                
    return np.array(result).reshape(480, 640, 3)
    

if __name__ == "__main__":
    compressed = open('1-compressed.rle', 'rb')
    string = compressed.read()
    arr = np.array([x for x in string])
    arr = arr.reshape(int(len(arr)/3), 3)
    restored = open('1-restored.txt', 'w')
    restored.write(restore(arr))
    compressed.close()
    restored.close()