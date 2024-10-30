#!/usr/bin/python3
""" Module 3-lru_cache.py """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Create a class LRUCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ instantiation of the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ method to put data to dictionary"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                least_used_item, _ = self.cache_data.popitem(True)
                print("DISCARD:", least_used_item)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item


    def get(self, key):
        """ getter method for the dictionary """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
