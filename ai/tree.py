#!/usr/bin/env python3
# tree.py
# author: Sébastien Combéfis
# version: February 28, 2016

import copy

class Tree:
    def __init__(self, value, children=[]):
        self.__value = value
        self.__children = copy.deepcopy(children)
    
    @property
    def size(self):
        result = 1
        for child in self.__children:
            result += child.size
        return result
    
    @property
    def value(self):
        return self.__value
    
    @property
    def children(self):
        return copy.deepcopy(self.__children)
    
    def addChild(self, tree):
        self.__children.append(tree)
    
    def __getitem__(self, index):
        return self.__children[index]

    def __len__(self):
        return len(self.children)
    
    def __str__(self):
        def _str(tree, level):
            result = '[{}]\n'.format(tree.__value)
            for child in tree.children:
                result += '{}|--{}'.format('   ' * level, _str(child, level + 1))
            return result
        return _str(self, 0)


if __name__ == '__main__':
    t = Tree(4, [Tree(5, [Tree(1), Tree(2)]), Tree(6)])
    print(len(t))

    for i in t:
        print(i)