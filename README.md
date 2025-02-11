# Python: Handling Empty Lists and Zero Values in Average Calculation

This repository demonstrates a common error in Python when calculating the average of a list of numbers and provides a robust solution.  The original code lacks proper handling of empty lists and lists containing only zeros which may lead to ZeroDivisionError exceptions or incorrect results. The improved version addresses these issues for a more reliable average calculation.

## Problem:
The initial `calculate_average` function doesn't handle the cases of an empty list or a list containing only zeros. Dividing by zero will raise a `ZeroDivisionError`.  Even without a zero division error, an average of a list of all zeros is expected to be 0 rather than a division by zero error.