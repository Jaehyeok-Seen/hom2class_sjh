# format 문자열 예시
a = 10
print("=== 기본 format 사용법 ===")
print(f"a = {a}")

# 2진수 변환
b = f'{a:b}'      # 기본 2진수
print(f"기본 2진수: {b}")

b = f'{a:010b}'   # 10자리 2진수 (앞에 0 채움)
print(f"10자리 2진수: {b}")

b = f'{a:08b}'    # 8자리 2진수 (앞에 0 채움)
print(f"8자리 2진수: {b}")

# 16진수 변환
c = f'{a:08x}'    # 8자리 16진수 (소문자)
print(f"8자리 16진수(소문자): {c}")

c = f'{a:08X}'    # 8자리 16진수 (대문자)
print(f"8자리 16진수(대문자): {c}")

print("\n" + "="*50)
print("=== format 문자열 문법 설명 ===")
print("{숫자:0자릿수진법}")
print("  0: 앞에 0으로 채우기")
print("  자릿수: 총 자릿수")
print("  진법: b(2진수), o(8진수), d(10진수), x(16진수)")

print("\n" + "="*50)
print("=== 다양한 숫자로 테스트 ===")

test_numbers = [5, 15, 255, 1023]
for num in test_numbers:
    print(f"\n숫자: {num}")
    print(f"  2진수 기본: {num:b}")
    print(f"  2진수 8자리: {num:08b}")
    print(f"  16진수 기본: {num:x}")
    print(f"  16진수 4자리: {num:04x}")
    print(f"  16진수 대문자: {num:04X}")

print("\n" + "="*50)
print("=== 16진수 → 2진수 변환 (format 사용) ===")

def hex_to_binary_format_simple(hex_str):
    """format 문자열을 사용한 16진수 → 2진수 변환"""
    decimal = int(hex_str, 16)
    target_length = len(hex_str) * 4  # 16진수 1자리 = 2진수 4자리
    return f'{decimal:0{target_length}b}'

# 테스트
test_hex_values = ["A", "01", "FF", "1A2B", "01D06079861D79F99F"]

for hex_val in test_hex_values:
    binary_result = hex_to_binary_format_simple(hex_val)
    print(f"{hex_val} -> {binary_result} (길이: {len(binary_result)})")

print("\n" + "="*50)
print("=== zfill vs format 비교 ===")

num = 42
print("zfill 방식:")
binary_zfill = bin(num)[2:].zfill(8)
print(f"  bin({num})[2:].zfill(8) = {binary_zfill}")

print("format 방식:")
binary_format = f'{num:08b}'
print(f"  f'{{num:08b}}' = {binary_format}")

print(f"결과 같음: {binary_zfill == binary_format}")

print("\n✅ format 문자열이 더 간단하고 직관적!")
print("✅ 한 줄로 깔끔하게 처리 가능!")