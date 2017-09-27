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


##########################

# If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

# For example:
# Input: "1123". You need to general all valid alphabet codes from this string.

# Output List
# aabc //a = 1, a = 1, b = 2, c = 3
# kbc // since k is 11, b = 2, c= 3
# alc // a = 1, l = 12, c = 3
# aaw // a= 1, a =1, w= 23
# kw // k = 11, w = 23


###############################

# Given a string S, and an integer K, rearrange the string such that similar characters are at least K distance apart.

# Example:

# S = AAABBBCC, K = 3
# Result : ABCABCABC (all 'A's are 3 distance apart, similarly with B's and C's)

# S = AAABC, K=2 : Not possible. (EDIT : k=3 is not possible).

# S = AAADBBCC, K = 2:
# Result: ABCABCDA