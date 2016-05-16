#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

import random


class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        curr_elem = self.head

        while curr_elem:
            print curr_elem.data
            curr_elem = curr_elem.next


def generate_list_with_random_data(length):
    n = random.randint(0, 1000)
    _l = LinkedList(head=Node(n))
    curr_elem = _l.head

    for _ in xrange(length - 1):
        n = random.randint(0, 100)
        curr_elem.next = Node(n)
        curr_elem = curr_elem.next

    return _l


def main():
    l = generate_list_with_random_data(10)

    l.print_list()


if __name__ == '__main__':
    main()
