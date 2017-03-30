import des_tables
import des_utils

try:
    input = raw_input
except NameError:
    pass

def permutate(binary, table):
    permutated = ''
    length = len(table)
    for i in range(length):
        permutated += binary[table[i] - 1]
    return permutated


def sbox(binary):
    b = ''
    for i in range(0, len(binary), 6):
        x = int(binary[i] + binary[i + 5], 2)
        y = int(binary[i + 1:i + 5], 2)
        b += des_utils.int_to_binary(des_tables.SBOX[i / 6][x][y])
    return b

def encrypt(plain, key_text):
    plain_text_split = des_utils.string_to_array(plain, 8)
    plain_binary_split = []
    for p in plain_text_split:
        plain_binary_split.append(des_utils.string_to_binary(p))
    print ''
    des_utils.debug('plain text', [plain])
    des_utils.debug('splitted', plain_text_split)
    des_utils.debug('plain binary', plain_binary_split)

    # key
    key = key_text
    key_binary = des_utils.string_to_binary(key)
    print ''
    des_utils.debug('key', key)
    des_utils.debug('key binary', key_binary, 8)

    # generate C, D
    cd0 = permutate(key_binary, des_tables.PC1)
    c = [cd0[:len(des_tables.PC1) / 2]]
    d = [cd0[len(des_tables.PC1) / 2:]]
    print ''
    des_utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(des_utils.left_shift(c[i], des_tables.LEFT_SHIFT[i]))
        d.append(des_utils.left_shift(d[i], des_tables.LEFT_SHIFT[i]))
        des_utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    # generate K
    print ''
    k = ['']
    for i in range(16):
        k.append(permutate(c[i + 1] + d[i + 1], des_tables.PC2))
        des_utils.debug('K' + str(i + 1), k[i + 1], 6)

    final_cipher = ''

    for i in range(len(plain_text_split)):

        # generate L, R
        lr0 = permutate(plain_binary_split[i], des_tables.IP)
        l = [lr0[:len(des_tables.IP) / 2]]
        r = [lr0[len(des_tables.IP) / 2:]]
        print ''
        des_utils.debug('L0', l[0], 8)
        des_utils.debug('R0', r[0], 8)

        # ---
        er = []
        a = ['']
        b = ['']
        pb = ['']
        for i in range(16):
            er.append(permutate(r[i], des_tables.EXPANSION))
            a.append(des_utils.xor(er[i], k[i + 1]))
            b.append(sbox(a[i + 1]))
            pb.append(permutate(b[i + 1], des_tables.PBOX))
            r.append(des_utils.xor(l[i], pb[i + 1]))
            l.append(r[i])
            print ''
            des_utils.debug('ER' + str(i), er[i], 6)
            des_utils.debug('A' + str(i + 1), a[i], 6)
            des_utils.debug('B' + str(i + 1), b[i], 4)
            des_utils.debug('PB' + str(i + 1), pb[i], 8)
            des_utils.debug('R' + str(i + 1), r[i + 1], 8)
            des_utils.debug('L' + str(i + 1), l[i + 1], 8)

        # cipher
        cipher_binary = permutate(r[16] + l[16], des_tables.IP_INV)
        cipher_binary_split = des_utils.string_to_array(cipher_binary, 8)
        cipher = ''
        for i in range(len(cipher_binary_split)):
            cipher += des_utils.binary_to_hex(cipher_binary_split[i])

        final_cipher += cipher

    return final_cipher

def decrypt(cipher, key_text):
    key = key_text
    key_binary = des_utils.string_to_binary(key)
    print ''
    des_utils.debug('key', key)
    des_utils.debug('key binary', key_binary, 8)

    # generate C, D
    cd0 = permutate(key_binary, des_tables.PC1)
    c = [cd0[:len(des_tables.PC1) / 2]]
    d = [cd0[len(des_tables.PC1) / 2:]]
    print ''
    des_utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(des_utils.left_shift(c[i], des_tables.LEFT_SHIFT[i]))
        d.append(des_utils.left_shift(d[i], des_tables.LEFT_SHIFT[i]))
        des_utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    # generate K
    print ''
    k = ['']
    for i in range(16):
        k.append(permutate(c[i + 1] + d[i + 1], des_tables.PC2))
        des_utils.debug('K' + str(i + 1), k[i + 1], 6)

    textbits = []
    ciphertext = ''
    for i in cipher:
        ciphertext += des_utils.hex_to_binary(i)
    for i in ciphertext:
        textbits.append(int(i))
    print textbits
    print ciphertext
    number_of_vacancy = len(textbits) % 64
    need_pads = number_of_vacancy > 0
    if need_pads:
        for i in range(64 - number_of_vacancy):
            textbits.append(0)

    final_cipher = ''
    for i in range(len(cipher)):

        # generate L, R
        lr0 = permutate(cipher[i], des_tables.IP)
        l = [lr0[:len(des_tables.IP) / 2]]
        r = [lr0[len(des_tables.IP) / 2:]]
        print ''
        des_utils.debug('L0', l[0], 8)
        des_utils.debug('R0', r[0], 8)

        # ---
        er = []
        a = ['']
        b = ['']
        pb = ['']
        for i in range(16):
            er.append(permutate(r[i], des_tables.EXPANSION))
            a.append(des_utils.xor(er[i], k[i + 1]))
            b.append(sbox(a[i + 1]))
            pb.append(permutate(b[i + 1], des_tables.PBOX))
            r.append(des_utils.xor(l[i], pb[i + 1]))
            l.append(r[i])
            print ''
            des_utils.debug('ER' + str(i), er[i], 6)
            des_utils.debug('A' + str(i + 1), a[i], 6)
            des_utils.debug('B' + str(i + 1), b[i], 4)
            des_utils.debug('PB' + str(i + 1), pb[i], 8)
            des_utils.debug('R' + str(i + 1), r[i + 1], 8)
            des_utils.debug('L' + str(i + 1), l[i + 1], 8)

        # cipher
        cipher_binary = permutate(r[16] + l[16], des_tables.IP_INV)
        cipher_binary_split = des_utils.string_to_array(cipher_binary, 8)
        cipher = ''
        for i in range(len(cipher_binary_split)):
            cipher += des_utils.binary_to_hex(cipher_binary_split[i])

        final_cipher += cipher

    return final_cipher.rstrip('\x00')


def main():
    print('Pilih : ')
    print('1. ENCRYPT')
    print('2. DECRYPT')
    choice = int(input())

    key_text = str(input('key : \n'))

    if(len(key_text) < 8):
    	print('Key harus terdiri dari 8 karakter')
    	return

    if(choice == 1):
        print ('string : ')
        plain = str(input())
        cipher = encrypt(plain, key_text)
        print('\nCipher : ')
        print(cipher)

    else:
        cipher = str(input('Cipher :\n'))
        plaintext = decrypt(cipher, key_text)
        print('\nString :')
        print(final)

    print('\nKeluar...')
    return

if __name__ == "__main__":
    main()