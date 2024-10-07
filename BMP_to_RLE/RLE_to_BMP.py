import numpy as np
from PIL import Image

def save_img(arr):
    img = Image.fromarray(arr, mode='RGB')
    img.save("BMPtoRLE/image_restored.bmp", format='BMP', quality=100, optimize=False, compress_level=0)


def restore(src, x, y):
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

    print(np.array(result, dtype='uint8').reshape(y, x, 3))
                
    return np.array(result, dtype='uint8').reshape(y, x, 3)
    

if __name__ == "__main__":
    compressed = open('BMPtoRLE/1-compressed.rle', 'rb')
    string = compressed.read()
    arr = np.array([x for x in string])
    arr = arr.reshape(int(len(arr)/3), 3)
    x = 236
    y = 414
    restored_arr = restore(arr, x, y)
    save_img(restored_arr)
    compressed.close()