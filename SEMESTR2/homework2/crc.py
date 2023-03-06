CRC_POLYMINAL = 0x04C11DB7

def encodeCRC(input_data: str, crc_pol: int = CRC_POLYMINAL) -> int:    # 0x04C11DB7 - CRC-32-IEEE code
    binary_data = ""
    for i in range(len(input_data)):
        binary_data += bin(ord(input_data[i]))[2:]

    poly_pow = len(bin(crc_pol)[2:]) - 1
    binary_data += "0" * poly_pow

    crc_xor = int(binary_data[:poly_pow + 1], 2) ^ crc_pol
    offset = 1
    crc_xor_str = bin(crc_xor)[2:]
    while offset < len(binary_data) - poly_pow:
        if len(crc_xor_str) == poly_pow + 1:
            crc_xor = int(crc_xor_str, 2) ^ crc_pol
            crc_xor_str = bin(crc_xor)[2:] + binary_data[poly_pow + offset]         
        else:
            crc_xor_str += binary_data[poly_pow + offset]
        offset += 1
        if offset == len(binary_data) - poly_pow:
            crc_xor = int(crc_xor_str, 2)

    return crc_xor

def decodeCRC(input_data: str, code_crc: int, crc_pol: int = CRC_POLYMINAL) -> bool:
    binary_data = ""
    for i in range(len(input_data)):
        binary_data += bin(ord(input_data[i]))[2:]
    poly_pow = len(bin(crc_pol)[2:]) - 1
    crc_bin = bin(code_crc)[2:]
    count_zeros = poly_pow - len(crc_bin)

    binary_data += "0" * count_zeros + crc_bin

    crc_xor = int(binary_data[:poly_pow + 1], 2) ^ crc_pol
    offset = 1
    crc_xor_str = bin(crc_xor)[2:]
    while offset < len(binary_data) - poly_pow:
        if len(crc_xor_str) == poly_pow + 1:
            crc_xor = int(crc_xor_str, 2) ^ crc_pol
            crc_xor_str = bin(crc_xor)[2:] + binary_data[poly_pow + offset]         
        else:
            crc_xor_str += binary_data[poly_pow + offset]
        offset += 1
        if offset == len(binary_data) - poly_pow:
            crc_xor = int(crc_xor_str, 2)
    return crc_xor == 0