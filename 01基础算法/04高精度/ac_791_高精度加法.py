import sys

# 【关键解封操作】将字符串转整数的最大位数限制设置为 0 (即无限制)
sys.set_int_max_str_digits(0)

def main() -> None:
    a = int(input())
    b = int(input())
    result = a + b
    print(result)

if __name__ == "__main__":
    main()