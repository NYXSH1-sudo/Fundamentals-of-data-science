def count_occurrences(numbers):
    freq = {}
    
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return freq



list1 = [1, 2, 2, 3, 3, 3]
print("List 1:", list1)
print("Output:", count_occurrences(list1))
print()

list2 = [5, 5, 5, 5, 1, 2, 2]
print("List 2:", list2)
print("Output:", count_occurrences(list2))
print()

list3 = [10, 20, 10, 30, 20, 10, 40]
print("List 3:", list3)
print("Output:", count_occurrences(list3))