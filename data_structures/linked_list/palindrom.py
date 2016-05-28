#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

from linked_list import LinkedList, ListNode


def is_palindrom(l):
    p1 = p2 = l.head
    stack = []
    even = True
    while True:

        stack.append(p1.value)
        if not p2.next:
            even = False
            break
        if not p2.next.next:
            break

        p1 = p1.next
        p2 = p2.next.next

    if not even:
        stack.pop()

    while p1.next:
        p1 = p1.next
        if p1.value != stack.pop():
            return False

    return True


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2, next_node=a)
    c = ListNode(7, next_node=b)
    d = ListNode(2, next_node=c)
    e = ListNode(3, next_node=d)
    ll = LinkedList(head=e)

    print ll

    print is_palindrom(ll)