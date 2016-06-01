#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

from linked_list import ListNode, LinkedList


def reverse_list(l):
    prev = None
    curr = l.head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    l.head = prev
    return l


if __name__ == '__main__':

    e = ListNode(5)
    d = ListNode(4, next_node=e)
    c = ListNode(3, next_node=d)
    b = ListNode(2, next_node=c)
    a = ListNode(1, next_node=b)

    l = LinkedList(a)

    print l

    reverse_list(l)

    print l