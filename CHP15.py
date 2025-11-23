class Date:
    def __init__(self, year, month, day):
        """
        Initializes a Date object with year, month, and day attributes.
        """
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """
        Returns a string representation of the date in YYYY-MM-DD format.
        """
        # Using an f-string with zero padding for month and day
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def to_tuple(self):
        """
        Helper method to return date attributes as a tuple for easy comparison.
        """
        return (self.year, self.month, self.day)

    def is_after(self, other_date):
        """
        Checks if this date object comes after the other_date object.
        """
        return self.to_tuple() > other_date.to_tuple()

# Create the first Date object: June 22, 1933
date1 = Date(1933, 6, 22)
print(f"Date 1: {date1}") # Output: Date 1: 1933-06-22

# Create the second Date object: September 17, 1933
date2 = Date(1933, 9, 17)
print(f"Date 2: {date2}") # Output: Date 2: 1933-09-17

# Check whether the second object comes after the first object
# We call the method on date2, passing date1 as the 'other_date' argument
print(f"Does date2 come after date1? {date2.is_after(date1)}") # Output: Does date2 come after date1? True

# Check the other way around
print(f"Does date1 come after date2? {date1.is_after(date2)}") # Output: Does date1 come after date2? False
