# -*- coding: utf-8 -*-
import unittest

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

def eval_rpn(expression):
    elements = expression.split()
    pile = []
    while elements:
        e = elements.pop(0)
        if e in operators:
            b = pile.pop()
            a = pile.pop()
            pile.append(operators[e](a, b))
        else:
            pile.append(int(e))
    return pile[0]


