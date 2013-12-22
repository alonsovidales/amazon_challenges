#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re
import collections

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
    After build this dict, we will choose the word with less occurences, in
    this case programming in order to reduce the complexity.
    For each position on this word, we will get a list of distances to the rest
    of words, to do this we will use binary search, easy and fast :)
    And from the list of distances we will get the list with a minimal range,
    this is the correct solution :)

    Complexity: O(n * log(n))
    """
    __debug = False

    def search_near_pos(self, positions, pos):
        """
        Using binary search get the nearest position on the list of position to
        the position "pos"
        """
        hi = len(positions)
        lo = 0

        while lo < hi:
            mid = (lo + hi) // 2
            midval = positions[mid]
            if midval < pos:
                lo = mid + 1
            elif midval > pos: 
                hi = mid

        distances = [(abs(positions[mid] - pos), mid)]

        if mid > 0:
            distances.append((abs(positions[mid - 1] - pos), mid - 1))

        if mid < len(positions) - 1:
            distances.append((abs(positions[mid + 1] - pos), mid + 1))

        near_pos = sorted(distances, key=lambda(x): x[0], reverse = False)[0][1]

        return positions[near_pos]

    def resolve(self):
        # If we don't have an occurence on the string for all the words, is not
        # possible to obtain a subset :'(
        if len(self.__words_pos) != len(self.__words_set):
            return "NO SUBSEGMENT FOUND"

        best_segment = (0, len(self.__text_words))
        for main_word, positions in self.__words_pos.items():
            # Gets for each word the first of the positions in order to study
            # all the possible best combinations
            pos = positions[0]
            possible_pos = [pos]
            # Compare the first position of this word to the nearest poisition
            # of the rest of words, the subsegment found will be the best
            # subsegment who includes thesmallest position of the current word
            for word, positions in self.__words_pos.items():
                if word != main_word:
                    if self.__debug:
                        print "%s - %s - Pos: %d - Nearest: %d" % (main_word, word, pos, self.search_near_pos(positions, pos))
                    possible_pos.append(self.search_near_pos(positions, pos))

            if self.__debug:
                print "Possible set: %s" % possible_pos

            # With the current subsegment, check if is better than the current
            # better subsegment, in this case get the new one
            aux_segment = (min(possible_pos), max(possible_pos))
            if aux_segment[1] - aux_segment[0] < best_segment[1] - best_segment[0]:
                best_segment = aux_segment

        return ' '.join(self.__text_words[best_segment[0]:best_segment[1] + 1])

    def __get_borders_only(self, positions):
        result = [positions[0]]

        position = 1
        last_pos = positions[0]
        added = set([0])
        while position < len(positions):
            if positions[position - 1] + 1 != positions[position]:
                if position - 1 not in added:
                    result.append(positions[position - 1])
                result.append(positions[position])

                added.add(position - 1)
                added.add(position)
                
            position += 1

        if position - 1 not in added:
            result.append(positions[position - 1])

        return result

    def __init__(self, text, words):
        # Remove special characters that shouldn't be considerer
        self.__text_words = re.sub('[^A-Za-z ]+', '', text).split()

        # Build the dicitonary of occurences, the key is the word, and the value
        # a list of positions for each word
        self.__words_pos = collections.defaultdict(list)
        self.__words_set = set(words)
	for wordPos in range(len(self.__text_words)):
            if self.__text_words[wordPos].lower() in self.__words_set:
                self.__words_pos[self.__text_words[wordPos]].append(wordPos)

        for key, value in self.__words_pos.items():
            self.__words_pos[key] = self.__get_borders_only(value)

        if self.__debug:
            print "Words: %s" % self.__text_words
            print "words by pos: %s" % self.__words_pos

if __name__ == "__main__":
    text = raw_input()
    words = [raw_input() for words in range(int(raw_input()))]

    print ShortestSubSegment(text, words).resolve()
