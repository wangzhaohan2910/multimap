from collections import defaultdict


class multimap(defaultdict):
    """The Multimap in Python.

    >>> issubclass(multimap, defaultdict)
    True
    """

    def __init__(self):
        """Ctor (Initializer).

        >>> multimap().default_factory
        <class 'set'>
        """
        super().__init__(set)

    def __str__(self):
        """Stringify it.

        >>> mp = multimap()
        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> ''.join(sorted(str(mp))) # This is the only way to test it.
        "         '''''''''''',,,,111222334455556666668999:::::aaabbbfffilmoooooortuzz{}"
        """
        res = "multi{"
        for k in self.keys():
            for v in self[k]:
                res += repr(k) + ": " + repr(v) + ", "
        return res[:-2] + "}"

    __repr__ = __str__

    def keys(self):
        res = set()
        for k in super().keys():
            if self.count(k) == 0:
                del self[k]
            else:
                res.add(k)
        return res

    def values(self):
        res = set()
        for k in self.keys():
            res.update(self[k])
        return res

    def items(self):
        res = set()
        for k in self.keys():
            for v in self[k]:
                res.add((k, v))
        return res

    def count(self, key):
        return len(self[key])

    def __len__(self):
        res = 0
        for k in self.keys():
            res += len(self[k])
        return res

    def insert(self, key, value):
        self[key].add(value)

    def erase(self, key, value):
        self[key].remove(value)
        if self.count(key) == 0:
            del self[key]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
