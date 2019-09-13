import re


s = input("Enter a sentence : ")  # Taking input of sentence
str_arr = s.split()  # splitting the input sentence into words
result = ""  # initializing result as empty string
result += str_arr[0].lower()  # Converting first word ( word at index 0 ) of the input sentence into its lowercase
for i in str_arr[1:]:  #starting iterating from index 1 and onwards
    result += (i.capitalize())  # Capitalizing rest of the words

print("Output : ", result)  # printing the required resultant string


def capitalize(word):
    # Convert word to have uppercase first letter, rest in lowercase
    return word[0:1].upper() + word[1:].lower()

def camel_case(sentence):
    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence)


def lowercase(word):
    '''convert a word to lowercase'''
    return word.lower()

def filter(s):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    res = "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}"
    for x in s:
        if not(x in punctuations):
            res += x
    return res

def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)


if __name__ == '__main__':
    main()




