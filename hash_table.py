Class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]
        return
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
        return None

ht = HashTable()

ht.add('golf', 'sport')
print(ht.hash('golf'))       # 424
print(ht.lookup('golf'))     # sport

ht.add('dear', 'friend')
ht.add('read', 'book')
print(ht.collection)
# {424: {'golf': 'sport'}, 412: {'dear': 'friend', 'read': 'book'}}

ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')
print(ht.collection[300])
# {'fcc': 'coding', 'cfc': 'chemical'}

ht.remove('fcc')
print(ht.lookup('fcc'))      # None
print(ht.lookup('cfc'))      # chemical
