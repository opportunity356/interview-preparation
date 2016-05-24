#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def is_palindrom(l):
    p1 = p2 = l
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

        print stack

        if not even:
            stack.pop()

    while p1.next:
        p1 = p1.next
        if p1.value != stack.pop():
            return False

    return True