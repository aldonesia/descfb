def string_to_array(text, length):
    texts = []
    for i in range(0, len(text), length):
        texts.append(text[i:i + length])
    return texts


def string_to_binary(text):
    binary = ''
    for c in text:
        binary += (format(ord(c), 'b').zfill(8))
    for i in range(8 - len(text)):
        binary += '00000000'
    return binary

def hex_to_binary(hex):
    return bin(int(hex, 16))[2:].zfill(4)


def int_to_binary(num):
    return format(num, 'b').zfill(4)


def binary_to_int(binary):
    return int(binary, 2)

def binary_to_text(binary):
    return bin_to_text_dict[binary]

def binary_to_hex(binary):
    return hex(int(binary, 2))[2:].zfill(2)


def split_string(text, length):
    splitted = ''
    for i in range(0, len(text), length):
        splitted += text[i:i + length] + ' '
    return splitted


def left_shift(binary, num):
    return binary[num:] + binary[:num]


def xor(binary1, binary2):
    result = ''
    length = len(binary1)
    for i in range(length):
        if binary1[i] == binary2[i]:
            result += '0'
        else:
            result += '1'
    return result


def debug(tag, content, length=None):
    content = str(content)
    if length is None:
        print tag + ' : ' + content
    else:
        print tag + ' : ' + split_string(content, length)