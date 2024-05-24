
def find_max_min():
    nums = input("Please enter some numbers separated by spaces: ").split()

    # Convert input strings to integers
    nums = [int(num) for num in nums]

    if not nums:
        print("No numbers were entered.")
        return None

    max_num = max(nums)
    min_num = min(nums)

    return max_num, min_num


result = find_max_min()
if result:
    max_num, min_num = result
    print(f"Maximum number is: {max_num}")
    print(f"Minimum number is: {min_num}")

