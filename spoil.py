import random

error_count = 0

def compare():
    text1 = open("original.txt").read()
    text2 = open("hamming_decode.txt").read()
    res = 0
    print(f"Всего символов в оригинальном файле: {len(text1)}")
    print(f"Всего символов в декодированном файле: {len(text2)}")
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            res += 1
    return res


def run():
    p = 0.01
    file = open("hamming_encode.txt", "r")
    text = file.read()
    new_text = ""
    file.close()
    global error_count

    for i in range(len(text)):
        if random.randint(0, 10000) / 10000 < p:
            if text[i] == '0':
                new_text += '1'
            else:
                new_text += '0'
            error_count+=1
        else:
            new_text += text[i]
    file = open("hamming_encode.txt", "w")
    file.write(str(new_text))
    file.close()

