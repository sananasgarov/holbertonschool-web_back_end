#!/usr/bin/env python3
"""Minimal local replacement for parameterized helpers used in tests.
"""

import sys


class parameterized:
    """Simple stand-in for the external parameterized package."""

    @staticmethod
    def _make_test_name(base_name, index, case):
        """Build a unittest-friendly generated test name."""
        test_name = f"{base_name}_{index}"

        if case and isinstance(case[0], str):
            suffix = "".join(
                character if character.isalnum() else "_"
                for character in case[0]
            )
            test_name = f"{test_name}_{suffix}"

        return test_name

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

                    generated_test.__doc__ = self.function.__doc__

                    test_names = [f"{name}_{index}"]
                    generated_name = parameterized._make_test_name(name, index, case)
                    if generated_name not in test_names:
                        test_names.append(generated_name)

                    for test_name in test_names:
                        generated_test.__name__ = test_name
                        setattr(owner, test_name, generated_test)

            def __get__(self, instance, owner):
                return self

        def decorator(fn):
            return ParameterizedTest(fn)

        return decorator

    @staticmethod
    def parameterized_class(attrs, cases):
        """Create one unittest subclass per case."""

        if isinstance(attrs, str):
            attrs = (attrs,)

        def decorator(cls):
            module = sys.modules[cls.__module__]

            for index, case in enumerate(cases):
                if not isinstance(case, tuple):
                    case = (case,)

                values = dict(zip(attrs, case))
                class_name = f"{cls.__name__}_{index}"
                generated_class = type(class_name, (cls,), values)
                generated_class.__module__ = cls.__module__
                setattr(module, class_name, generated_class)

            cls.__test__ = False
            return cls

        return decorator


parameterized_class = parameterized.parameterized_class