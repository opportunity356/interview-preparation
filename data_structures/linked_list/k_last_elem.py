#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def k_last_elem(l, k):
    """
    Function returns k-th last element of a list. 1-st last element is simply last element.
    :param l:
    :param k:
    :return:
    """
    k_last = curr = l.head
    i = 1

    while curr.next:
        if i >= k:
            k_last = k_last.next
        else:
            i += 1
        curr = curr.next

    return k_last