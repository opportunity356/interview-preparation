#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random


def qsort(a):
    n = len(a)
    quick_sort(a, 0, n - 1)


def quick_sort(a, left, right):
    q = partition(a, left, right)
    if left < q - 1:
        quick_sort(a, left, q - 1)
    if q < right:
        quick_sort(a, q, right)


def partition(a, left, right):
    pivot = a[(left + right) // 2]

    i = left
    j = right

    while i <= j:
        while a[i] < pivot:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

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
