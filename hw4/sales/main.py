with open('input.txt', "r") as f:
    db = {}
    for line in f.read().splitlines():
        name, product, amount = line.split()
        new_log = {product: int(amount)}
        if name in db:
            if product in db[name]:
                db[name][product] += int(amount)
            else:
                db[name][product] = int(amount)
        else:
            db[name] = new_log
    for name, log in sorted(db.items()):
        print(f"{name}:")
        for product, amount in sorted(log.items()):
            print(f"{product} {amount}")
