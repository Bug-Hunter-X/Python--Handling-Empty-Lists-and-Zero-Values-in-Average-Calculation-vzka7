def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    if total == 0:
        return 0 # Handle list with all zeros
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
result = calculate_average(my_empty_list)  # Returns 0 for empty list
print(f"The average is: {result}")

my_numbers_with_zero = [10, 0, 20, 0, 30]
average_with_zero = calculate_average(my_numbers_with_zero) # Handles list with zeros correctly
print(f"The average is: {average_with_zero}")

my_all_zeros = [0, 0, 0]
result_all_zeros = calculate_average(my_all_zeros) #Returns 0 for a list of all zeros
print(f"The average is: {result_all_zeros}") 