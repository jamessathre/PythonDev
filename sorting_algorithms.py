#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: sorting_algorithms.py
Author: James Sathre
Date: 2026-05-06
Version: 1.0.0
Description: This script my implementations of various sorting routines and their time.
"""

import numpy as np
import time
from functools import wraps

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Record start time
        start_time = time.perf_counter()
        
        # 2. Execute the actual function
        result = func(*args, **kwargs)
        
        # 3. Record end time and calculate duration
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        print(f"⏱️  '{func.__name__}' executed in {duration:.6f} seconds")
        return result
    return wrapper

@monitor_performance
def generate_random_list(number_elements=1000000):
    return np.random.randint(0, number_elements, size=number_elements)

@monitor_performance
def basic_sort(element_list=[]):
    element_list.sort()

def test_sort_times():
    rand_list = generate_random_list()
    # print("Random List ")
    # print(*rand_list)    
    
    print("Testing basic sort method")
    basic_sort(rand_list.copy())



if __name__ == "__main__":
    test_sort_times()
