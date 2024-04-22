def normalize_phone_number(phone_number):
    phone_number = phone_number.replace("-", "").replace("(", "").replace(")", "").replace("+", "")
    if len(phone_number) > 7:
        phone_number = phone_number[1:len(phone_number)]
    else:
        phone_number = "495" + phone_number
    return phone_number


def main():
    pn_wanted = input()
    pn_wanted = normalize_phone_number(pn_wanted)
    pn_list = []
    for i in range(3):
        pn_temp = input()
        pn_temp = normalize_phone_number(pn_temp)
        pn_list.append(pn_temp)
    for i in range(3):
        if pn_wanted == pn_list[i]:
            print("YES")
        else:
            print("NO")


main()
