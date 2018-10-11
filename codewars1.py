# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:31:12 2018

@author: Admin
"""
# https://www.codewars.com

''' Given an array, find the int that appears an odd number of times.
'''
def find_it(seq):
    for n in seq:
        if seq.count(n) % 2 == 1:
            return n

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

print('*'*40)

''' check  that the elements in b are the elements in a squared, 
regardless of the order.
'''
import math
def comp(array1, array2):
    # your code
    if (not array1) or (not array2) :
        print('empty array(s)')
        return False    
    elif len(array1) != len(array2) :
        print('arrays have different lengths')
        return False
    else:
        for a in array1:
            if a != a or not isinstance(a,int):
                return False
            
        for b in array2:
            if b != b or not isinstance(b,int):
                return False
        array1 = sorted(array1)
        array2 = sorted(array2)
        array1sq = [i**2 for i in array1]
        array2sqrt = [math.sqrt(i) for i in array2]
        print(array1sq)
#        print(array2)
        print(array2sqrt)
#        return array2 == array1sq
        return array1 == array2sqrt

        # check for all a if there is a matching b
#        for a in array1:
#            same = False
#            for b in array2:
#                # print(a,b)
#                if a**2 == b:
#                    same = True
#                    break # go to next a
#            if same == False: # didn't find a matching b
#                return same
#        
#        # check for all b if there is a matching a
#        for b in array2:
#            same = False
#            for a in array1:
#                if a**2 == b:
#                    same = True
#                    break # go to next b
#            if same == False: # didn't find a matching a
#                return same
#                
#        return same

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
a3 = [11,19]
a4 = [12,11*11]
a5 = ['text', 'test']
a6 = [14,79]
a7 = [19,6241]
a8 = [100]
a9 = [10001]
a10 = [15,93]
a11 = [226, 8649]
print(comp(a1, a2))
print(comp(a3, a4))
print(comp(a3,a5))
print(comp(a6,a7))
print(comp(a8,a9))
print(comp(a10,a11))

print('*'*40)

''' Your task is to sort a given string. 
Each word in the String will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. 
The words in the input String will only contain 
valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return 
"Thi1s is2 3a T4est"
'''

def order(sentence):
  if not sentence:
      return sentence
  else:
      my_dic = {'1': 'NONE', '2': 'NONE', '3': 'NONE',
              '4': 'NONE', '5': 'NONE', '6': 'NONE',
              '7': 'NONE', '8': 'NONE', '9': 'NONE'}
      words = sentence.split(' ')
      for w in words:
          for c in w:
              if c.isdigit():
                  my_dic[c] = w
      sorted_dic = sorted(my_dic.items())
      ordered_sentence = ''
      w_count = 0
      for s in sorted_dic:
          if s[1] != 'NONE':
              w_count += 1
              if w_count == 1:
                  ordered_sentence += (s[1])
              else:
                  ordered_sentence += (' ' + s[1])
      return ordered_sentence

print("Thi1s is2 3a T4est -->", order("is2 Thi1s T4est 3a"))

def order_better(sentence):
    return ' '.join(sorted(sentence.splits(' '), 
                           key=lambda w: filter(str.isdigit, w)))
print("Thi1s is2 3a T4est -->", order("is2 Thi1s T4est 3a"))

print('*'*40)

'''
Move the first letter of each word to the end of it, then add "ay" 
to the end of the word. Leave punctuation marks untouched.
examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
'''
from string import punctuation
def pig_it(sentence):
    words = sentence.split()
    new_words = []
    for w in words:
        if w in punctuation:
            new_words.append(w)
        else:
            new_words.append(''.join([w[1:],w[0],'ay']))
    new_sentence = ' '.join(new_words)
    return new_sentence

print('Pig latin is cool ! -->', pig_it('Pig latin is cool !'))

def pig_it_better(sentence):
    lst = sentence.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' 
                      if word.isalpha() else word for word in lst])
    
print('Pig latin is cool ! -->', pig_it_better('Pig latin is cool !'))

print('*'*40)

''' Your task in this kata is to implement a function that calculates 
the sum of the integers inside a string. 
For example, in the string 
"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum 
of the integers is 3635.
'''
def sum_of_int_in_string(s):
#    return [i for i in s]
    return sum([int(i) for i in s if i.isdigit()])

print('h3ll0w0rld -->', sum_of_int_in_string('h3ll0w0rld'))
print('The Great Depression lasted from 1929 to 1939. -->', 
      sum_of_int_in_string('The Great Depression lasted from 1929 to 1939.'))
print('*'*40)

import string

print(string.ascii_letters)

''' Write a method that takes an array of consecutive (increasing) letters 
as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter 
be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
'''
def find_missing_letter(chars):
    if chars[0] in string.ascii_lowercase:
        full = string.ascii_lowercase
    elif chars[0] in string.ascii_uppercase:
        full = string.ascii_uppercase
    full_chars = [c for c in full]
    pos_start = full_chars.index(chars[0])
    for i,c in enumerate(chars):
        print(i, c, full_chars[pos_start+i])
        if full_chars[pos_start+i] != c:
            return full_chars[pos_start+i]

print('test:')
print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))
print('*'*40)

''' Tortoise racing
More generally: given two speeds v1 (A's speed, integer > 0) 
and v2 (B's speed, integer > 0) and a lead g (integer > 0) 
how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time 
needed in hours, minutes and seconds (don't worry for 
fractions of second).
'''

def race(v1,v2,g):
    hms = [0,0,0]
    h_float = 0.
    if v2 > v1:
        h_float = float(g)/float(v2-v1) # h in float
    else:
        return None
    secs = h_float*3600
    hms[0] = math.floor(h_float)
#    m_float = (h_float % 1)*60.
#    hms[1] = math.floor(m_float)
    hms[1] = math.floor((secs % 3600) / 60)
#    s_float = (m_float % 1)*60.
    hms[2] = math.floor(secs % 60)    
    return hms

def race_better(v1,v2,g):
    if v1 >= v2:
        return None
    secs = 3600*g/(v2-v1)
    return [secs/3600, secs%3600/60, secs%60]

print('test:')
print('race(720, 850, 70):', race(720, 850, 70))
print('race(80, 100, 40):', race(80, 100, 40))
print('race(70, 80, 1):', race(70, 80, 1))
print('race(20, 45, 11):', race(20, 45, 11))

print('*'*40)

'''
Given a list lst and a number N, create a new list that contains 
each number of lst at most N times without reordering. For example 
if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in
 the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
 '''
 
def delete_nth(order, max_e):
     ans = []
     for i in order:
         if ans.count(i) < max_e:
             ans.append(i)
     return ans

print('test:')
print('delete_nth([20,37,20,21], 1)', delete_nth([20,37,20,21], 1))
print('delete_nth([1,1,3,3,7,2,2,2,2], 3)', delete_nth([1,1,3,3,7,2,2,2,2], 3))

print('*'*40)

'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the 
input string. The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.
'''

def duplicate_count(text):
    count_dict = {}
    unique_chars = []
    for c in list(text.lower()):
        if c not in unique_chars:
            unique_chars.append(c)
            count_dict[c] = text.count(c)
    print(count_dict)
    n_dup = 0
    for k,v in count_dict.items():
        if v > 1:
            n_dup += 1
    return n_dup

print('test:')
print('duplicate_count("abcde")', duplicate_count("abcde"))
print('duplicate_count("a1bc1d22e")', duplicate_count("a1bc1d22e"))
print('duplicate_count("Indivisibilities")', duplicate_count("Indivisibilities"))
print('duplicate_count("AaAbBC1bc1d22e")', duplicate_count("AaAbBC1bc1d22e"))

print('*'*40)

'''
takes in numbers num1 and num2 and returns 1 if there is a straight triple 
of a number at any place in num1 and also a straight double of the same 
number in num2.
'''

#def triple_double(num1,num2):
#    c1 = 0
#    c2 = 0
#    int_list1 = [int(i) for i in str(num1)]
#    int_list2 = [int(i) for i in str(num2)]
#    for o, i in enumerate(int_list1):
#        if i > 0:
#            if i == int_list1[0-1]:
#                c1 += 1

print('test:')


print('*'*40)

'''
So this function should return the first pair of two prime numbers spaced 
with a gap of g between the limits m, n if these numbers exist otherwise nil 
or null or None or Nothing
'''

def gap(g, m, n):
#    first_prime = 2
    prime_count = 0
    for k in range(m,n+1):
        k_is_prime = True
        for i in range(2, int(k/2)+1):
#            print(k,i)
            if k%i == 0:
                k_is_prime = False
                break
        if k_is_prime:
            prime_count += 1
#            print(f'{k} is prime, prime count = {prime_count}')
            if prime_count == 1:
                first_prime = k
            elif k - first_prime == g:
                return [first_prime, k]
            else:
                first_prime = k

print('test:')
print('gap(5,2,100)', gap(5,2,100))
print('gap(2,100,200)', gap(2,100,200))
print('gap(10,300,400)', gap(10,300,400))
print('*'*40)
