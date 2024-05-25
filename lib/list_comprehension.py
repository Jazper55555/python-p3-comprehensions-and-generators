#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [n for n in num_list if n % 2 == 0]
    return even_num
    pass

def make_exclamation(sentence_list):
    ex_list = [n + '!' for n in sentence_list]
    return ex_list
    pass