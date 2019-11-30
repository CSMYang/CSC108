"""Starter for CSC108 Assignment 2"""

from typing import List, TextIO

ENCRYPT = 'e'
DECRYPT = 'd'

def clean_message(s: str) -> str:
    """Return a cleaned version of string s with only uppercase letters inside.
    
    >>> clean_message('a.wG135')
    'AWG'
    >>> clean_message('hfuaohfo')
    'HFUAOHFO'
    """
    new = ''
    for char in s:
        if char.isalpha():
            new = new + char
    return new.upper()

def swap_cards(l: List[int], n: int) -> None:
    """Modify the list l and switch the position of element at index n with
    the element under it.
    >>> s = [1, 3, 5, 6, 9]
    >>> swap_cards(s, 3)
    >>> s
    [1, 3, 6, 5, 9]
    """
    if n < len(l) - 1:
        right = l[n + 1]
        l[n + 1] = l[n]
        l[n] = right
    else:
        right = l[0]
        l[0] = l[n]
        l[n] = right

def get_small_joker_value(l: List[int]) -> int:
    """Return the second highest value in l.
    Precondition: len(l) >= 2
    >>> get_small_joker_value([1, 7, 9, 5, 10])
    9
    """
    new_list = l[:]
    new_list.sort()
    return new_list[-2]

def get_big_joker_value(l: List[int]) -> int:
    """Return the highest value in l.
    >>> get_big_joker_value([1, 7, 9, 5, 10])
    10
    """
    return max(l)

def move_small_joker(l: List[int]) -> None:
    """ Swap the second highest value in l with the number follows it.
    >>> l = [1, 3, 8, 7, 5]
    >>> move_small_joker(l)
    [1, 3, 8, 5, 7]
    """
    swap_cards(l, l.index(get_small_joker_value(l)))

def move_big_joker(l: List[int]) -> None:
    """Move the highest value in list l two places down.
    >>> l = [1, 3, 8, 7, 5]
    >>> move_big_joker(l)
    >>> l
    [1, 3, 7, 5, 8]
    
    """
    swap_cards(l, l.index(get_big_joker_value(l)))
    swap_cards(l, l.index(get_big_joker_value(l)))

def triple_cut(l: List[int]) -> None:
    """Move the part of list after the second highest value and switch the
    position of that part with the part of list before the highest value in
    the list.
    >>> l = [1, 9, 5, 7, 3]
    >>> triple_cut(l)
    >>> l
    [3, 9, 5, 7, 1]
    """
    mi = min(l.index(get_small_joker_value(l)), l.index(get_big_joker_value(l)))
    ma = max(l.index(get_small_joker_value(l)), l.index(get_big_joker_value(l)))
    if mi == 0:
        left = []
    else:
        left = l[:mi]
    middle = l[mi : ma + 1]
    if l[ma] == l[-1]:
        right = []
    else:
        right = l[ma + 1:]
    l[:] = right + middle + left

def insert_top_to_bottom(l: List[int]) -> None:
    """Move the first a few numbers in list l and put them before the last num.
    Number of 'last num in the list' numbers are moved.
    
    >>> l = [1, 3, 5, 7, 2]
    >>> insert_top_to_bottom(l)
    >>> l
    [5, 7, 1, 3, 2]
    """
    n = l[-1]
    if n == max(l):
        n = get_small_joker_value(l)
    first_few = l[: n]
    l[:] = l[n: -1] + first_few + l[-1: -2: -1]

def get_card_at_top_index(l: List[int]) -> int:
    """Return the number at index of first number in list l.
    >>> get_card_at_top_index([1, 3, 5, 7, 9])
    3
    """
    v = l[0]
    if v == get_big_joker_value(l):
        v = get_small_joker_value(l)
    return l[v]

def get_next_keystream_value(l: List[int]) -> int:
    """Return the next keystream value of list l. 
    >>> get_next_keystream_value([1, 2, 3, 4, 5])
    2
    """
    move_small_joker(l)
    move_big_joker(l)
    triple_cut(l)
    insert_top_to_bottom(l)
    n = get_card_at_top_index(l)
    while n == get_big_joker_value(l) or n == get_small_joker_value(l):
        move_small_joker(l)
        move_big_joker(l)
        triple_cut(l)
        insert_top_to_bottom(l)
        n = get_card_at_top_index(l)        
    return n

def encrypt_letter(s: str, n: int) -> str:
    """Return the encrypted version of letter s with keystream value n applied.
    >>> encrypt_letter('H', 7)
    'O'
    """
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = l.find(s)
    return l[(index + n) % 26]

def decrypt_letter(s: str, n: int) -> str:
    """Return the decrypted version of letter s with keystream value n applied.
    >>> decrypt_letter('O', 7)
    'H'
    """
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = l.find(s)
    return l[(index - n) % 26]

def process_messages(deck: List[int], message: List[str], operation: str) \
    -> List[str]:
    """Return a list of message with a list of deck of cards after operation
    applied to list of message.
    """
    new_list = []
    if operation == ENCRYPT:
        for sentence in message:
            mes = ''
            for letter in clean_message(sentence):
                n = get_next_keystream_value(deck)
                mes = mes + encrypt_letter(letter, n)
            new_list.append(mes)
    elif operation == DECRYPT:
        for sentence in message:
            mes = ''
            for letter in clean_message(sentence):
                n = get_next_keystream_value(deck)
                mes = mes + decrypt_letter(letter, n)
            new_list.append(mes)
    return new_list

def read_messages(file: TextIO) -> List[str]:
    """Return a list of messages read from file without newline character.
    """
    new_list = []
    line = file.readline()
    while line != '':
        new_list.append(line.strip())
        line = file.readline()
    return new_list

def is_valid_deck(deck: List[int]) -> bool:
    """Return whether the deck provided is a valid deck.
    
    >>> is_valid_deck([1, 2, 3, 4, 5])
    True
    >>> is_valid_deck(['a', 'b', 2, 4, 7]
    False
    """
    new_list = []
    n = len(deck)
    for card in deck:
        if type(card) != int:
            return False
        elif not 1 <= card <= n:
            return False
        elif int(card) in new_list:
            return False
        new_list.append(int(card))
    return True

def read_deck(deck: TextIO) -> List[int]:
    """Return a list of int containing all numbers from deck.
    """
    list_of_num = []
    s = deck.read()
    s1 = s.strip().split()
    for num in s1:
        list_of_num.append(int(num))
    return list_of_num
    
    
    
    
    
          




#if __name__ == '__main__':
    
    
    #import doctest
    #doctest.testmod()
