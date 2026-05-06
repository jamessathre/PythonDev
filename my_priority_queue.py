#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: priority_queue.py
Author: James Sathre
Date: 2026-05-06
Version: 1.0.0
Description: This script is an example priority queue implementation
"""

import unittest
from my_queue import MyQueue


class MyPriorityQueue(MyQueue):    
    def __init__(self, sortmax=True):
        super().__init__()
        self.max = sortmax

    def push(self, input):
        super().push(input)
        if self.max:
            self.data.sort(reverse=True)
        else:
            self.data.sort()

class TestPriorityQueueMethods(unittest.TestCase):

    def generate_test_queue(self, sortmax=True):
        q = MyPriorityQueue(sortmax)
        q.push(7)
        q.push(2)
        q.push(5)
        q.push(1)
        return q

    def test_push_max(self):
        q = self.generate_test_queue(True)
        self.assertTrue(q.get_queue_contents() == [7, 5, 2, 1])

    def test_push_min(self):
        q = self.generate_test_queue(False)
        self.assertTrue(q.get_queue_contents() == [1, 2, 5, 7])

    def test_pop_max(self):
        q = self.generate_test_queue(True)
        q.pop()
        self.assertTrue(q.get_queue_contents() == [5, 2, 1])

    def test_pop_min(self):
        q = self.generate_test_queue(False)
        q.pop()
        self.assertTrue(q.get_queue_contents() == [2, 5, 7])

    def test_front_max(self):
        q = self.generate_test_queue(True)
        self.assertTrue(q.front() == 7)

    def test_front_min(self):
        q = self.generate_test_queue(False)
        self.assertTrue(q.front() == 1)

    def test_back_max(self):
        q = self.generate_test_queue(True)
        self.assertTrue(q.back() == 1)

    def test_back_min(self):
        q = self.generate_test_queue(False)
        self.assertTrue(q.back() == 7)

    def test_empty(self):
        q = self.generate_test_queue(False) 
        q.clear()
        self.assertTrue(q.empty())

    def test_clear(self):
        q = self.generate_test_queue(False)
        q.clear()
        self.assertTrue(q.get_queue_contents() == [])

    def test_size(self):
        q = self.generate_test_queue(True)
        self.assertTrue(q.size() == 4)


if __name__ == "__main__":    
    unittest.main()