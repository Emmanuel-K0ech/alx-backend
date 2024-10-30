#!/usr/bin/python3
""" 0-basic_cache.py module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache class """
    def put(self, key, item):
        """ setter method """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Getter method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
