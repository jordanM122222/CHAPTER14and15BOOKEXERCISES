class Date:
    """Represents a year, month, and day"""
    pass

def make_date(year: int, month: int, day: int) -> Date:
    """
    Creates a new Date object and assigns year, month, and day attributes.
    """
    date_obj = Date()
    date_obj.year = year
    date_obj.month = month
    date_obj.day = day
    return date_obj

def print_date(date_obj: Date):
    """
    Prints a Date object in YYYY-MM-DD format using an f-string.
    Months and days are zero-padded for consistent formatting.
    """
    print(f"{date_obj.year}-{date_obj.month:02}-{date_obj.day:02}")

def date_to_tuple(date_obj: Date) -> tuple:
    """
    Helper function: Takes a Date object and returns a tuple
    (year, month, day) in the correct comparison order.
    """
    return (date_obj.year, date_obj.month, date_obj.day)

def is_after(date1: Date, date2: Date) -> bool:
    """
    Checks whether the first Date object comes chronologically after the second.
    """
    # By converting dates to a tuple (YYYY, MM, DD), Python's tuple comparison
    # automatically handles chronological order checks (compares year, then month, then day).
    return date_to_tuple(date1) > date_to_tuple(date2)


# --- Execution and Testing ---

# 1. Create the first object representing June 22, 1933
date1 = make_date(1933, 6, 22)

# 2. Print the first date to verify the format
print("Date 1:")
print_date(date1) # Expected output: 1933-06-22

# 3. Create the second object representing September 17, 1933
date2 = make_date(1933, 9, 17)

print("\nDate 2:")
print_date(date2) # Expected output: 1933-09-17

# 4. Check whether the second object comes after the first
print(f"\nIs Date 2 after Date 1? {is_after(date2, date1)}") # Expected: True

# Check the inverse as well
print(f"Is Date 1 after Date 2? {is_after(date1, date2)}") # Expected: False

# Check dates in different years
date3 = make_date(2020, 1, 1)
print(f"\nIs 2020-01-01 after 1933-06-22? {is_after(date3, date1)}") # Expected: True
