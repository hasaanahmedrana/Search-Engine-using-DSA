class Hashtable:
    '''Hashtable class to store key value pairs in a hash table.'''
    def __init__(self, size=255) -> None:
        '''Initialize a new Hashtable with a given size. Default size is 255.'''
        self.size = size
        self.table = [None] * self.size

    def hashing(self, name):
        '''Generate a hash for a given name.'''
        h = 0
        for each in name:
            h += ord(each)
        return h % self.size

    def insert(self, name):
        '''Insert a node into the hash table.'''
        h = self.hashing(name)
        if self.table[h] is None:
            self.table[h] = name
            return True
        else:
            new = h + 1
            while True:
                if new == h: return False
                if new == self.size: new = 0
                if self.table[new] is None:
                    self.table[new] = name
                    return True
                new += 1

    def search(self, name):
        '''search for a query in the hash table.'''
        h = self.hashing(name)
        if self.table[h] is None: return False
        if self.table[h] == name: return True
        temp = h + 1
        while True:
            if temp == self.size: temp = 0
            if temp == h: return False
            if self.table[temp] == name:
                return True
            temp += 1

    def remove(self, name):
        ''' Remove the query name from the hash table.'''
        h = self.hashing(name)
        if self.table[h] is None: return False
        if self.table[h] == name:
            self.table[h] = None
            return True
        temp = h + 1
        while True:
            if temp == h: return False
            if temp == self.size: temp = 0
            if self.table[temp] == name:
                self.table[temp] = None
                return True

    def display(self):
        '''Display the hash table.'''
        lst = []
        for each in self.table:
            if each is not None:
                lst.append(each)
            else:
                lst.append('Empty')
        return lst

    def loadfactor(self):
        '''Calculate and return the load factor of the hash table.'''
        count = 0
        for i in self.table:
            if i is not None:
                count += 1
        return count/self.size

    def none_count(self):
        '''Count and return the number of None values in the hash table.'''
        count = 0
        for each in self.table:
            if each is None:
                count += 1
        return count

    def is_empty(self):
        '''Check if the hash table is empty.'''
        return self.none_count() == self.size - 1

    def is_full(self):
        ''' Check if the hash table is full.'''
        return self.none_count() == 0

    def __iter__(self):
        '''Return an iterator for the hash table.'''
        return iter(self.table)

    def __len__(self):
        '''Return the size of the hash table.'''
        return len(self.table)



if __name__ == '__main__':
    size = int(input('Enter the size of the Hashtable:'))
    table = Hashtable(size)
    choices =['Insert a Name.', 'Search for a name.','Remove a name.', 'Display the hashtable', 'Display a load Factor.', 'Exit' ]
    for idx, elem in enumerate(choices):
        print(f'{idx+1:} {elem}')
    while True:
        selected = int(input('Enter Your choice:'))
        if selected == 6: break
        if selected in (1, 2, 3):
            name = input('Enter name:')
            if selected == 1:
                print(table.insert(name))
            elif selected == 2:
                print(table.search(name))
            else:
                print(table.remove(name))

        if selected == 4:
            print(table.display())
        if selected == 5:
            print(table.loadfactor())






