def init():
    # d = dict()
    # d = {}

    d = {
        'name': 'john',
        'age': 23,
        'email': 'john@163.com'
    }



def method():
    d = {
        'name': 'john',
        'age': 23,
        'email': 'john@163.com'
    }

    print(type(d))                # <class 'dict'>
    print(isinstance(d, dict))    # True

    print(d['age'])
    # print(d['sex'])     # KeyError: 'sex'
    print(d.get('sex'))   # None
    print(d.get('sex', "not found"))   # "not found"


    '''删除'''
    # d.pop("age")
    # del d['age']
    # d.clear()
def get():
    d = {'name': 'john', 'age': 23, 'email': 'john@163.com'}
    d.update({'sex': 'male'})

    print(d.keys())
    print(d.values())
    print(d.items())



if __name__ == '__main__':
    # init()
    # method()
    get()
    pass

