from datetime import datetime, timedelta


def subtract_time(time_end: datetime, time_start: datetime) -> float:
    """
    Calculates the interval between two datetime objects in seconds,
    assuming they are on the same day.

    Args:
        time_end: The later datetime object.
        time_start: The earlier datetime object.

    Returns:
        The interval between the two times in seconds (as a float).
    """
    # The subtraction of two datetime objects results in a timedelta object
    interval: timedelta = time_end - time_start

    # timedelta has a built-in method to get the total seconds
    return interval.total_seconds()


# --- Example Usage ---

# Define two specific times for the same day (e.g., Nov 23, 2025)
# Make sure the dates are identical for the "same day" assumption to work simply.
time_morning = datetime(2025, 11, 23, 9, 0, 0)  # 9:00:00 AM
time_afternoon = datetime(2025, 11, 23, 14, 30, 0)  # 2:30:00 PM

# Calculate the difference
seconds_elapsed = subtract_time(time_afternoon, time_morning)

# Print the result
print(f"Start Time: {time_morning.strftime('%H:%M:%S')}")
print(f"End Time:   {time_afternoon.strftime('%H:%M:%S')}")
print(f"Interval in seconds: {seconds_elapsed}")
print(f"Interval in hours: {seconds_elapsed / 3600.0}")
