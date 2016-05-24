#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def has_loop(l):
    turtle = rabbit = l.head

    res = False
    while rabbit and rabbit.next:

        turtle = turtle.next
        rabbit = rabbit.next.next

        print turtle.value, rabbit.value

        if turtle == rabbit:
            res = True
            break

    return res