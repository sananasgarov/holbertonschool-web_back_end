#!/usr/bin/env python3
"""Minimal local replacement for parameterized.expand used in tests.
"""
from functools import wraps


class parameterized:
    """Simple stand-in for the external parameterized package."""

    @staticmethod
    def expand(cases):
        """Run the wrapped test once for each case."""

        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                for case in cases:
                    if not isinstance(case, tuple):
                        case = (case,)
                    fn(*args, *case, **kwargs)

            return wrapper

        return decorator