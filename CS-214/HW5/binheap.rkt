#lang dssl2

let eight_principles = ["Know your rights.",
    "Acknowledge your sources.",
    "Protect your work.",
    "Avoid suspicion.",
    "Do your own work.",
    "Never falsify a record or permit another person to do so.",
    "Never fabricate data, citations, or experimental results.",
    "Always tell the truth when discussing your work with your instructor."]

# HW5: Binary Heap

interface PRIORITY_QUEUE[X]:
    # Returns the number of elements in the priority queue.
    def len(self) -> nat?
    # Returns the smallest element; error if empty.
    def find_min(self) -> X
    # Removes the smallest element; error if empty.
    def remove_min(self) -> NoneC
    # Inserts an element; error if full.
    def insert(self, element: X) -> NoneC

# Class implementing the PRIORITY_QUEUE ADT as a binary heap.
class BinHeap[X] (PRIORITY_QUEUE):
    let _data: VecC[OrC(X, NoneC)]
    let _size: nat?
    let _lt?:  FunC[X, X, bool?]

    # Constructs a new binary heap with the given capacity and
    # less-than function for type X.
    def __init__(self, capacity, lt?):
        self._size = 0
        self._lt? = lt?
        self._data = [None; capacity]

    def _switch(self, x, y) -> NoneC:
        let temp = self._data[x]
        self._data[x] = self._data[y]
        self._data[y] = temp

    def _sift_up(self, i) -> NoneC:
        while i > 0:
            let parent = (i - 1) // 2
            if self._lt?(self._data[i], self._data[parent]):
                self._switch(i, parent)
                i = parent
            else: break

    def _sift_down(self, i) -> NoneC:
        while True:
            let left = 2*i + 1
            let right = 2*i + 2
            if left >= self._size: break
            let smallest = left
            if right < self._size and self._lt?(self._data[right], self._data[left]):
                smallest = right
            if self._lt?(self._data[smallest], self._data[i]):
                self._switch(i, smallest)
                i = smallest
            else: break

    def len(self)->nat?:
        return self._size
    
    def find_min(self) -> X:
        if self._size == 0: error("heap is empty")
        return self._data[0]

    def remove_min(self) -> NoneC:
        if self._size == 0: error("heap is empty")
        self._data[0] = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size = self._size - 1
        self._sift_down(0)
    
    def insert(self, element: X) -> NoneC:
        if self._size == len(self._data): error("heap is full")
        self._data[self._size] = element
        let i = self._size
        self._size = self._size + 1
        self._sift_up(i)

    def get_vector(self) -> VecC[OrC(X, NoneC)]:
        return self._data

# Other methods you may need can go here.


# Woefully insufficient test.
test 'insert, insert, remove_min':
    # The `nat?` here means our elements are restricted to `nat?`s.
    let h = BinHeap[nat?](10, λ x, y: x < y)
    h.insert(1)
    assert h.find_min() == 1

# Sorts a vector of Xs, given a less-than function for Xs.
#
# This function performs a heap sort by inserting all of the
# elements of v into a fresh heap, then removing them in
# order and placing them back in v.
def heap_sort[X](v: VecC[X], lt?: FunC[X, X, bool?]) -> NoneC:
    let h = BinHeap[X](len(v), lt?)
    for i in range(len(v)):
        h.insert(v[i])
    for i in range(len(v)):
        v[i] = h.find_min()
        h.remove_min()

test 'heap sort descending':
    let v = [3, 6, 0, 2, 1]
    heap_sort(v, λ x, y: x > y)
    assert v == [6, 3, 2, 1, 0]

test 'heap sort ascending':
    let v = [3, 6, 0, 2, 1]
    heap_sort(v, λ x, y: x < y)
    assert v == [0, 1, 2, 3, 6]

test 'heap sort duplicates':
    let v = [3, 1, 2, 1, 3]
    heap_sort(v, λ x, y: x < y)
    assert v == [1, 1, 2, 3, 3]


# Sorting colleges

struct college:
    let name: str?
    # Where is the college located? Can be "rural", "urban" or "suburban".
    let environment: str?
    # Average salary of graduates five years after graduation.
    let salary: int?
    # Average yearly tuition.
    let tuition: int?
    # Average SAT score of last incoming freshling class: between 400 and 1600.
    let sat: int?
    # Average GPA of last incoming freshling class: between 0.0 and 4.0.
    let gpa: num?
    # Number of full-time students attending the school as of last fall.
    let students: int?
    # Student-to-faculty ratio. E.g., 7000 students and 1000 faculty => 7
    let stf_ratio: num?
    # Acceptance rate. 0.0 = accepts no one. 1.0 = accepts everyone.
    let acceptance: num?

let sample_colleges = \
  [college("Montgomery College", "urban", 70000, 30000, 1500, 3.8, 4000, 8, 0.22),
   college("Vanderwaal University", "rural", 100000, 70000, 1550, 4.0, 1000, 2, 0.01),
   college("Manzikert University", "suburban", 70000, 50000, 1530, 3.9, 8500, 6, 0.07),
   college("Melvin College", "suburban", 38000, 6000, 1410, 3.9, 1500, 9, 0.39),
   college("Woods University","rural", 54000, 10000, 1360, 3.6, 500, 13, 0.53),
   college("Dilaurentis University", "rural", 58000, 40000, 1400, 3.7, 5000, 8, 0.44)
   ]

# Is `a` a better college than `b`?
# You decide what makes a college better than another, and you can use any
# or all of the information you have about each college to determine that.
def is_better?(a: college?, b: college?) -> bool?:
    if a.name == "Northwestern University":
        return True
    elif b.name == "Northwestern University":
        return False
    else:
        return (a.salary - a.tuition) > (b.salary - b.tuition)
#   ^ WRITE CODE HERE

# Rank the sample colleges above, in order from "best" to "worst".
def rank_colleges() -> VecC[college?]:
    heap_sort(sample_colleges, is_better?)
    return sample_colleges


test 'length':
    let h = BinHeap[nat?](10, λ x, y: x < y)
    assert h.len() == 0
    h.insert(1)
    assert h.len() == 1
    h.insert(2)
    assert h.find_min() == 1
    assert h.len() == 2
    h.remove_min()
    assert h.len() == 1
    h.remove_min()
    assert h.len() == 0

test 'find_min':
    let h = BinHeap[nat?](10, λ x, y: x < y)
    h.insert(3)
    assert h.find_min() == 3
    h.insert(1)
    assert h.find_min() == 1
    h.insert(2)
    assert h.find_min() == 1
    h.remove_min()
    assert h.find_min() == 2
    h.remove_min()
    assert h.find_min() == 3  

test 'remove_min':
    let h = BinHeap[nat?](10, λ x, y: x < y)
    h.insert(3)
    h.insert(1)
    h.insert(2)
    h.remove_min()
    assert h.find_min() == 2
    h.remove_min()
    assert h.find_min() == 3
    h.remove_min()
    assert h.len() == 0

test 'insert':
    let h = BinHeap[nat?](10, λ x, y: x < y)
    h.insert(3)
    assert h.find_min() == 3
    h.insert(1)
    assert h.find_min() == 1
    h.insert(2)
    assert h.find_min() == 1

test 'weird comparator':
    def weird_lt?(x: str?, y: str?) -> bool?:
        return len(x) < len(y)
    let h = BinHeap[str?](10, weird_lt?)
    h.insert("hello")
    assert h.find_min() == "hello"
    h.insert("hi")
    assert h.find_min() == "hi"
    h.insert("a")
    assert h.find_min() == "a"

test 'error messages':
    let h = BinHeap[nat?](2, λ x, y: x < y)
    assert_error h.find_min(), "heap is empty"
    assert_error h.remove_min(), "heap is empty"
    h.insert(1)
    h.insert(2)
    assert_error h.insert(3), "heap is full"

test 'get_vector':
    let h = BinHeap[nat?](5, λ x, y: x < y)
    assert h.get_vector() == [None, None, None, None, None]
    h.insert(3)
    assert h.get_vector() == [3, None, None, None, None]
    h.insert(1)
    assert h.get_vector() == [1, 3, None, None, None]
    h.insert(2)
    assert h.get_vector() == [1, 3, 2, None, None]

test 'duplicates':
    let h = BinHeap[nat?](10, λ x, y: x < y)
    h.insert(2)
    h.insert(1)
    h.insert(2)
    h.insert(3)
    assert h.find_min() == 1
    h.remove_min()
    assert h.find_min() == 2
    h.remove_min()
    assert h.find_min() == 2