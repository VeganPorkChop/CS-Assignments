#lang dssl2

# HW2: Stacks and Queues

let eight_principles = ["Know your rights.",
"Acknowledge your sources.",
"Protect your work.",
"Avoid suspicion.",
"Do your own work.",
"Never falsify a record or permit another person to do so.",
"Never fabricate data, citations, or experimental results.",
"Always tell the truth when discussing your work with your instructor."]

import ring_buffer

interface STACK[T]:
    def push(self, element: T) -> NoneC
    def pop(self) -> T
    def empty?(self) -> bool?

# Defined in the `ring_buffer` library; copied here for reference.
# Do not uncomment! or you'll get errors.
# interface QUEUE[T]:
#     def enqueue(self, element: T) -> NoneC
#     def dequeue(self) -> T
#     def empty?(self) -> bool?

# Linked-list node struct (implementation detail):
struct _cons:
    let data
    let next: OrC(_cons?, NoneC)

###
### ListStack
###

class ListStack[T] (STACK):

    # Any fields you may need can go here.
    let header: OrC(_cons?, NoneC)

    # Constructs an empty ListStack
    def __init__ (self):
        self.header = None
    #   ^ WRITE CODE HERE
    def push(self, element: T) -> NoneC:
        self.header = _cons(element, self.header)
    # Other methods you may need can go here.
    def pop(self) -> T:
        if self.header == None:
            error("empty stack")
        let return_val = self.header.data
        self.header = self.header.next
        return return_val

    def empty?(self) -> bool?:
        return self.header == None

test "ListStack Tests basic functionality":
    let s = ListStack()
    assert s.empty?() == True
    s.push(2)
    assert s.empty?() == False
    assert s.pop() == 2
    assert s.empty?() == True
test "ListStack Tests errors":
    let s = ListStack()
    assert_error s.pop(), "empty stack"
test "ListStack Tests niche cases":
    let s = ListStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    assert s.empty?() == False
    assert [s.pop(), s.pop(), s.pop(), s.pop()] == [4, 3, 2, 1]
    assert s.empty?() == True
    assert_error s.pop(), "empty stack"

###
### ListQueue
###

class ListQueue[T] (QUEUE):

    # Any fields you may need can go here.
    let header: OrC(_cons?, NoneC)
    let tail: OrC(_cons?, NoneC)
    let length: int?
    # Constructs an empty ListQueue.
    def __init__ (self):
        self.header = None
        self.tail = None
        self.length = 0
    #   ^ WRITE CODE HERE
    def enqueue(self, element: T) -> NoneC:
        let new_el = _cons(element, None)
        if self.length != 0:
            self.tail.next = new_el
        else:
            self.header = new_el
        self.tail = new_el
        self.length = self.length + 1
    def dequeue(self) -> T:
        if self.length == 0:
            error("empty queue")
        let return_val = self.header
        self.header = self.header.next
        self.length = self.length - 1
        if self.length == 0:
            self.tail = None
        return return_val.data

    def empty?(self) -> bool?:
        return self.length == 0
    # Other methods you may need can go here.

test "ListQueue basic func":
    let s = ListQueue()
    assert s.empty?() == True
    s.enqueue(2)
    assert s.empty?() == False
    assert s.dequeue() == 2
    assert s.empty?() == True
test "ListQueue errors":
    let s = ListQueue()
    assert_error s.dequeue(), "empty queue"
test "ListQueue niche cases":
    let s = ListQueue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    assert s.empty?() == False
    assert [s.dequeue(), s.dequeue(), s.dequeue(), s.dequeue()] == [1, 2, 3, 4]
    assert s.empty?() == True
    assert_error s.dequeue(), "empty queue"

###
### Playlists
###

struct song:
    let title: str?
    let artist: str?
    let album: str?

# Enqueue five songs of your choice to the given queue, then return the first
# song that should play.
def fill_playlist (q: QUEUE!):
    if not q.empty?():
        error("non-empty queue")
    let lst =   [song("Binary Sunset","The Data Structures","Array of Hope"),
                song("Linked List Blues", "Pointer Sisters", "Memory Management"),
                song("Stack Overflow", "Recursion", "Void Return"),
                song("Hash Function", "Collision", "The Mapping"),
                song("QuickSort Shuffle", "Divide & Conquer", "Efficiency")]
    for s in lst:
        q.enqueue(s)
    return q.dequeue()

test "ListQueue playlist":
    let song_queue = ListQueue()
    assert fill_playlist(song_queue) == song("Binary Sunset", "The Data Structures", "Array of Hope")
    song_queue.enqueue(song("THIS", "SONG", "SUCKS"))
    assert_error fill_playlist(song_queue), "non-empty queue"

# To construct a RingBuffer: RingBuffer(capacity)
test "RingBuffer playlist":
    let song_queue = RingBuffer(5)
    assert fill_playlist(song_queue) == song("Binary Sunset", "The Data Structures", "Array of Hope")
    song_queue.enqueue(song("THIS", "IS THE LAST", "SONG IN THE QUEUE"))
    assert_error song_queue.enqueue(song("AHH", "TOOO", "MANYYYYY")), "full"



