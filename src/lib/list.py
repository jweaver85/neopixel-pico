class queue:
    def __init__(self, iterable, maximum):
        if iterable == None:
            self.l = []
        else:
            self.l = list(iterable)
            
    def push(self, item):
        self.l.insert(0,item)
        
    def pop(self):
        self.l.pop()
        
    def extend(self, a):
        self.q.extend(a)

    def __len__(self):
        return len(self.q)

    def __bool__(self):
        return bool(self.q)

    def __iter__(self):
        yield from self.q

    def __str__(self):
        return 'deque({})'.format(self.q)