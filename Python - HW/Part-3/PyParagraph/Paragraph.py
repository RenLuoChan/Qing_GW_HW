#import re
import os
#import string


paragraph_path1 = os.path.join('raw_data','paragraph_1.txt')

#re.split("(?<=[.!?]) +", paragraph)
def load_file(filepath1):
    with open(filepath1, "r") as paragraph_file_handler1:
        return paragraph_file_handler1.read().lower().split()
    
word_list1 = load_file(paragraph_path1)
word_count1 = {}.fromkeys(word_list1, 0)

# Loop through the word list and count each word.
for word1 in word_list1:
    word_count1[word1] += 1
#print(word_count)

num_word1 = len(word_count1)

print("Paragraph 1 Analysis")
print("-----------------------")
print("Approximate Word Count: ", num_word1)
#print("Approximate Sentence Count: ", num_s)
#print("Average Letter Count: ", average_l)
#print("Average Sentence Length: ", average_s)



print("*******************************************************\n")



paragraph_path2 = os.path.join('raw_data','paragraph_2.txt')

#re.split("(?<=[.!?]) +", paragraph)
def load_file(filepath2):
    with open(filepath2, "r") as paragraph_file_handler2:
        return paragraph_file_handler2.read().lower().split()
    
word_list2 = load_file(paragraph_path2)
word_count2 = {}.fromkeys(word_list2, 0)

# Loop through the word list and count each word.
for word2 in word_list2:
    word_count2[word2] += 1
#print(word_count)

num_word2 = len(word_count2)

print("Paragraph 2 Analysis")
print("-----------------------")
print("Approximate Word Count: ", num_word2)
