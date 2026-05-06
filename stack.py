#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: stack.py
Author: James Sathre
Date: 2026-05-06
Version: 1.0.0
Description: This script is an example stack implementation
"""

import unittest

class Stack:

    def __init__(self):
        self.data = []

    def push(self, input):
        """pushes the input parameter on the stack at the top"""
        self.data.insert(0, input)

    def pop(self):
        """pops the top parameter off the stack"""
        return self.data.pop(0)

    def top(self):
        """returns the top parameter off the stack"""
        return self.data[0]

    def get_stack_contents(self):
        """returns a list representing the stack's data"""
        return self.data

    def empty(self):
        """empty's all data contained in the stack"""
        self.data.clear()

    def size(self):
        """returns the number of elements in the stack"""
        return len(self.data)

class TestStackMethods(unittest.TestCase):

    def test_push(self):
        stack_obj = Stack()
        stack_obj.push(1)
        stack_obj.push(2)
        stack_obj.push(3)
        self.assertEqual(stack_obj.get_stack_contents(), [3,2,1])        

    def test_pop(self):
        stack_obj = Stack()
        stack_obj.push(1)
        stack_obj.push(2)
        stack_obj.push(3)
        stack_obj.pop()
        self.assertEqual(stack_obj.get_stack_contents(), [2,1])

    def test_top(self):
        stack_obj = Stack()
        stack_obj.push(1)
        self.assertEqual(stack_obj.top(), 1)
        self.assertTrue(len(stack_obj.get_stack_contents()) == 1)

    def test_empty(self):
        stack_obj = Stack()
        stack_obj.push(1)
        stack_obj.push(2)
        stack_obj.push(3)
        stack_obj.empty()
        self.assertTrue(len(stack_obj.get_stack_contents()) == 0)

    def test_size(self):
        stack_obj = Stack()
        stack_obj.push(1)
        stack_obj.push(2)
        stack_obj.push(3)
        self.assertTrue(stack_obj.size() == 3)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()