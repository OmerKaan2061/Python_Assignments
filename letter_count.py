sentence = str(input("Please enter a sentence: ").lower()) #takes the sentence from the user
sen_list = list(sentence) #makes the sentence iterable by listing 
sen_dict = {} # an empty dictionary to add items in
count = len(sen_list) #counts the characters of the sentence

for i in range(count):
   sen_dict.update({i : sen_list[i]}) #adds every character with a key and value to the dictionary

print(sen_dict)