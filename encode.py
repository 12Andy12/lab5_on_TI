import numpy as np

# порождающая матрица
G = [[1, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 1, 1, 1]]


def hamming_code(segment):
    res = [0] * 7
    for i in range(0, 7):
        suma = 0
        for j in range(0, 4):
            suma += segment[j] * G[j][i]
        res[i] = int(suma % 2)
    return res


def run():
    segment = [0] * 4

    text = open("original.txt", "r").read().rstrip()
    index = 0

    file = open("hamming_encode.txt", "w")
    for char in text:
        if char != '\n':
            segment[index] = ord(char) - ord('0')
            index += 1
            if index == 4:
                res = hamming_code(segment)
                for index in range(0, 7):
                    file.write(str(res[index]))
                index = 0
    file.close()
