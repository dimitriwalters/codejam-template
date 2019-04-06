#!/bin/python3

def sol(t, n, l, L):
    print('Case #%d: %s' % (t, 'a'))
    return

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, l = map(int, input().split())
        inputs = input().split()
        L = []
        for j in range(l):
            L.append(int(inputs[j]))

        sol(i + 1, n, l, L)
