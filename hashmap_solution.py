"""
CS3C assignment #7, HashMap
Copyright 2023 Zibin Yang (11/15/2024)
Instructor's solution for HashMap
"""
from hashqp import *


class HashMap:
    """Data structure that maps keys to values, much like Python's dict."""

    class MapEntry:
        """
        This class stores a key-value pair that represents an entry in HashMap
        """
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if isinstance(other, HashMap.MapEntry):
                # other is MapEntry, so compare the .key attribute.
                # HashQP.insert() goes through this comparison.
                return self.key == other.key
            else:
                # Compare .key to other, assuming other is key.
                # HashQP.find() goes through this comparison.
                return self.key == other

            # Intriguingly, this one line works almost the same as the above,
            # in many cases. For builtin types like int/str, when compared
            # with types it doesn't know how to compare, those types returns
            # NotImplemented, and Python interpreter will then flip the equality
            # test, i.e. other == self.key, or other.__eq__(self.key). So if
            # other is MapEntry, it'll then compare other.key to self.key,
            # which is what we want.
            #
            # The case in which the following line doesn't work is on self.key
            # that doesn't return NotImplemented when compared with types it
            # doesn't know how to handle, for example
            # HashMapTestCase.testEqUserType.UserType.
            #
            # return self.key == other

        def __hash__(self):
            """Hash key only."""
            return hash(self.key)

        def __str__(self):
            return f"key={self.key}, value={self.value}"

    def __init__(self):
        # Internally this uses an instance of HashQP
        self._hashtable = HashQP()

    def __getitem__(self, key):
        """Given key, returns value associated with the key."""
        # HashQP.find(key) compares the stored MapEntry with key through
        # MapEntry.__eq__()'s "self.key == other" code path.
        return self._hashtable.find(key).value

    def __setitem__(self, key, value):
        """Given key-value pair, store them."""
        try:
            # See if key's already in table, if so, update value.
            self._hashtable.find(key).value = value
        except KeyError:
            # If not already in, insert the key-value pair.
            # HashQP.insert() compares the stored MapEntry with the new
            # MapEntry through MapEntry.__eq__()'s "self.key == other.key"
            # code path.
            self._hashtable.insert(HashMap.MapEntry(key, value))

    def __len__(self):
        return len(self._hashtable)

    def __iter__(self):
        """Iterate over all the keys in HashMap"""
        for entry in self._hashtable:
            yield entry.key

    def __eq__(self, other):
        if not isinstance(other, HashMap):
            return False

        # Check if the two contain the same keys (HashQP.__eq__()
        # makes sure both HashMap contains the same MapEntry's as
        # compared by their .key attributes)
        if self._hashtable != other._hashtable:
            return False

        # Check if each key maps to the same value.
        return all(self[key] == other[key] for key in self)