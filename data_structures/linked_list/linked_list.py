#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

import random


class ListNode(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

        self.tail = self.head
        if self.tail:
            while self.tail.next:
                self.tail = self.tail.next

    def add(self, value):
        self.tail.next = ListNode(value)

    def __str__(self):
        list_items = []

        curr_node = self.head
        while curr_node:
            list_items.append(str(curr_node.value))
            curr_node = curr_node.next

        return ' -> '.join(list_items)


def generate_list_with_random_data(length, with_loop=False):
    n = random.randint(0, 1000)
    _l = LinkedList(head=ListNode(n))
    curr_elem = _l.head

    for _ in xrange(length - 1):
        n = random.randint(0, 100)
        curr_elem.next = ListNode(n)
        curr_elem = curr_elem.next

    # if with_loop:
    #     k = random.randint(0, length - 1)
    #     tmp = _l.head
    #     for _ in xrange(k):
    #         tmp =

    return _l


def main():
    length = 5
    # l = generate_list_with_random_data(length)

    # l.print_list()
    #
    # print is_poly(l.head)
    # print k_last_elem(l, 5).value

    # print has_loop(l)
    #
    # curr_elem = l.head
    # loop_start = 3
    # i = 1
    # while curr_elem:
    #     if i == loop_start:
    #         tmp = curr_elem
    #     else:
    #         i += 1
    #     curr_elem = curr_elem.next
    # curr_elem = tmp
    #
    a = ListNode(3)
    b = ListNode(2, next_node=a)
    c = ListNode(7, next_node=b)
    d = ListNode(2, next_node=c)
    e = ListNode(3, next_node=d)
    ll = LinkedList(head=e)

    print ll




    # l.print_list()


if __name__ == '__main__':
    main()
