"""
CS3C assignment #7, HashMap (HashQP)
Copyright 2021 Zibin Yang
Instructor's solution for HashQP
"""


from enum import Enum
from prime import *


class Bucket:
    class State(Enum):
        EMPTY = 0
        ACTIVE = 1
        DELETED = 2

    def __init__(self, item=None):
        self._item = item
        if item is None:
            self._state = self.State.EMPTY
        else:
            self._state = self.State.ACTIVE

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    def __str__(self):
        if self.state is Bucket.State.ACTIVE:
            return str(self.item)
        else:
            return f"<{self.state}>"

    def __repr__(self):
        return str(self)


class HashQP:
    INIT_TABLE_SIZE = 97
    INIT_MAX_LAMBDA = 0.49  # Can be 0.5, but doesn't hurt to be safe...

    def __init__(self, table_size=INIT_TABLE_SIZE):
        if not is_prime(table_size):
            table_size = next_prime(table_size)
        self._nbuckets = table_size

        self._ncollisions = 0

        self._max_lambda = self.INIT_MAX_LAMBDA
        self._clear()

    def _clear(self):
        self._buckets = [Bucket() for _ in range(self._nbuckets)]
        self._nitems = 0
        self._noccupied = 0  # non-EMPTY

    @property
    def size(self):
        return self._nitems

    def __len__(self):
        return self._nitems

    @property
    def max_lambda(self):
        return self._max_lambda

    def __str__(self):
        return f"{self.__class__.__name__}: nitems={self.size}," \
               f" noccupied={self._noccupied}, nbuckets={self._nbuckets}," \
               f" max_lambda={self.max_lambda}, ncollisions={self._ncollisions}"

    def __repr__(self):
        return f"{self}\nbuckets={self._buckets}"

    def _hash(self, item):
        return hash(item) % self._nbuckets

    def _iter_index_slow(self, key):
        h = self._hash(key)
        k = 0
        while k < self._nbuckets:
            yield (h + k * k) % self._nbuckets
            k += 1
        raise ValueError(f"Probed {k} indices when searching for {key}, too many.")

    # This method yields the same index as _iter_index_slow(), but is faster.
    # It's based on the following observation:
    # hash_index = hash(value)
    # index = hash_index
    # index = hash_index + 1
    # index = hash_index + 4
    # index = hash_index + 9
    # index = hash_index + 16
    # ... same as ...
    # index = hash_index
    # index = hash_index + 0 + 1
    # index = hash_index + 1 + 3
    # index = hash_index + 4 + 5
    # index = hash_index + 9 + 7
    # ... same as ...
    # index = hash_index
    # index = index + 1
    # index = index + 3
    # index = index + 5
    # index = index + 7
    def _iter_index(self, key):
        bucket_index = self._hash(key)
        count = 0

        k = 1
        while count < self._nbuckets:
            # The probing sequence should not be longer than the number of
            # buckets in the hash table.
            yield bucket_index
            self._ncollisions += 1
            bucket_index += k
            bucket_index %= self._nbuckets
            k += 2
            count += 1

        # This is a safe guard against probing forever; shouldn't happen
        # unless there's a bug.
        raise ValueError(f"Probed {count} indices when searching for {key}, too many.")

    def insert(self, item):
        for bucket_index in self._iter_index(item):
            bucket = self._buckets[bucket_index]
            # For insert(), we want to find an EMPTY bucket.
            if bucket.state == Bucket.State.ACTIVE and bucket.item == item:
                raise ValueError(f"{item} already exists")
            elif bucket.state == Bucket.State.EMPTY:
                bucket.state = Bucket.State.ACTIVE
                bucket.item = item
                self._nitems += 1
                self._noccupied += 1
                self._rehash_as_needed()
                break

    def _rehash_as_needed(self):
        # We must use ._noccupied to calculate the load factor, because the
        # number of empty buckets must be more than active/deleted (another way
        # of saying load factor must be < 0.5), otherwise when looking for a
        # non-existent key, find()/__contains__() may loop forever and not hit
        # an empty bucket
        if self._noccupied / self._nbuckets >= self.max_lambda:
            self._rehash()

    def _rehash(self):
        buckets = self._buckets

        # print(f"{self}; going from table_size={self._table_size} to ", end="")
        self._nbuckets = next_prime(self._nbuckets * 2)
        # print(f"{self._table_size}")
        self._clear()

        for bucket in buckets:
            if bucket.state == Bucket.State.ACTIVE:
                self.insert(bucket.item)

    # for __contains__(), we want to find ACTIVE and ==item
    def __contains__(self, key):
        for bucket_index in self._iter_index(key):
            bucket = self._buckets[bucket_index]
            if bucket.state == Bucket.State.ACTIVE and bucket.item == key:
                return True
            elif bucket.state == Bucket.State.EMPTY:
                return False

    def remove(self, key):
        for bucket_index in self._iter_index(key):
            bucket = self._buckets[bucket_index]
            # for remove(), we want to find ACTIVE and ==item
            if bucket.state == Bucket.State.ACTIVE and bucket.item == key:
                bucket.state = Bucket.State.DELETED
                self._nitems -= 1
                break
            elif bucket.state == Bucket.State.EMPTY:
                raise KeyError(f"{key} not found")

    ######################################################################
    # Added for assignment 7
    ######################################################################
    def find(self, key):
        for bucket_index in self._iter_index(key):
            bucket = self._buckets[bucket_index]
            # for find(), we want to find ACTIVE and ==item
            if bucket.state == Bucket.State.ACTIVE and bucket.item == key:
                return bucket.item
            elif bucket.state == Bucket.State.EMPTY:
                raise KeyError(f"{key} not found")

    def __iter__(self):
        for bucket in self._buckets:
            if bucket.state == Bucket.State.ACTIVE:
                yield bucket.item

    def __eq__(self, other):
        # It's not required that HashQP can be compared with Python set, though
        # that's nice to have.
        if not isinstance(other, HashQP):
            return False

        if len(self) != len(other):
            return False

        # For all items in self, they should be in other as well.
        # Note all() is passed a generator expression (not list comprehension),
        # and is lazy-evaluated/short-circuited, so as soon as one of them is
        # False it stops, without evaluating the rest.
        return all(item in other for item in self)