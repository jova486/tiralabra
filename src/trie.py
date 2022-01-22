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
            for i in range(0,len(arr)-max_lenght):
                sub_arr = arr[i:(i+max_lenght)]
                self.insert(sub_arr)
                '''
                for j in range(1,max_lenght+1):
                    sub_sub_arr = sub_arr[0:j]

                    self.insert(sub_sub_arr)
                '''



    def dfs(self, node, prefix):
            """Syvyyshaku joka käy rakenteen läpi ja etsii halutut sekvenssit

            Args:
                - node: solmu josta haku alkaa
                - prefix: etsitty
            """

            if node.end:
                self.output.append((prefix+[node.note], node.counter))

            for child in node.child_nodes.values():
               self.dfs(child, prefix+[node.note])

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

            self.dfs(node, input[:-1])

            return self.output

