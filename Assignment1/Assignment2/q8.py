def remove_duplicates_and_sort(numbers):
    
    
    unique_sorted = sorted(set(numbers))
    return unique_sorted



user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

result = remove_duplicates_and_sort(numbers)



print("List after removing duplicates and sorting:")
print(result)