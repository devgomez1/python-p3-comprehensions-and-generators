#!/usr/bin/env python3

def return_evens(num_list):
    new_list = []

    for num in num_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

def make_exclamation(sentence_list):
   new_list = []

   for list in sentence_list:
         new_list.append(list + "!")
   return new_list
    