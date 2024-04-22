def is_growing(test_list):
    for i in range(len(test_list) - 1):
        if test_list[i] >= test_list[i + 1]:
            return False
    return True


def main():
    a = map(int, input().split())
    a = list(a)
    if len(a) > 0:
        if is_growing(a):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


main()
