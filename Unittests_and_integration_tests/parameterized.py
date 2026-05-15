#!/usr/bin/env python3
"""Minimal local replacement for parameterized.expand used in tests.
"""


class parameterized:
    """Simple stand-in for the external parameterized package."""

    @staticmethod
    def expand(cases):
        """Create one unittest method per case."""

        class ParameterizedTest:
            """Descriptor that registers generated test methods."""

            def __init__(self, function):
                self.function = function

            def __set_name__(self, owner, name):
                for index, case in enumerate(cases):
                    if not isinstance(case, tuple):
                        case = (case,)

                    def generated_test(self, _case=case, _function=self.function):
                        return _function(self, *_case)

                    generated_test.__name__ = f"{name}_{index}"
                    generated_test.__doc__ = self.function.__doc__
                    setattr(owner, generated_test.__name__, generated_test)

            def __get__(self, instance, owner):
                return self

        def decorator(fn):
            return ParameterizedTest(fn)

        return decorator