#!/usr/bin/env python3
"""Basic caching module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching"""

    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: key of the item
            item: value of the item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key

        Args:
            key: key to retrieve

        Returns:
            value linked to key or None
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)
