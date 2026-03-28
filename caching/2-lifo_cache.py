#!/usr/bin/python3
""" LIFO Caching Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a LIFO caching system
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ 
        Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        # Check if key already exists to update order
        if key in self.cache_data:
            self.order.remove(key)
        
        # Add the item to cache and tracking list
        self.cache_data[key] = item
        self.order.append(key)

        # Handle overflow
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LIFO: Discard the second to last item added 
            # (The last one added is the one we just put in, 
            # so we discard the one that was previously the "newest")
            last_key = self.order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ 
        Get an item by key
        """
        return self.cache_data.get(key, None)
