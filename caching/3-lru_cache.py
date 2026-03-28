#!/usr/bin/env python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Init """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add item in cache """
        if key is None or item is None:
            return

        # Əgər key artıq varsa → yenilə
        if key in self.cache_data:
            self.usage_order.remove(key)
        else:
            # yeni keydirsə və limit dolubsa
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get item """
        if key is None or key not in self.cache_data:
            return None

        # istifadə olundu → sona at
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
