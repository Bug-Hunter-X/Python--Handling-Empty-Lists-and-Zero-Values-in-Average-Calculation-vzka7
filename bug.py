def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
result = calculate_average(my_empty_list)  #Trying to return 0 if the list is empty
print(f"The average is: {result}")

my_numbers_with_zero = [10, 0, 20, 0, 30]
average_with_zero = calculate_average(my_numbers_with_zero) #Trying to handle the list with 0 values
print(f"The average is: {average_with_zero}")