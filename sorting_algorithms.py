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
import random


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

def generate_random_list(number_elements=1000000):
    return np.random.randint(0, number_elements, size=number_elements)

@monitor_performance
def basic_sort(element_list=[]):
    element_list.sort()

def swap(i, j, list_ref):
    list_ref[i], list_ref[j] = list_ref[j], list_ref[i]

@monitor_performance
def quick_sort(element_list=[]):
    quick_sort_helper(element_list)

def quick_sort_helper(element_list=[]):
    list_len = len(element_list)
    # Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
    if list_len == 1:
        return

    # Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
    pivot_index = random.randint(0, list_len-1)
    pivot_number = element_list[pivot_index]

    num_less = 0
    for num in element_list:
        if num < pivot_number:
            num_less += 1

    swap(pivot_index, num_less, element_list)
    pivot_index = num_less

    # Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
    # swap numbers on left with numbers on right
    
    if num_less != 0:
        i = 0
        j = num_less
        
        for i in range(num_less):
            if element_list[i] > pivot_number:
                while j < list_len:
                    if element_list[j] < pivot_number:
                        swap(i, j, element_list)
                        break
                    else:
                        j += 1        

    # generate left list
    left_index = 0
    right_index = pivot_index if pivot_index > 0 else 1
    left_list = element_list[left_index:right_index]    

    #generate right list
    left_index = pivot_index+1 if (pivot_index+1) < list_len else list_len-1
    right_index = list_len
    right_list = element_list[left_index:right_index]
    
    # Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
    quick_sort_helper(left_list)
    quick_sort_helper(right_list)    

# @monitor_performance
def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(i, j, arr)
    
    # move pivot after smaller elements and
    # return its position
    swap(i + 1, high, arr)
    return i + 1

@monitor_performance
def quickSort2(arr, low, high):
    quickSort2Helper(arr, low, high)

def quickSort2Helper(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort2Helper(arr, low, pi - 1)
        quickSort2Helper(arr, pi + 1, high) 



def test_sort_times():
    num_list_elements = 1000000
    rand_list = generate_random_list(num_list_elements)
    # print("Random List ")
    # print(*rand_list)    
    
    # print("Testing basic sort method")
    basic_sort(rand_list.copy())        
    quick_sort(rand_list.copy())

    # test = np.array([1, 7, 5, 9, 2, 4, 3])
    # print(f"final list: {test}")
    quickSort2(rand_list.copy(), 0, num_list_elements-1)
    


if __name__ == "__main__":
    test_sort_times()
