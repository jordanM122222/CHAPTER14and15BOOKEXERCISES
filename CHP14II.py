# Assuming a 'Time' class or 'make_time' function is defined elsewhere
# that returns an object capable of standard comparison or has time components.
# If using Python's standard library, we use datetime.time objects as shown below.

from datetime import time


def is_after(t1: time, t2: time) -> bool:
    """Checks whether `t1` is after `t2`.

    >>> is_after(time(3, 2, 1), time(3, 2, 0))
    True
    >>> is_after(time(3, 2, 1), time(3, 2, 1))
    False
    >>> is_after(time(11, 12, 0), time(9, 40, 0))
    True
    """
    # Python's built-in time objects correctly overload the '>' operator.
    # It compares the hours, then minutes, then seconds, then microseconds.
    return t1 > t2


# --- If you are using a custom 'Time' class where comparison might not be built-in,
# --- you would need to define how that comparison works internally.
# --- Here is an example implementation of a simple Time class for context:

class CustomTime:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    # Define how to compare this custom object
    def __gt__(self, other):
        # Convert both times into seconds from the start of the day for easy comparison
        seconds_self = self.h * 3600 + self.m * 60 + self.s
        seconds_other = other.h * 3600 + other.m * 60 + other.s
        return seconds_self > seconds_other

    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def __repr__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


def is_after_custom(t1: CustomTime, t2: CustomTime) -> bool:
    """Checks whether `t1` is after `t2` using the CustomTime class."""
    # This works because we defined the __gt__ method in the class above.
    return t1 > t2

# Example usage with custom class:
# print(f"Is 03:02:01 after 03:02:00? -> {is_after_custom(CustomTime(3, 2, 1), CustomTime(3, 2, 0))}")
# print(f"Is 11:12:00 after 09:40:00? -> {is_after_custom(CustomTime(11, 12, 0), CustomTime(9, 40, 0))}")
