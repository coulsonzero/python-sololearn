class Queue:
    def __init__(self, contents):
        # private
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


if __name__ == '__main__':
    queue = Queue([1, 2, 3])    # Queue([1, 2, 3])
    print(queue)

    queue.push(0)               # Queue([0, 1, 2, 3])
    print(queue)

    queue.pop()                 # Queue([0, 1, 2])
    print(queue)

    print(queue._hiddenlist)    # [0, 1, 2]


