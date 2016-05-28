#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def cycle_shift_right(a, n, k):
    """
    Function shifts array a on k positions right
    :param a: array
    :param n: length of array
    :param k: the value of shift
    :return:
    """
    cnt = 0

    i = start = 0
    curr = a[i]

    while cnt < n:
        j = (i + k) % n

        tmp = a[j]
        a[j] = curr
        curr = tmp

        i = j

        cnt += 1

        if j == start:
            start = (start + 1) % n  # using the modulus of n for situation if k=n
            i = start
            curr = a[i]

    return a


if __name__ == '__main__':
    a = range(1, 13)
    n = len(a)
    k = 12

    print a
    print cycle_shift_right(a, n, k)