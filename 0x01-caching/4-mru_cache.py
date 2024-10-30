#!/usr/bin/env python3
""" Module 4-mru_cache.py"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    A class MRUCache that inherits from
    BaseCaching
    """
    def __init__(self):
        """Initializing"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Setter method"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                most_recently_used, _ = self.cache_data.popitem(False)
                print("DISCARD:", most_recently_used)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Getter method"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
