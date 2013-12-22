#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re
import binascii
import string

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class ShortestSubSegment:
    """
    This is a solution based on hashing, I obtain a integer value for each word,
    and check all the possible subsets, is the sum of all the integer values is
    the same than the sum for all the words, is high probable that this sub set
    contain the given words.
    This kind of comparation is really fast, and have a complexity of O(n)
    where n are the number of words.
    """
    __debug = False

    def resolve(self):
        # Get a list with only words from the words list
        filtered = []
        word_positions = []
        last_word = 0
        for word_pos in range(len(self.__textWords)):
            if self.__textWords[word_pos].lower() in self.__words:
                word = binascii.crc32(self.__textWords[word_pos].lower())
                if last_word != word:
                    last_word = word
                    filtered.append(word)
                    word_positions.append(word_pos)

        if self.__debug:
            print "Filtered: %s" % filtered
            print "Word Pos: %s" % word_positions

        smallest = len(self.__textWords)
        sub_set = False
        # Check the sum of all the words of the sub sets
        for subset_pos in range(len(filtered) - len(self.__words) + 1):
            crc_subset_words = set(filtered[subset_pos:subset_pos + len(self.__words)])

            extra_words = 0
            while len(crc_subset_words) != len(self.__words) and subset_pos + len(self.__words) + extra_words < len(filtered):
                if self.__debug:
                    print "Extra %d - %s" % (subset_pos + len(self.__words) + extra_words, filtered[subset_pos + len(self.__words) + extra_words])
                crc_subset_words.add(filtered[subset_pos + len(self.__words) + extra_words])
                extra_words += 1

            if self.__debug:
                print "Ended: %s" % crc_subset_words

            if sum(crc_subset_words) == self.__wordsWeight:
                first = word_positions[subset_pos]
                last = word_positions[subset_pos + len(self.__words) + extra_words - 1]
                lenght = last - first + 1
                if lenght < smallest:
                    smallest = lenght
                    if self.__debug:
                        print "First: %d - %d - Diff: %d" % (first, last, lenght)

                    sub_set = self.__textWords[first:first + lenght]

                    # Well is pretty sure that we have found the subset, but is
                    # better check it words by word in order to avoid false positives
                    found = True
                    for wordPos in range(len(sub_set)):
                        if sub_set[wordPos].lower() not in self.__words:
                            found = False

                    if found and len(sub_set) == len(self.__words):
                        return ' '.join(sub_set)

        if not sub_set:
            return "NO SUBSEGMENT FOUND"

        return ' '.join(sub_set)

    def __init__(self, text, words):
        self.__textWords = re.sub('[^A-Za-z ]+', '', text).split()
        self.__textWordsCrc = map(binascii.crc32, map(string.lower,self.__textWords))
        self.__words = set(map(string.lower, words))
        self.__wordsWeight = sum(map(binascii.crc32, map(string.lower, words)))

        if self.__debug:
            print "Text Words: %s" % self.__textWords
            print "Text Words Crc: %s" % self.__textWordsCrc
            print "Words: %s" % self.__words_crc
            print "Words Weight: %s" % self.__wordsWeight

if __name__ == "__main__":
    text = raw_input()
    words = [raw_input() for words in range(int(raw_input()))]

    print ShortestSubSegment(text, words).resolve()
