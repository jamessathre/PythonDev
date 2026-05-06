#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: queue.py
Author: James Sathre
Date: 2026-05-06
Version: 1.0.0
Description: This script is an example queue implementation
"""

import unittest


class Queue:

    def __init__(self):
        self.data = []

    def push(self, input):
        self.data.append(input)

    def pop(self):
        self.data.pop(0)

    def front(self):
        """Access the front element of the queue"""
        return self.data[0]

    def back(self):
        """Access the end element of the queue"""
        return self.data[len(self.data)-1]

    def empty(self):
        """Check whether a queue is empty or not"""
        return len(self.data) == 0
    
    def clear(self):
        """clears all contents of a queue"""    
        self.data.clear()

    def get_queue_contents(self):
        return self.data

    def size(self):
        return len(self.data)


class TestQueueMethods(unittest.TestCase):
    
    def test_push(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertTrue(q.get_queue_contents() == [1, 2, 3])

    def test_pop(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.pop()
        self.assertTrue(q.get_queue_contents() == [2])

    def test_front(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertTrue(q.front() == 1)

    def test_back(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertTrue(q.back() == 3)

    def test_empty(self):
        q = Queue()        
        self.assertTrue(q.empty())

    def test_clear(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.clear()
        self.assertTrue(q.get_queue_contents() == [])

    def test_size(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertTrue(q.size() == 3)


if __name__ == "__main__":
    unittest.main()