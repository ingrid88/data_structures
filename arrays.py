import pdb

def word_combos(st):
    i = 0
    for jj in range(len(st)+1):
        if st[i:jj] in words:
            # pdb.set_trace()    
            # print st[i:jj]
            i = jj
            # print jj
    if i == len(st):
        return True
    else:
        return False
         
        
def can_decompose(st):
    # print st
    if len(st) == 0:
        return True
# True if exists a prefix w of s that belongs to dict and f(s without the prefix w) is True,
    for j in range(len(st) + 1):
        if st[0:j] in words:
            if can_decompose(st[j:len(st) + 1]):
                # print st[0:j]
                return True
    return False


def words_found(s):
    if len(s) == 0:
        return ''

    for j in range(len(s) + 1):
        if (s[0:j] in words) and (words_found(s[j:len(s) + 1]) is not None): 
            return s[0:j] + "," + words_found(s[j:len(s) + 1])
    return None

# f(s) = {
    # return words separated by commas if a composition is possible
    #  else return None
# }

def print_combos(s, word_list=''):

    count = 0
    if len(s) == 0:
        print 'word list'
        print word_list
        word_list = ''
        return 1
    for j in range(len(s) + 1):
        if s[0:j] in words: 
            variants_count = print_combos(s[j:len(s) + 1], word_list +"."+ s[0:j])
            if variants_count > 0:
                count += variants_count

    return count


def number_of_variants_found(st, words):
    # print st
    count = 0
    if len(st) == 0:
        print "len st 0"
        return 1
# True if exists a prefix w of s that belongs to dict and f(s without the prefix w) is True,
    for j in range(len(st) + 1):
        if st[0:j] in words:

            variants_count = number_of_variants_found(st[j:len(st) + 1], words)
            if variants_count > 0:
                print st[0:j]
                count += variants_count
    return count

# f(s) = {
#     // returns true iff the s is decomposable with words from the dictionary
#     True if s is empty,
#     True if exists a prefix w of s that belongs to dict and f(s without the prefix w) is True,
#     False otherwise (there doesn't exist a prefix...)
# }



# words = {"a", "aa", "aaa", "aaaa", "b"}
# s = "baaaaaaaaaaaabaaaaaaaaaab"
# print can_decompose(s)



words = {
"take",
"bat",
"cat",
"tak",
"bath",
"and",
"come",
"hand"}
# s = "take"

# print can_decompose(s)
# print "{} variants found".format(number_of_variants_found(s, words))
# print words_found(s)
# print words_found2(s)
# s = "takebathandcome"
# print can_decompose(s)
# print "{} variants found".format(number_of_variants_found(s, words))
# print words_found(s)
# print words_found2(s)
s = "takebathandcomecat"
# print word_combos(s)
# print can_decompose(s)
print print_combos(s)
# print "{} variants found".format(number_of_variants_found(s, words))
# print words_found(s)
# print words_found2(s)
# s = "takebathandcomes"
# print can_decompose(s)
# print "{} variants found".format(number_of_variants_found(s, words))
# print words_found(s)
# print words_found2(s)
# s = "takeathandcomes"
# print can_decompose(s)
# print "{} variants found".format(number_of_variants_found(s, words))
# print words_found(s)
# print words_found2(s)
#####################################
def find_grants_cap(grantsArray, newBudget):
  # algorithm: 
    # { For all values in array that are less than the cap/len(array)
      # substract that value from the cap and count the number of times this occurs
    # divide the new value by the number of numbers over the cap/len(array) 
    # replace all values with new value calculated in division }
  count = 0
  for grant in grantsArray:
    if grant < float(newBudget) / len(grantsArray):
      count += 1
      newBudget -= grant
  print newBudget
  for i, grant in enumerate(grantsArray):
    if grant > float(newBudget) / len(grantsArray):
      grantsArray[i] = float(newBudget) / (len(grantsArray) - count)
  cap = float(newBudget) / (len(grantsArray) - count)
  return cap

import numpy

def find_grants_cap(grantsArray, newBudget):
  # algorithm: 
    # { Order grants from least to greatest and iterate through
      # if the value is less than the average_cap
          # substract value from budget and recaculate cap
      # if the value is more than the cap, then return cap }
  grantsArray = numpy.sort(grantsArray)
  cap = float(newBudget) / len(grantsArray)
  for i, grant in enumerate(grantsArray):
    if grant < cap:
      newBudget -= grant
      cap = float(newBudget) / len(grantsArray[i+1:])
  return cap

grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print find_grants_cap(grantsArray, newBudget)

grantsArray = [2,100,50,120,167]
newBudget = 400
print find_grants_cap(grantsArray, newBudget)
# output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190

##########################

import random


def inplace_shuffle(l):
    for i, value in enumerate(l):
        random_position = numpy.floor(len(l[i:])*random.random() + i)
        b = l[random_position]
        a = value
        l[i] = b
        l[random_position] = a
    return l

# l = [1,5,2,4,3]
# print inplace_shuffle(l)
# Write a function for doing an in-place shuffle of a list.
# The shuffle must be "uniform," meaning each item in the original 
# list must have the same probability of ending up in each spot in the final list.

# Assume that you have a function get_random(floor, ceiling) 
# for getting a random integer that is >= floor and <= ceiling.    
#########################

def twoSum(nums, target):
    seq_length = len(nums)
    for i in range(seq_length):
        for j in range(seq_length):
            if (nums[i] != nums[j]) and (nums[j] + nums[i] == target):
                print nums[i]
                print nums[j]
                print nums[i] + nums[j]
                return [i, j]
    return None   

print "twoSum"
print twoSum([2,3,7,5], 12)  
print "  "   
##########################

    def addTwoNumbers(l1, l2):
        carry_over = 0
        solution = []
        print l1
        print l2
        i = 0
        diff = len(l1) - len(l2)
        if diff > 0:
            solution = l1[0:diff]
            l1 = l1[diff:]
        if diff < 0:
            solution = l2[0:diff]
            l2 = l2[diff:]
        for i in range(len(l1)-diff):
            s = l1[i] + l2[i]
            left_over = s % 10
            solution.append(left_over + carry_over)
            carry_over = 10 - left_over
        return solution

##########################


def find_duplicates(arr1, arr2):
  duplicates = []
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      i += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      duplicates.append(arr1[i])
      j += 1
      i += 1
  return duplicates

arr1 = [1, 2, 3, 5, 6, 7]

arr2 = [3, 6, 7, 8, 20]
print find_duplicates(arr1, arr2)
'''
 arr1 = [1, 2, 3 ...1000... 2000] len(arr1) = 10
                    i
 arr2 = [1000 --- 1004] ... len(arr2) = 10000000000
            j
            
            
   M = very large  
   
   N = small each value from the smaller array, in the bigger array.
   N^2 + N 
 
'''


# If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

# For example:
# Input: "1123". You need to general all valid alphabet codes from this string.

# Output List
# aabc //a = 1, a = 1, b = 2, c = 3
# kbc // since k is 11, b = 2, c= 3
# alc // a = 1, l = 12, c = 3
# aaw // a= 1, a =1, w= 23
# kw // k = 11, w = 23

def generated_strings(string_number="1123"):
    pass

###############################

# Given a string S, and an integer K, rearrange the string such that similar characters are at least K distance apart.

# Example:

# S = AAABBBCC, K = 3
# Result : ABCABCABC (all 'A's are 3 distance apart, similarly with B's and C's)

# S = AAABC, K=2 : Not possible. (EDIT : k=3 is not possible).

# S = AAADBBCC, K = 2:
# Result: ABCABCDA