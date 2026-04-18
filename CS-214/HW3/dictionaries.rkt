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

    def _find(self, key: K):
        let item = self._head
        while item:
            if item.key == key:
                return item
            item = item.next
        return None

    def len(self) -> int?:
        return self._len

    def mem?(self, key: K) -> bool?:
        return self._find(key) != None

    def get(self, key: K) -> V:
        let node = self._find(key)
        if node == None:
            error("key not found")
        return node.data
    
    def put(self, key: K, val: V) -> NoneC:
        let node = self._find(key)
        if node != None:
            node.data = val
            return
        self._head = _node(key, val, self._head)
        self._len = self._len + 1

    def del(self, key: K) -> NoneC:
        let item = self._head
        let prev = None
        while item:
            if item.key == key:
                if prev == None:
                    self._head = item.next
                else:
                    prev.next = item.next
                self._len = self._len - 1
                return
            prev = item
            item = item.next
        error("cant delete an empty list")


test 'I DONT need more tests':
    let a = AssociationList()
    assert not a.mem?('hello')
    a.put('hello', 5)
    assert a.len() == 1
    assert a.mem?('hello')
    assert a.get('hello') == 5

test "testing bounds":
    let a = AssociationList()
    assert a.len() == 0
    assert_error a.del("nothing"), "cant delete an empty list"
    assert a.len() == 0
    a.put("key", "val")
    assert a.len() == 1
    a.del("key")
    assert a.len() == 0
    a.put("key", "val")
    a.put("key", "val_replace")
    assert a.len() == 1
    assert a.get("key") == "val_replace"

test "get error":
    let a = AssociationList()
    assert_error a.get("nuthin"), "key not found"
    a.put("x", 1)
    assert_error a.get("nuthin"), "key not found"

test "mem? after del":
    let a = AssociationList()
    a.put("a", 1)
    assert a.mem?("a")
    a.del("a")
    assert not a.mem?("a")
    assert a.len() == 0

test "lots o' keys":
    let a = AssociationList()
    a.put("a", 1)
    a.put("b", 2)
    a.put("c", 3)
    assert a.len() == 3
    assert a.mem?("a")
    assert a.mem?("b")
    assert a.mem?("c")
    assert a.get("a") == 1
    assert a.get("b") == 2
    assert a.get("c") == 3

test "del middle and del the whole thing":
    let a = AssociationList()
    a.put("a", 1)
    a.put("b", 2)
    a.put("c", 3)
    a.del("b")
    assert a.len() == 2
    assert not a.mem?("b")
    assert a.mem?("a")
    assert a.mem?("c")
    a.del("a")
    assert a.len() == 1
    assert not a.mem?("a")
    assert a.mem?("c")

test "put replace keeps last key":
    let a = AssociationList()
    a.put("a", 1)
    a.put("b", 2)
    a.put("a", 99)
    assert a.len() == 2
    assert a.get("a") == 99
    assert a.get("b") == 2


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