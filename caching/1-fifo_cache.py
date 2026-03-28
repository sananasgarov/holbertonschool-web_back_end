#!/usr/bin/env python3
""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Init """
        super().__init__()
        self.order = []  # FIFO üçün sıra saxlayırıq

    def put(self, key, item):
        """ Add item in cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """ Get item """
        if key is None:
            return None
        return self.cache_data.get(key)
