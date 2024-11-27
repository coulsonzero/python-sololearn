

num : int     = 7
pi  : float   = 3.14
c   : complex = 1 + 2j

flag: bool  = True
name: str   = "John Smith"

nums: list  = [1, 2, 3]
tup : tuple = ('a', "bc", 123)
d   : dict  = {"name": "John Smith", "age": 27, "sex": 1}
s   : set   = {1, 3, "ab"}


print(type(num))    # <class 'int'>
print(type(nums))   # <class 'list'>
print(type(num) == int)          # True
print(isinstance(num, int))      # True
