"""Checker for CSC108 Assignment 2"""

import sys

sys.path.insert(0, './pyta')


print("================= Start: checking coding style =================")

import python_ta
python_ta.check_all('cipher_functions.py', config='pyta/a2_pyta.txt')

print("================= End: checking coding style =================\n")


print("================= Start: checking parameter and return types =================")

import builtins
import copy

# Check for use of functions print and input.
our_print = print
our_input = input

def disable_print(*_args, **_kwargs):
    """ Notices if print is called """
    raise Exception("You must not call built-in function print!")


def disable_input(*_args, **_kwargs):
    """ Notices if input is called """
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input

import cipher_functions

sample_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
               18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]

# typecheck the cipher_functions.py functions

# Type check cipher_functions.clean_message
result = cipher_functions.clean_message('abc')
assert isinstance(result, str), \
       '''clean_message should return a str, but returned {0}''' \
       .format(type(result))


# Type check cipher_functions.encrypt_letter
result = cipher_functions.encrypt_letter('A', 1)
assert isinstance(result, str) and len(result) == 1, \
       '''encrypt_letter should return a single character, but returned {0}''' \
       .format(type(result))


# Type check cipher_functions.decrypt_letter
result = cipher_functions.decrypt_letter('B', 1)
assert isinstance(result, str) and len(result) == 1, \
       '''decrypt_letter should return a single character, but returned {0}''' \
       .format(type(result))


# Type check cipher_functions.swap_cards
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.swap_cards(sample_deck, 1)
assert result is None, \
       '''swap_cards should return None, but returned {0}''' \
       .format(type(result))
assert deck_copy != sample_deck, \
       '''swap_cards should mutate the deck, but did not'''


# Type check cipher_functions.get_small_joker_value
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.get_small_joker_value(sample_deck)
assert isinstance(result, int), \
       '''get_small_joker_value should return int, but returned {0}''' \
       .format(type(result))
assert deck_copy == sample_deck, \
       '''get_small_joker_value should NOT mutate the deck, but it did'''


# Type check cipher_functions.get_big_joker_value
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.get_big_joker_value(sample_deck)
assert isinstance(result, int), \
       '''get_big_joker_value should return int, but returned {0}''' \
       .format(type(result))
assert deck_copy == sample_deck, \
       '''get_big_joker_value should NOT mutate the deck, but it did'''


# Type check cipher_functions.move_small_joker
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.move_small_joker(sample_deck)
assert result is None, \
       '''move_small_joker should return None, but returned {0}''' \
       .format(type(result))
assert deck_copy != sample_deck, \
       '''move_small_joker should mutate the deck, but did not'''


# Type check cipher_functions.move_big_joker
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.move_big_joker(sample_deck)
assert result is None, \
       '''move_big_joker should return None, but returned {0}''' \
       .format(type(result))   
assert deck_copy != sample_deck, \
       '''move_big_joker should mutate the deck, but did not'''


# Type check cipher_functions.triple_cut
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.triple_cut(sample_deck)
assert result is None, \
       '''triple_cut should return None, but returned {0}''' \
       .format(type(result))
assert deck_copy != sample_deck, \
       '''triple_cut should mutate the deck, but did not'''


# Type check cipher_functions.insert_top_to_bottom
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.insert_top_to_bottom(sample_deck)
assert result is None, \
       '''insert_top_to_bottom should return None, but returned {0}''' \
       .format(type(result))
assert deck_copy != sample_deck, \
       '''insert_top_to_bottom should mutate the deck, but did not'''


# Type check cipher_functions.get_card_at_top_index
deck_copy = copy.deepcopy(sample_deck)
result = cipher_functions.get_card_at_top_index(sample_deck)
assert isinstance(result, int), \
       '''get_card_at_top_index should return an int, but returned {0}''' \
       .format(type(result))
assert deck_copy == sample_deck, \
       '''get_card_at_top_index should NOT mutate the deck, but it did'''


# Type check cipher_functions.get_next_keystream_value
result = cipher_functions.get_next_keystream_value(sample_deck)
assert isinstance(result, int), \
       '''get_next_keystream_value should return an int, but returned {0}''' \
       .format(type(result))


# Type check cipher_functions.process_messages
result = cipher_functions.process_messages(sample_deck, ['A', 'B', 'C'], 'd')
assert isinstance(result, list), \
       '''process_messages should return a list, but returned {0}''' \
       .format(type(result))   
for item in result: 
    assert isinstance(item, str), \
           '''process_messages should return a list of str, but returned a list of {0}'''\
           .format(type(item)) 


# Type check cipher_functions.read_messages
try:
    message_file = open('secret1.txt')
except FileNotFoundError:
    assert False, \
           '''make sure secret1.txt is in the same folder as the checker'''
result = cipher_functions.read_messages(message_file)
assert isinstance(result, list), \
       '''read_messages should return a list, but returned {0}''' \
       .format(type(result))
for item in result:
    assert isinstance(item, str), \
           '''read_messages should return a list of str, but returned a list of {0}'''\
           .format(type(item))
assert not message_file.closed, \
       '''read_messages should not close the file'''
message_file.close()


# Type check cipher_functions.is_valid_deck
possible_deck = [1, 2, 3]
deck_copy = copy.deepcopy(possible_deck)
result = cipher_functions.is_valid_deck(possible_deck)
assert isinstance(result, bool), \
       '''is_valid_deck should return a bool, but returned {0}''' \
       .format(type(result))
assert possible_deck == deck_copy, \
       '''is_vaild_deck should not mutate the list'''


# Type check cipher_functions.read_deck
try:
    deck_file = open('deck1.txt')
except FileNotFoundError:
    assert False, \
           '''make sure deck1.txt is in the same folder as the checker'''
result = cipher_functions.read_deck(deck_file)
assert isinstance(result, list), \
       '''read_deck should return a list, but returned {0}''' \
       .format(type(result))
for item in result:
    assert isinstance(item, int), \
           '''read_deck should return a list of int, but returned a list of {0}'''\
           .format(type(item))
assert not deck_file.closed, \
       '''read_deck should not close the file'''
deck_file.close()


builtins.print = our_print
builtins.input = our_input

print("================= End: checking parameter and return types =================\n")

print("The parameter and return type checker passed.")
print("This means we will be able to test your code.")
print("It does NOT mean your code is necessarily correct.")
print("You should run your own thorough tests to convince yourself your code is correct.")
print()
print("Scroll up to review the output of checking coding style.")
