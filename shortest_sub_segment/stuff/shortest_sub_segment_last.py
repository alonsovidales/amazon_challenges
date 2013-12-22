#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re
import binascii
import string

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class ShortestSubSegment:
    __debug = False

    def resolve(self):
        subset_lenght = len(self.__words_crc)
        smallest_str = None

        if self.__debug:
            print self.__text_words_crc
        while subset_lenght <= len(self.__text_words_crc):
            if self.__debug:
                print "Len: %d" % subset_lenght

            print self.__text_words_crc
            for pos in range(len(self.__text_words_crc) - subset_lenght + 1):
                text_len = self.__text_words_crc[pos + subset_lenght - 1][1] - self.__text_words_crc[pos][1] + 1
                print text_len
                if smallest_str == None or text_len <= len(smallest_str):
                    subset = self.__text_words_crc[pos:pos + subset_lenght]
                    print subset

                    if sum(set([word[0] for word in subset])) == self.__words_weight:
                        smallest_str = self.__text_words[subset[0][1]:subset[0][1] + text_len]

                        if self.__debug:
                            print "FOUND :) %d - %s" % (text_len, ' '.join(self.__text_words[subset[0][1]:subset[0][1] + text_len]))

                        if len(smallest_str) == len(self.__words_crc):
                            return ' '.join(smallest_str)

            subset_lenght += 1

        if smallest_str == None:
            return "NO SUBSEGMENT FOUND"

        return ' '.join(smallest_str)

    def __init__(self, text, words):
        self.__words_crc = set(map(abs, map(binascii.crc32, map(string.lower, words))))
        self.__words_weight = sum(self.__words_crc)

        self.__text_words = re.sub('[^A-Za-z ]+', '', text).split()
        self.__text_words_crc = []

        for wordPos in range(len(self.__text_words)):
            word_crc = abs(binascii.crc32(self.__text_words[wordPos].lower()))

            if word_crc in self.__words_crc:
                self.__text_words_crc.append((word_crc, wordPos))

        if self.__debug:
            print "Words: %s" % self.__words_crc
            print "WordsCrc: %s" % self.__text_words_crc

if __name__ == "__main__":
    text = raw_input()
    words = [raw_input() for words in range(int(raw_input()))]

    print ShortestSubSegment(text, words).resolve()
