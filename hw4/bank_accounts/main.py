with open('input.txt', 'r') as f:
    db = {}
    for line in f.read().splitlines():
        details = list(line.split())
        operation = details[0]
        match operation:
            case 'DEPOSIT':
                name, amount = details[1], int(details[2])
                if name in db:
                    db[name] += amount
                else:
                    new_account = 0
                    db[name] = new_account
                    db[name] += amount

            case 'WITHDRAW':
                name, amount = details[1], int(details[2])
                if name in db:
                    db[name] -= amount
                else:
                    new_account = 0
                    db[name] = new_account
                    db[name] -= amount

            case 'BALANCE':
                name = details[1]
                if name in db:
                    print(db[name])
                else:
                    print("ERROR")

            case 'TRANSFER':
                name_from, name_to, amount = details[1], details[2], int(details[3])
                if name_from in db:
                    if name_to in db:
                        db[name_from] -= amount
                        db[name_to] += amount
                    else:
                        new_account = 0
                        db[name_to] = new_account
                        db[name_from] -= amount
                        db[name_to] += amount
                else:
                    new_account = 0
                    db[name_from] = new_account
                    if name_to in db:
                        db[name_from] -= amount
                        db[name_to] += amount
                    else:
                        new_account = 0
                        db[name_to] = new_account
                        db[name_from] -= amount
                        db[name_to] += amount

            case 'INCOME':
                percent = int(details[1])
                for name, account_val in db.items():
                    if account_val > 0:
                        db[name] += int(account_val * percent/100)
