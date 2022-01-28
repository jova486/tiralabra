#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
import random


class TrieNode:
    """Trie rakenteen solmua kuvaava luokka
    """

    def __init__(self, note):
        """Luokan konstruktori.
        Args:
            note: tallennettava nuotti, kokonaislukuarvo
        """

        self.note = note
        self.end = False
        self.counter = 0
        self.child_nodes = {}


class Trie(object):
    """Trie rakennetta kuvaava luokka
    """

    def __init__(self):
        """Trie rakenteen konstruktori.
           Juuri solmun arvoksi alustetaan -1
        """
        self.root = TrieNode(-1)

    def insert(self, arr):
        node = self.root
        for n in arr:
            if n in node.child_nodes:
                node = node.child_nodes[n]

            else:

                new_node = TrieNode(n)
                node.child_nodes[n] = new_node
                node = new_node

        node.end = True
        node.counter += 1

    def insert_array(self, arr, max_lenght):
        """Tallentaa Trieen pidemmän sekvenssin jaettuna pienempiin osiin
           joiden maksimipituus on annettu. Sekvenssit tallennetaan myös 1-max_lenght pituisina osiana
        Args:
            arr: tallennettava sekvenssi
            max_lenght: tallennettavien osien maksimipituus
        """
        for j in range(1, max_lenght+1):
            for i in range(0, len(arr)-j+1):

                sub_arr = arr[i:(i+j)]
                self.insert(sub_arr)

    def dfs(self, node, prefix, l):
        """Syvyyshaku joka käy rakenteen läpi ja etsii halutut sekvenssit

        Args:
            - node: solmu josta haku alkaa
            - prefix: etsitty
        """

        if node.end:
            out = prefix+[node.note]
            if len(out) == l:
                self.output.append((prefix+[node.note], node.counter))

        if len(prefix) < l:
            for child in node.child_nodes.values():

                if node.note == -1:
                    self.dfs(child, prefix, l)
                else:
                    self.dfs(child, prefix+[node.note], l)

    def query(self, input):
        """Hakee Triessä olevat sekvenssit
        Syötteelle input haetaan kaikki sitä vastaavat sekvenssit ja niiden frekvenssi
        Args:
            - input: etsitty sekvenssi
        Returns: taulukko jossa tupleina sekvenssit ja niiden frekvenssi
        """

        node = self.root
        self.output = []

        for n in input:

            if n in node.child_nodes.keys():

                node = node.child_nodes[n]

            else:

                return []

        self.dfs(node, input[:-1], (len(input)+1))

        return self.output
