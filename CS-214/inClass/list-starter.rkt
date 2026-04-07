#lang dssl2

# a Link is one of:
# - cons { data: Any, next: Link }
# - None
struct cons:
    let data
    let next

class SLL:
    let head
    let length

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_front(self, data):
        self.head = cons(data, self.head)
        self.length = self.length + 1

    def get_first(self):
        if cons?(self.head): return self.head.data
        else: error('first of an empty list')

    def _find_nth_node(self, n):    # leading _ → private method
        let curr = self.head
        while not curr == None:
            if n == 0:
                return curr
            n    = n - 1
            curr = curr.next
        error('list too short')

    def get_nth(self, n):
        return self._find_nth_node(n).data

    def set_nth(self, n, val):
        self._find_nth_node(n).data = val

    def get_last(self):
        if self.length != 0: self._find_nth_node(self.length-1).data
        else: error("last of an empty list")


test 'get_first':
    let lst = SLL()
    assert_error lst.get_first(), 'first of an empty list'
    lst.insert_front(4)
    assert lst.get_first() == 4
    lst.insert_front(3)
    assert lst.get_first() == 3

test 'get_nth':
    let lst = SLL()
    lst.insert_front(4)
    lst.insert_front(3)
    lst.insert_front(2)
    assert lst.get_nth(0) == 2
    assert lst.get_nth(1) == 3
    assert_error lst.get_nth(5), 'list too short'
    assert_error SLL().get_nth(0), 'list too short'

test 'get_last':
    let lst = SLL()
    assert_error lst.get_last(), 'last of an empty list'
    lst.insert_front(4)
    lst.insert_front(3)
    lst.insert_front(2)
    assert lst.get_last() == 4
