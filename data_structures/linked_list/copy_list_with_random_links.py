#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


class ListNode(object):

    def __init__(self, data, random=None, next_node=None):
        self.data = data
        self.random = random
        self.next = next_node


class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def __str__(self):
        d = []
        r = []

        curr = self.head
        while curr:
            d.append(str(curr.data))
            r.append(str(curr.random.data))
            curr = curr.next

        return ' --> '.join(d) + '\n' + '  |  '.join(r)


def copy_list(l):
    head = l.head
    if not head:
        return

    curr = head
    while curr:
        new = ListNode(
            curr.data,
            curr.random,
            curr.next
        )
        curr.next = new
        curr = new.next

    curr = head
    while curr:
        new = curr.next
        new.random = new.random.next
        curr = new.next

    curr = head
    new_head = head.next
    while curr:
        new = curr.next
        curr = new.next
        if new.next:
            new.next = new.next.next

    new_l = LinkedList(new_head)
    return new_l


if __name__ == '__main__':

    e = ListNode(5)
    d = ListNode(4, next_node=e)
    c = ListNode(3, next_node=d)
    b = ListNode(2, next_node=c)
    a = ListNode(1, next_node=b)

    a.random = c
    b.random = e
    c.random = b
    d.random = d
    e.random = a

    l = LinkedList(a)

    print l

    new_l = copy_list(l)
    print new_l
    print new_l is l


    curr = l.head
