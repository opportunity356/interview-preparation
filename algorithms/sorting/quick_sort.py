#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random


def qsort(a):
    n = len(a)
    quick_sort(a, 0, n - 1)


def quick_sort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quick_sort(a, l, q)
        quick_sort(a, q + 1, r)


def partition(a, l, r):
    q = (l + r) // 2
    x = a[q]

    i = l
    j = r

    while i < j:
        while a[i] < x:
            i += 1

        while a[j] > x:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    return i


if __name__ == '__main__':
    l = range(0, 10)

    for i in xrange(10000):
        random.shuffle(l)
        x = l[:]
        # print "shuffled: ", l

        qsort(l)
        a = l[:]
        # print "qsort: ", l

        l.sort()
        b = l[:]
        # print "sort: ", l

        stop = False
        for i, j in zip(a, b):
            if i != j:
                stop = True
                print x
                break

        if stop:
            break