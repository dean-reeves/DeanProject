# func_py_reverse_linked_list.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def func_py_reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev
