import numpy as np

H = [[0, 1, 1],
     [1, 0, 1],
     [1, 1, 0],
     [1, 1, 1],
     [1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]


def get_syndrome(array):
    S = [0, 0, 0]
    for i in range(0, 3):
        suma = 0
        for j in range(0, 7):
            suma += array[j] * H[j][i]
        S[i] = int(suma % 2)
    return S


def decode(array):
    decoded_word = [0, 0, 0, 0]
    for i in range(0, 4):
        decoded_word[i] = array[i]
    return decoded_word


def fix_word(syndrome, segment):
    x1 = [0] * 4
    is_correct = True
    error_index = 0

    for i in range(0, 7):
        if syndrome == H[i]:
            error_index = i
            is_correct = False

    if not is_correct:
        print("Ошибка была допущена в блоке " + str(segment) + " в бите " + str(error_index) + "  и была исправлена.")
        if segment[error_index] == 1:
            segment[error_index] = 0
        else:
            segment[error_index] = 1
        print("Исправленный блок: " + str(segment))

    return segment


def run():
    segment = [0] * 7
    text = open("hamming_encode.txt", "r").read().rstrip()

    index = 0
    x = [0] * 4
    file = open("hamming_decode.txt", "w")

    for char in text:
        if char != '\n':
            segment[index] = ord(char) - ord('0')
            index += 1

            if index == 7:
                syndrome = get_syndrome(segment)
                index = 0
                x = decode(fix_word(syndrome, segment))
                for i in range(0, 4):
                    file.write(str(x[i]))

    file.close()
