#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def insertion_sort(a):
    n = len(a)
    for i in xrange(1, n):
        tmp = a[i]
        j = i - 1
        while j >= 0 and tmp < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
