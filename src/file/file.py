import os


# os.walk(): 更推荐
def walkDir(path) -> list:
    # if not os.path.isdir(path):
    #     print('FileNotFoundError:', path, 'is not a directory or does not exist.')
    #     return

    ans = []
    for root, dirs, files in os.walk(path):
        # for d in dirs:
        #     # print(os.path.join(root, d))
        #     # ans.append(os.path.join(root, d))
        #     pass
        for f in files:
            # print(os.path.join(root, f))
            ans.append(os.path.join(root, f))

    return ans


# os.listdir() 递归
def listDir(path):
    for f in os.listdir(path):
        fp = os.path.join(path, f)
        print(fp)     # dirs
        if os.path.isdir(fp):
            listDir(fp)


if __name__ == '__main__':
    pass
    print(walkDir("./"))
    # listDir("./")

