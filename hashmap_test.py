"""
Assignment 7 Test
Stanley He
"""
import unittest
from hashmap import HashMap
from ebook import *
import random


class HashMapTestCase(unittest.TestCase):
    def testInit(self):
        pass

    def testSetandGetItem(self):
        hashmap = HashMap()
        hashmap[2] = "bat"
        hashmap[9] = "barn"
        hashmap[3] = "car"
        self.assertEqual("bat", hashmap[2])
        self.assertEqual("barn", hashmap[9])
        self.assertEqual("car", hashmap[3])

    def testGetFailure(self):
        hashmap = HashMap()
        hashmap[2] = "bat"
        hashmap[9] = "barn"
        hashmap[3] = "car"
        with self.assertRaises(KeyError):
            print(hashmap[5])

    def testSetItem(self):
        hashmap = HashMap()
        hashmap[1000] = 1
        hashmap[1000] = 2
        hashmap[2000] = 2
        hashmap[-4] = 2
        self.assertEqual(2, hashmap[1000])
        self.assertEqual(2, hashmap[2000])
        self.assertEqual(2, hashmap[-4])

    def testIter(self):
        hashmap = HashMap()
        keys = [2, 9, 3, 8, 1]
        for key in keys:
            hashmap[key] = random.randint(1, 100)
        self.assertEqual(sorted(keys), [o for o in hashmap])

    def testEq(self):
        hashmap1 = HashMap()
        hashmap1[2] = "bat"
        hashmap1[9] = "beer"
        hashmap1[3] = "car"
        hashmap2 = HashMap()
        hashmap2[2] = "bat"
        hashmap2[9] = "beer"
        hashmap2[3] = "car"
        self.assertTrue(hashmap1 == hashmap2)

    def testGutenburg(self):
        hashmap = HashMap()
        my_books = eBookEntryReader("catalog-short4.txt")
        for book in my_books:
            hashmap[book.id] = book
        print("24743: Daudet, Alphonse, 1840-1897 -> Les rois en exil. Finnish (Paris (France) -- Fiction)")
        print(hashmap[24743])
        print("24749: Reynolds, Mack, 1917-1983 -> Adaptation (Science fiction, American)")
        print(hashmap[24749])
        print("24751: Walton, Amy, 1848-1899 -> The Kitchen Cat and Other Stories (Short stories)")
        print(hashmap[24751])

    def testGutenburg2(self):
        hashmap = HashMap()
        my_books = eBookEntryReader("catalog-short4.txt")
        for book in my_books:
            tuple = (book.author, book.title)
            hashmap[tuple] = book
        print("24742: Stephens, James, 1882-1950 -> Mary, Mary (Mothers and daughters -- Fiction)")
        print(hashmap[("Stephens, James, 1882-1950", "Mary, Mary")])
        print("24743: Daudet, Alphonse, 1840-1897 -> Les rois en exil. Finnish (Paris (France) -- Fiction)")
        print(hashmap[("Daudet, Alphonse, 1840-1897", "Les rois en exil. Finnish")])
        print("24749: Reynolds, Mack, 1917-1983 -> Adaptation (Science fiction, American)")
        print(hashmap[("Reynolds, Mack, 1917-1983", "Adaptation")])