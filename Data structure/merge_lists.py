'This program will execute the program containing all elements from both without duplicates'


def merge_lists():
    lst1 = input("Please enter items for the first list,with spaces: ").split()
    lst2 = input("Please enter items for the second list, with spaces: ").split()

    merged_list = list(set(lst1 + lst2))
    merged_list.sort()
    return merged_list


print(merge_lists())
