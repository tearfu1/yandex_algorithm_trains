def main():
    started = False
    prev = 0
    type = ""
    while True:
        if not started:
            prev = int(input())
            started = True
        else:
            curr = int(input())
            if curr == -2000000000:
                break
            if curr > prev:
                if type == "" or type == "ASCENDING":
                    type = "ASCENDING"
                elif type == "DESCENDING" or type == "WEAKLY DESCENDING":
                    type = "RANDOM"
                elif type == "CONSTANT" or type == "WEAKLY ASCENDING":
                    type = "WEAKLY ASCENDING"
            elif curr == prev:
                if type == "":
                    type = "CONSTANT"
                elif type == "ASCENDING" or type == "WEAKLY ASCENDING":
                    type = "WEAKLY ASCENDING"
                elif type == "DESCENDING" or type == "WEAKLY DESCENDING":
                    type = "WEAKLY DESCENDING"
            else:
                if type == "" or type == "DESCENDING":
                    type = "DESCENDING"
                elif type == "ASCENDING" or type == "WEAKLY ASCENDING":
                    type = "RANDOM"
                elif type == "CONSTANT" or type == "WEAKLY DESCENDING":
                    type = "WEAKLY DESCENDING"
            prev = curr

    print(type)


main()
