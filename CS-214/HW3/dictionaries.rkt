#lang dssl2

# HW3: Dictionaries

import sbox_hash

# A signature for the dictionary ADT. The contract parameters `K` and
# `V` are the key and value types of the dictionary, respectively.
interface DICT[K, V]:
    # Returns the number of key-value pairs in the dictionary.
    def len(self) -> nat?
    # Is the given key mapped by the dictionary?
    # Notation: `key` is the name of the parameter. `K` is its contract.
    def mem?(self, key: K) -> bool?
    # Gets the value associated with the given key; calls `error` if the
    # key is not present.
    def get(self, key: K) -> V
    # Modifies the dictionary to associate the given key and value. If the
    # key already exists, its value is replaced.
    def put(self, key: K, value: V) -> NoneC
    # Modifes the dictionary by deleting the association of the given key.
    def del(self, key: K) -> NoneC
    # The following method allows dictionaries to be printed
    def __print__(self, print)

struct _node:
        let key
        let data
        let next: OrC(_node?, NoneC)

class AssociationList[K, V] (DICT):

    let _head
    let _len

    def __init__(self):
        self._head = None
        self._len = 0
        pass

    def __print__(self, print):
        print("#<object:AssociationList head=%p>", self._head)

    def _looper(self, x:FunC):
        let item = self._head
        while item:
            if item.key == key:
                return True
            item = item.next

    # Other methods you may need can go here.
    def len(self) -> int?:
        return self._len

    def mem?(self, key: K) -> bool?:
        if self._head == None:
            return False
        let item = self._head
        while item:
            if item.key == key:
                return True
            item = item.next
        return False

    def get(self, key: K) -> V:
        if not self.mem?(key):
            error("key not found")
        let item = self._head
        while item:
            if item.key == key:
                return item.data
            item = item.next
    
    def put(self, key: K, val: V) -> NoneC:
        let item = self._head
        while item:
            if item.key == key:
                item.data = val
            item = item.next
        item.next = _node(key, val, None)

    def del(self, key: K) -> NoneC:
        let item = self._head
        let prev = None
        while item:
            item = item.next
            if item.key == key:
                prev.next = item.next
                break
            prev = item
        

test 'yOu nEeD MorE tEsTs':
    let a = AssociationList()
    assert not a.mem?('hello')
    a.put('hello', 5)
    assert a.len() == 1
    assert a.mem?('hello')
    assert a.get('hello') == 5


class HashTable[K, V] (DICT):
    let _hash
    let _size
    let _data

    def __init__(self, nbuckets: nat?, hash: FunC[AnyC, nat?]):
        self._hash = hash
        pass
    #   ^ WRITE CODE HERE

    # This avoids trying to print the hash function, since it's not really
    # printable and isn’t useful to see anyway:
    def __print__(self, print):
        print("#<object:HashTable  _hash=... _size=%p _data=%p>",
              self._size, self._data)

    # Other methods you may need can go here.


# first_char_hasher(String) -> Natural
# A simple and bad hash function that just returns the ASCII code
# of the first character.
# Useful for debugging because it's easily predictable.
def first_char_hasher(s: str?) -> int?:
    if s.len() == 0:
        return 0
    else:
        return int(s[0])

test 'yOu nEeD MorE tEsTs, part 2':
    let h = HashTable(10, make_sbox_hash())
    assert not h.mem?('hello')
    h.put('hello', 5)
    assert h.len() == 1
    assert h.mem?('hello')
    assert h.get('hello') == 5


def compose_phrasebook(d: DICT!) -> DICT?:
    pass
#   ^ WRITE CODE HERE

test "AssociationList phrasebook":
    pass

test "HashTable phrasebook":
    pass