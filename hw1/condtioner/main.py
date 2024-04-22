def main():
    troom, tcond = map(int, input().split())
    mode = input()
    match mode:
        case "freeze":
            tans = tcond if tcond < troom else troom
            print(tans)
        case "heat":
            tans = tcond if tcond > troom else troom
            print(tans)
        case "auto":
            print(tcond)
        case "fan":
            print(troom)


main()
