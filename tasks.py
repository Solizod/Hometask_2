# Find the Amount of Potatoes

# Posted by mkjlong ​​in Python

# language_fundamentals

# regex

# strings

# Create a function to return the amount of potatoes there are in a string.

# Examples

# potatoes ("potato") + 1

# potatoes ("potatopotato") →2

# potatoes ("potatoapple") → 1




# def potatoes(string):
#     return string.count("potato")

# print(potatoes("potato"))
# print(potatoes("potatopotato"))
# print(potatoes("potatoapple"))

# _________________________________________________________________


# Sum Greater Than Five

# Posted by BijogFc24 in Python

# arrays

# language_fundamentals

# math

# Write a function that returns the sum of elements greater than 5, in the given list.

# Examples

# sum_five([1, 5, 20, 30, 4, 9, 18]) 77

# sum_five ([1, 2, 3, 4]) → 0

# sum_five ([10, 12, 28, 47, 55, 100]) 252




# def sum_five(nums):
#     return sum(num for num in nums if num>5)

# print(sum_five([1, 5, 20, 30, 4, 9, 18]))
# print(sum_five([1, 2, 3, 4]))
# print(sum_five([10, 12, 28, 47, 55, 100]))


# _____________________________________________________________________________

# Stuttering Function

# Posted by Deep Xavier in Python

# algorithms

# formatting

# language_fundamentals

# strings

# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis pronounced with a question mark?. and space after each, and then the word is

# Examples

# stutter("incredible") →"in... in... incredible?"

# stutter("enthusiastic") "en... en... enthusiastic?"

# stutter("outstanding") →"ou... ou... outstanding?"



# def stutter(word):
#     return f"{word[:2]}... {word[:2]}... {word}?"

# print(stutter("incredible"))
# print(stutter("enthusiastic"))
# print(stutter("outstanding"))


# ________________________________________________________________________________________________________________________

# Find the Discount

# Posted by AniXDownLoе in Python

# math

# numbers

# Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.


# Examples

# dis (1500, 50) → 750

# dis (89, 20) → 71.2

# dis (100, 75) → 25 



# def dis(price, discount):
#     return price - (price / 100 * discount)

# print("Result --->  ", dis( 500, 50))
# print("Result --->  ",  dis(89, 20))
# print("Result --->  ", dis(100, 75))


# _____________________________________________________________________________________________________________________

# End Corona!

# Posted by Matt in Python

# math

# numbers

# Create a function that takes the number of daily average recovered cases recovers, daily average new_cases, current active_cases, and returns the number of days it will take to reach zero cases.

# Examples

# end_corona (4000, 2000, 77000) → 39

# end_corona (3000, 2000, 50699) → 51

# end_corona (30000, 25000, 390205) - 79

# Notes

# • The number of people who recover per day recovers will always be greater than daily new_cases

# • Be conservative and round up the number of days needed.


# def end_corona(recovers, new_cases, active_cases):
#     daily_net_recovery = recovers - new_cases
#     days_needed = (active_cases + daily_net_recovery - 1) // daily_net_recovery
#     return days_needed

# print("Result --->  ", end_corona(4000, 2000, 77000))
# print("Result --->  ", end_corona(3000, 2000, 50699))
# print("Result --->  ", end_corona(30000, 25000, 390205))


# _____________________________________________________________________________________________________________________

# Number Split

# Posted by Joshua Señoron in Python

# arrays

# math

# numbers

# Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

# Examples

# number_split(4) [2,2]

# number_split(10) [5, 5]

# number_split(11) - [5, 6]

# number_split(-9) ← [-5, -4]



# def number_split(num):
#     half = num // 2
#     return [half, num - half]

# print("Result --->  ", number_split(4))
# print("Result --->  ", number_split(10))
# print("Result --->  ", number_split(11))
# print("Result --->  ", number_split(-9))

# ___________________________________________________________________________________________________________________________________

# Fix the Errors / Comparing Arrays

# Published

# jameel in Python

# arrays

# bugs

# validation

# Programmer Pete is trying to create a function that returns True if two lists share the same length and have identical numerical values at every index, otherwise, it will return False.

# However, the solution his function gives is in an unexpected format. Can you fix Pete's function so that it behaves as seen in the examples below?

# Examples

# check_equals([1, 2], [1, 3]) False

# check_equals([1, 2], [1, 2]) → True

# check_equals([4, 5, 6], [4, 5, 6]) + True

# check_equals([4, 7, 6], [4, 5, 6]) + False

# check_equals([1, 12], [11, 2]) False


# def check_equals(list1, list2):
#     return list1 == list2

# print("Result --->  ", check_equals([1, 2], [1, 3]))
# print("Result --->  ", check_equals([1, 2], [1, 2]))
# print("Result --->  ", check_equals([4, 5, 6], [4, 5, 6]))
# print("Result --->  ", check_equals([4, 7, 6], [4, 5, 6]))
# print("Result --->  ", check_equals([1, 12], [11, 2]))


# _____________________________________________________________________________________________________________________________

# Word without First Character

# Posted by caloizou in Python

# formatting

# language_fundamentals

# strings

# Create a function that takes a word and returns the new word without including the first character.

# Examples

# new_word("apple") "pple"

# new_word("cherry") + "herry"

# new_word("plum") + "lum"

# Notes

# The input is always a valid word.


# def new_word(word):
#     return word[1:]

# print("Result --->  ", new_word("apple"))
# print("Result --->  ", new_word("cherry"))
# print("Result --->  ", new_word("plum"))


# _______________________________________________________________________________________________________

# Click me to see the sample solution

# 8. Write a Q Python program to calculate the sum of harmonic series upto n terms.

# Note: The harmonic sum is the sum of reciprocals of the positive integers.

# Example :

# def harmonic_sum(n):
#     sum = 0.0
#     for i in range(1, n + 1):
#         sum += 1 / i
#     return sum

# n = 5
# print("The sum of the Harmonic series up to ---> ", n, "terms is: ----> ", harmonic_sum(n))


# ___________________________________________________________________________________________________________

# The Reverser!

# Posted by Jake Braswell in Python

# formatting

# language_fundamentals

# strings

# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

# Examples

# reverse ("Hello World") → "DLROW OLLEH"

# reverse ("ReVeRsE") + "eSrEvEr"

# reverse("Radar") "RADAr"



# def reverse(s):
#     return s[::-1].swapcase()

# print("Result --->  ", reverse("Hello World"))
# print("Result --->  ", reverse("ReVeRsE") + "eSrEvEr")
# print("Result --->  ", reverse("Radar"))


def say_hello():
    return "HI"