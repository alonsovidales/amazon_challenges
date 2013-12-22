#!/usr/bin/env python
# -*- coding: utf-8 -*- 

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class ConnectedSets:
    """
    This is a classic percolation problem, the algorithms uses an array
    of integer to represent tees, each tree will be a set of connected elements
    """
    __debug = False

    def link_nodes(self, left, right):
        """
        For two given nodes, search for the root node of each tree, after
        obtaine the two root nodes, point the right root node to the left root
        node connecting the two trees
        To represent the trees, an array is used, the root nodes are -1 and the
        value on each positions points to the position of the parent node
        """
        if self.__debug:
            print "Linking: %s - %s" % (left, right)
        root_left = (left[0] * len(self.__matrix)) + left[1]
        parent_left = self.__percolation[root_left]

        while parent_left != -1:
            root_left = parent_left
            parent_left = self.__percolation[parent_left]

        root_right = (right[0] * len(self.__matrix)) + right[1]
        parent_right = self.__percolation[root_right]
        while parent_right != -1:
            root_right = parent_right
            parent_right = self.__percolation[parent_right]

        if root_right != root_left:
            self.__percolation[root_right] = root_left
            if self.__debug:
                print "Link: %d - %d - %s" % (root_left, root_right, self.__percolation)

    def resolve(self):
        size = len(self.__matrix)

        for rowPos in range(size):
            for colPos in range(size):
                # Check left connection
                if colPos > 0:
                    if self.__matrix[rowPos][colPos - 1] == self.__matrix[rowPos][colPos]:
                        # Link pos with left
                        self.link_nodes((rowPos, colPos - 1), (rowPos, colPos))

                # Check top-right connection
                if (colPos + 1) < size and rowPos > 0:
                    if self.__matrix[rowPos - 1][colPos + 1] == self.__matrix[rowPos][colPos]:
                        # Link pos with top-left
                        self.link_nodes((rowPos - 1, colPos + 1), (rowPos, colPos))

                # Check top-left connection
                if colPos > 0 and rowPos > 0:
                    if self.__matrix[rowPos - 1][colPos - 1] == self.__matrix[rowPos][colPos]:
                        # Link pos with top-left
                        self.link_nodes((rowPos - 1, colPos - 1), (rowPos, colPos))

                # Check top connection
                if rowPos > 0:
                    if self.__matrix[rowPos - 1][colPos] == self.__matrix[rowPos][colPos]:
                        # Link pos with top
                        self.link_nodes((rowPos - 1, colPos), (rowPos, colPos))

        if self.__debug:
            print self.__percolation

        components = 0
        # Get all the root nodes of the trees (nodes with -1 as parent), and
        # check if the root node on the original matrix contains a 1
        for pos in range(len(self.__percolation)):
            if self.__percolation[pos] == -1 and self.__matrix[pos / size][pos % size] == 1:
                components += 1

        return components

    def __init__(self, matrix):
        self.__percolation = [-1] * (len(matrix) ** 2)
        self.__matrix = matrix

if __name__ == "__main__":
    for problem in range(int(raw_input())):
        matrix = []
        for row in range(int(raw_input())):
            matrix.append(map(int, raw_input().split()))

        print ConnectedSets(matrix).resolve()
