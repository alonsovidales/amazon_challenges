#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re
import collections
import sys
sys.setrecursionlimit(100000)

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class ShortestSubSegment:
    """
    This solution is really simple, first of all creates a dictionary with all
    the positions for each word, for example for the string:
        This is a test. This is a programming test. This is a programming test
        in any language.
    And the words:
        this
        a
        test
        programming

    We will obtian a dictionary like:
        'This': [0, 4, 9],
        'a': [2, 6, 11],
        'test': [3, 8, 13],
        'programming': [7, 12]

    For example, this occurs in the position 0, 4, and 9
    After build this dict, we sort the occurences by size, in order to decrease
    the recursion.
    With the positions sorted, search by deep the sortest way :)
    """
    __debug = False

    def __search_by_deep(self, values, words = []):
        # Check if this way if worst than a previous one yet selected
        if len(words) > 0:
            used_size = max(words) - min(words)
            if used_size >= self.__min_words:
                return

        if len(values) == 0:
            # We have all the words, check if this way is better or not than the
            # previous roads
            if used_size < self.__min_words:
                self.__min_words = used_size
                self.__range = (min(words), max(words))
            return

        # Search by deep all the possible combinations
        deep_values = values[1:]
        for position in values[0]:
            new_words = words[:]
            new_words.append(position)
            self.__search_by_deep(deep_values, new_words)

    def resolve(self):
        # If we don't have an occurence on the string for all the words, is not
        # possible to obtain a subset :'(
        if len(self.__words_pos) != len(self.__words_set):
            return "NO SUBSEGMENT FOUND"

        # Sort the words by positions in order to improbe the search
        values = sorted(self.__words_pos.values(), key=lambda(x): len(x))

        self.__search_by_deep(values)

        return ' '.join(self.__text_words[self.__range[0]:self.__range[1] + 1])

    def __init__(self, text, words):
        # Remove special characters that shouldn't be considerer
        self.__text_words = re.sub('[^A-Za-z ]+', '', text).split()

        # Build the dicitonary of occurences, the key is the word, and the value
        # a list of positions for each word
        self.__words_pos = collections.defaultdict(list)
        self.__words_set = set(words)
        self.__min_words = len(self.__text_words)
	for wordPos in range(len(self.__text_words)):
            if self.__text_words[wordPos].lower() in self.__words_set:
                self.__words_pos[self.__text_words[wordPos]].append(wordPos)

        if self.__debug:
            print "Words: %s" % self.__text_words
            print "words by pos: %s" % self.__words_pos

if __name__ == "__main__":
    text = raw_input()
    words = [raw_input() for words in range(int(raw_input()))]

    print ShortestSubSegment(text, words).resolve()
