
hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
          '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

hex_revesred_dict = {v: k for k, v in hex_dict.items()}

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
    return hex_revesred_dict[hex]

def int_to_binary(num):
    return format(num, 'b').zfill(4)


def binary_to_int(binary):
    return int(binary, 2)


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

def add_pads_if_necessary(s):
    """adding bits to make an integer number of 64-bit blocks
    """
    number_of_vacancy = len(s) % 64
    need_pads = number_of_vacancy > 0
    if need_pads:
        for i in range(64 - number_of_vacancy):
            s.append(0)
    return s