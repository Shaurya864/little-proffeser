#Write a function that takes a list and returns sum and average.
def sum_and_average(lst):
    total = sum(lst)
    avg = total / len(lst) if lst else 0
    return total, avg


nums = [10, 20, 30, 40]
print("Sum and Average:", sum_and_average(nums))