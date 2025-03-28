"""
Assignment 7: Hash Map
Stanley He
"""
from hashqp import *


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, KeyValuePair):
            return self.key == other.key
        else:
            return self.key == other

    def __hash__(self):
        return hash(self.key)


class HashMap:
    def __init__(self):
        self.hash_table = HashQP()

    def __getitem__(self, key):
        kv_item = self.hash_table.find(key)
        return kv_item.value

    def __setitem__(self, key, value):
        kv_item = KeyValuePair(key, value)
        try:
            self.hash_table.remove(kv_item)
        except KeyError:
            pass
        self.hash_table.insert(kv_item)

    # def __setitem__(self, key, value):
    #     kv_item = KeyValuePair(key, value)
    #     try:
    #         item = self.hash_table.find(key)
    #         item.value = value
    #     except KeyError:
    #         self.hash_table.insert(kv_item)

    def __iter__(self):
        for kv_item in self.hash_table:
            yield kv_item.key

    def __eq__(self, other):
        if not isinstance(other, HashMap):
            return False
        if len(self.hash_table) != len(other.hash_table):
            return False
        for kv_item in self.hash_table:
            try:
                if other[kv_item.key] != kv_item.value:
                    return False
            except KeyError:
                return False
        return True

    def __str__(self):
        return f"({self.key}: {self.value})"

