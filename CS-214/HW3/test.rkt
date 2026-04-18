#lang dssl2

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
        if not self._head:
            self._head = _node(key, val, None)
        let item = self._head
        while item:
            if item.key == key:
                item.data = val
                break
            item = item.next
        self._len = self._len + 1

    def del(self, key: K) -> NoneC:
        let item = self._head
        let prev = None
        while item:
            item = item.next
            if item.key == key:
                if item.next:
                    prev.next = item.next
                else:
                    prev.next = None
                break
            prev = item
        self._len = self._len -1


test 'yOu nEeD MorE tEsTs':

    let a = AssociationList()
    assert not a.mem?('hello')
    a.put('hello', 5)
    assert a.len() == 1
    print(a)
    assert a.mem?('hello')
    assert a.get('hello') == 5