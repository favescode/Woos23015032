"""This program will collect user input in form of string and count them"""
def count_words(input_string):
    words = input_string.split()  # for Spliting the input string into words
    num_words = {}

    for word in words:
        if word in num_words:  # checking in the dictionary
            num_words[word] += 1  # Increment its count
        else:
            num_words[word] = 1  # Add the word to the dictionary with count 1

    return num_words
input_string = input("Pls enter string of string$ ")
word_counts = count_words(input_string)
print(word_counts)
