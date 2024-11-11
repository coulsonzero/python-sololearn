import os

def demo():
    ans = []
    for f in os.listdir(os.getcwd()):
        if os.path.isfile(f) and f.endswith('.py'):
            ans.append(f)
    print(ans)
    # ['get-filename.py', 'file.py', 'example-file.py', 'read-file.py']


if __name__ == '__main__':

    pass
