#task 1
str = "The quick brown fox jumps over the lazy dog"

# a. Print the string to the page
print(str)

# b. Print the length of the string to the page
print(len(str))

# c. Print the string in all uppercase letters
print(str.upper())

# d. Print the string in all lowercase letters
print(str.lower())

# e. Print the string in the title case
print(str.title())

# f. Print the string in reverse
print(str[::-1])

# g. Print the string in reverse title case
print(str[::-1].title())

# h. Count the number of times the letter “a” appears in the string
print(str.count('a'))

# i. Count the number of times the word “the” appears in the string
print(str.count('the'))

# j. Replace the word “the” with the word “a”
print(str.replace('the', 'a'))


#task 4
str = "The quick brown fox jumps over the lazy dog"
frequency_dict = {}

for char in str:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

print(frequency_dict)




#task 5
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for i in range(len(people)):
    print(f"{people[i]} the {sex[i]} is {age[i]} years old.")
    