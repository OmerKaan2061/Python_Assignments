Sayı bulma oyunu :
------------------

answer = 28

question = "What a two-digit number am I thinking of?"

print('Lets begin the game!')
condition = True

while condition : #condition tanımlamazsak döngü sonnda break ile çıkarız

  guess = int(input(question))

  if guess > answer:
    print('little lower')
  elif guess < answer:
    print('little higher')
  else :
    print('Congrats')
    condition = False

/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

Cümledeki en uzun kelimeyi bulma :
----------------------------------

sentence = input("noktalama isareti olmayan bir cumle giriniz: ")
word_list = sentence.split()
i = 0
longest = 0
while i <= (len(word_list)-1):
    if len(word_list[i]) > longest :
        longest = len(word_list[i])
        b = word_list[i]
    i += 1
print(sentence, longest, b, sep="\n")