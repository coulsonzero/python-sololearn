def demo():
    d = {}
    s = "leetcode"
    for i in s:
        d[i] = d.get(i, 0) + 1
    print(d)

def demo2():
    d = {}
    s = "leetcode"
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)

def dict_update():
    d = {
        "name": "john",
        "country": "USA",
        "sex": "0"
    }
    # d.update({"sex": "1"})
    d["sex"] = 1
    print(d)

if __name__ == '__main__':
    dict_update()