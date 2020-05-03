# Vowel counter
# Counts the number of vowels in word inputted by the user

print("Enter a word:")
user_input = input()

def count_vowels(word):
    length = len(word)
    num_vowels = 0          #initialize vowel counter to zero
    for i in range(0,length,1):
        if ( word[i]=='a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u'):
            num_vowels = num_vowels + 1
   
    return num_vowels

answer = count_vowels(user_input)
print(answer)