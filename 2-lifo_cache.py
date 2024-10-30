#!/usr/bin/python3
""" Module 1-fifo_cache.py """

# from base_caching import BaseCaching
from collections import OrderedDict
base_caching = __import__('base_caching').BaseCaching


class LIFOCache(base_caching):
    """
    Create a class FIFOCache that inherits from BaseCaching
    and is a caching system:
    """
    def __init__(self):
        """ instantiation of the class """
        super().__init__()
        self.cache.data = OrderedDict()

    def put(self, key, item):
        """ method to put data to dictionary"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > base_caching.MAX_ITEMS:
                last_item, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_item)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ getter method for the dictionary """
        return self.cache_data.get(key, None)
