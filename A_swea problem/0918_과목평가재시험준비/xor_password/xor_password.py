def xor_encrypt_decrypt():
    # 입력 받기
    message = input("암호화할 문자열: ")  # 예: HELLO
    key = input("암호화 키 (한 글자): ")  # 예: K

    print(f"\n원본 메시지: {message}")
    print(f"암호화 키: {key}")

    # 키의 ASCII 값
    key_ascii = ord(key)
    print(f"키의 ASCII 값: {key_ascii} (이진: {bin(key_ascii)})")

    # 1. 암호화 과정
    encrypted = ""
    encrypted_hex = ""

    print(f"\n=== 암호화 과정 ===")
    for i, char in enumerate(message):
        char_ascii = ord(char)  # 문자의 ASCII 값

        # XOR 연산 수행 (비트 연산)
        encrypted_ascii = char_ascii ^ key_ascii

        # 결과를 16진수로 변환 (2자리로 맞춤)
        hex_value = format(encrypted_ascii, '02X')
        encrypted_hex += hex_value

        # 암호화된 문자 (출력용)
        encrypted_char = chr(encrypted_ascii)
        encrypted += encrypted_char

        print(
            f"{char}({char_ascii:3d}, {bin(char_ascii):>8s}) XOR {key}({key_ascii:3d}, {bin(key_ascii):>8s}) = {encrypted_ascii:3d} ({bin(encrypted_ascii):>8s}) → {hex_value}")

    print(f"\n암호화된 결과 (16진수): {encrypted_hex}")