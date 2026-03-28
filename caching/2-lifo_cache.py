#!/usr/bin/env python3
from base_caching import BaseCaching
class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Init """
        super().__init__()
        self.stack = []  # son əlavə olunanları izləmək üçün

    def put(self, key, item):
        """ Add item in cache """
        if key is None or item is None:
            return

        # Əgər yeni keydirsə stack-ə əlavə et
        if key not in self.cache_data:
            self.stack.append(key)

        self.cache_data[key] = item

        # limit aşılırsa → sonuncunu sil
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """ Get item """
        if key is None:
            return None
        return self.cache_data.get(key)
