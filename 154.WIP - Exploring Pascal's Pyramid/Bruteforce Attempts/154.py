def add_to_dict(dictionary: dict, key, value):
    if key in dictionary.keys():
        dictionary[key] += value
    else:
        dictionary[key] = value


coefs = {(0, 0, 0): 1}

for p in range(1, 200001):
    new_coefs = {}
    for c in coefs.keys():
        add_to_dict(new_coefs, (c[0]+1, c[1], c[2]), coefs[c])
        add_to_dict(new_coefs, (c[0], c[1]+1, c[2]), coefs[c])
        add_to_dict(new_coefs, (c[0], c[1], c[2]+1), coefs[c])
    coefs = new_coefs
    print(p)
