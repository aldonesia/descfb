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

def convert_plain_to_binary_splitted(plain):
    plain_splitted = des_utils.string_to_array(plain, 8)
    plain_binary_splitted = []
    for p in plain_splitted:
        plain_binary_splitted.append(des_utils.string_to_binary(p))
    des_utils.forceDebugLine()
    des_utils.forceDebug('plain text           ', plain)
    des_utils.forceDebug('plain splitted       ', plain_splitted)
    des_utils.forceDebug('plain splitted binary', plain_binary_splitted)
    return plain_binary_splitted

def encrypt(plain, key_text, iv):
    plain_binary_splitted = convert_plain_to_binary_splitted(plain)
    block = len(plain_binary_splitted)
    
    key_bin =  des_utils.convert_key_to_binary(key_text)

    iv_bin =  des_utils.convert_iv_to_binary(iv)

    cd0 = permutate(key_bin, des_tables.PC1)
    c = [cd0[:len(des_tables.PC1) / 2]]
    d = [cd0[len(des_tables.PC1) / 2:]]
    des_utils.debugLine()
    des_utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(des_utils.left_shift(c[i], des_tables.LEFT_SHIFT[i]))
        d.append(des_utils.left_shift(d[i], des_tables.LEFT_SHIFT[i]))
        des_utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    des_utils.debugLine()
    k = ['']
    for i in range(16):
        k.append(permutate(c[i + 1] + d[i + 1], des_tables.PC2))
        des_utils.debug('K' + str(i + 1), k[i + 1], 6)

    plain_binary_splitted = [iv_bin] + plain_binary_splitted
    cipher_binary_splitted = [iv_bin]
    for i in range(block):
        temp = cipher_binary_splitted[i]

        lr0 = permutate(temp, des_tables.IP)
        l = [lr0[:len(des_tables.IP) / 2]]
        r = [lr0[len(des_tables.IP) / 2:]]
        des_utils.debugLine()
        des_utils.debug('L0', l[0], 8)
        des_utils.debug('R0', r[0], 8)

         # core
        er = []
        a = ['']
        b = ['']
        pb = ['']
        for j in range(16):
            er.append(permutate(r[j], des_tables.EXPANSION))
            a.append(des_utils.xor(er[j], k[j + 1]))
            b.append(sbox(a[j + 1]))
            pb.append(permutate(b[j + 1], des_tables.PBOX))
            r.append(des_utils.xor(l[j], pb[j + 1]))
            l.append(r[j])
            des_utils.debugLine()
            des_utils.debug('ER' + str(j), er[j], 6)
            des_utils.debug('A' + str(j + 1), a[j + 1], 6)
            des_utils.debug('B' + str(j + 1), b[j + 1], 4)
            des_utils.debug('PB' + str(j + 1), pb[j + 1], 8)
            des_utils.debug('R' + str(j + 1), r[j + 1], 8)
            des_utils.debug('L' + str(j + 1), l[j + 1], 8)

        des_k = permutate(r[16] + l[16], des_tables.IP_INV)
        cipher_binary_temp = des_utils.xor(plain_binary_splitted[i + 1], des_k)
        cipher_binary_splitted.append(cipher_binary_temp)
    plain_binary_splitted.remove(iv_bin)
    cipher_binary_splitted.remove(iv_bin)

    cipher_binary = ''
    cipher_hex = ''
    for c in cipher_binary_splitted:
        cipher_binary += c
        cipher_hex += des_utils.convert_cipher_temp_to_hex(c)
    return cipher_hex


def decrypt(cipher, key_text, iv):
    cipher = cipher.decode('hex')
    plain_binary_splitted = convert_plain_to_binary_splitted(cipher)
    block = len(plain_binary_splitted)

    key_bin =  des_utils.convert_key_to_binary(key_text)

    iv_bin =  des_utils.convert_iv_to_binary(iv)

    cd0 = permutate(key_bin, des_tables.PC1)
    c = [cd0[:len(des_tables.PC1) / 2]]
    d = [cd0[len(des_tables.PC1) / 2:]]
    des_utils.debugLine()
    des_utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(des_utils.left_shift(c[i], des_tables.LEFT_SHIFT[i]))
        d.append(des_utils.left_shift(d[i], des_tables.LEFT_SHIFT[i]))
        des_utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)
        
    des_utils.debugLine()
    k = ['']
    for i in range(16):
        k.append(permutate(c[i + 1] + d[i + 1], des_tables.PC2))
        des_utils.debug('K' + str(i + 1), k[i + 1], 6)

    plain_binary_splitted = [iv_bin] + plain_binary_splitted
    cipher_binary_splitted = [iv_bin]
    for i in range(block):
        temp = plain_binary_splitted[i]

        lr0 = permutate(temp, des_tables.IP)
        l = [lr0[:len(des_tables.IP) / 2]]
        r = [lr0[len(des_tables.IP) / 2:]]
        des_utils.debugLine()
        des_utils.debug('L0', l[0], 8)
        des_utils.debug('R0', r[0], 8)

         # core
        er = []
        a = ['']
        b = ['']
        pb = ['']
        for j in range(16):
            er.append(permutate(r[j], des_tables.EXPANSION))
            a.append(des_utils.xor(er[j], k[j + 1]))
            b.append(sbox(a[j + 1]))
            pb.append(permutate(b[j + 1], des_tables.PBOX))
            r.append(des_utils.xor(l[j], pb[j + 1]))
            l.append(r[j])
            des_utils.debugLine()
            des_utils.debug('ER' + str(j), er[j], 6)
            des_utils.debug('A' + str(j + 1), a[j + 1], 6)
            des_utils.debug('B' + str(j + 1), b[j + 1], 4)
            des_utils.debug('PB' + str(j + 1), pb[j + 1], 8)
            des_utils.debug('R' + str(j + 1), r[j + 1], 8)
            des_utils.debug('L' + str(j + 1), l[j + 1], 8)

        des_k = permutate(r[16] + l[16], des_tables.IP_INV)
        cipher_binary_temp = des_utils.xor(plain_binary_splitted[i + 1], des_k)
        cipher_binary_splitted.append(cipher_binary_temp)
    plain_binary_splitted.remove(iv_bin)
    cipher_binary_splitted.remove(iv_bin)

    cipher_binary = ''
    cipher_hex = ''
    for c in cipher_binary_splitted:
        cipher_binary += c
        cipher_hex += des_utils.convert_cipher_temp_to_hex(c)
    cipher = cipher_hex.decode('hex')
    return cipher

def main():
    print('Pilih : ')
    print('1. ENCRYPT')
    print('2. DECRYPT')
    choice = int(input())

    key_text = str(input('key (HEX): \n'))
    iv = str(input('iv (STRING): \n'))

    # if(len(key_text) < 8):
    #     print('Key harus terdiri dari 8 karakter')
<<<<<<< HEAD
    #     return
=======
    #    return
>>>>>>> 70cb4fd39293e0851cde12bda4fdb666198edfbb

    # if(len(iv) < 8):
    #     print('iv harus terdiri dari 8 karakter')
    #     return

    if(choice == 1):
        print ('string : ')
        plain = str(input())
        cipher = encrypt(plain, key_text, iv)
        print('\nCipher : ')
        print(cipher)

    else:
        cipher = str(input('Cipher :\n'))
        final = decrypt(cipher, key_text, iv)
        print('\nString :')
        print(final)

    print('\nKeluar...')
    return

if __name__ == "__main__":
    des_utils.enableDebug = False
    main()