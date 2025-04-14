###WORD COUNTER###

#user_input
user_input = input('Enter a sentence to count the amount of words: ')

#Methods
words = user_input.split() #slipts the sentence by space

number_of_words = len(words) #Counts the number of items in words

#output
print(f'This sentence has {number_of_words} words in total.')



#remove duplicates
#unique_words = []

#for word in words: #looping in split list
#    if word not in unique_words and word.isalnum(): #check if word is a word
#        unique_words.append(word)


#output
print(f'This sentence has {number_of_words} words in total.')
#The cat in the hat, knows about hats! and thats
