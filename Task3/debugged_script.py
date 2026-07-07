"""
Original Bug:

numbers = [10, 20, 30]
print(numbers[5])

This caused IndexError.
"""


numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range. Please check the list size.")