def remove_duplicates(text_input):
    new_list = []  # an empty list to store unique elements

    for item in text_input:
        if item not in new_list:
            new_list.append(item)  # Append the item if it's not already in the list

    return new_list


# Example usage
input_list = input("Pls enter your items  ").split()
extended_list = remove_duplicates(input_list)
print("Unique list:", extended_list)
