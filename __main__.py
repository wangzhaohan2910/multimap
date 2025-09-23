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

    def remove_item(self, key, value):
        """Remove a k-v item.

        >>> mp1 = multimap()
        >>> mp2 = multimap()
        >>> mp1["foo"] = {"baz", "bar", 0xcafe}
        >>> mp2["foo"] = {"baz", 0xcafe}
        >>> mp1[0xfeed] = {998244353, "baz"}
        >>> mp2[0xfeed] = {998244353, "baz"}
        
        >>> mp1.remove_item("foo", "bar")
        >>> mp1 == mp2
        True
        
        >>> mp2[0xfeed] = {998244353}
        >>> mp1.remove_item(0xfeed, "baz")
        >>> mp1 == mp2
        True
        
        >>> del mp2[0xfeed]
        >>> mp1 == mp2
        False
        
        >>> mp1.remove_item(0xfeed, 998244353)
        >>> mp1 == mp2
        True
        """
        self[key].remove(value)
        if self[key] == set():
            del self[key]

    def change_key(self, old, new):
        """Rename a key. If the key is already existed, then merge it.

        >>> mp1 = multimap()
        >>> mp2 = multimap()
        >>> mp1["foo"] = {"baz", "bar", 0xcafe}
        >>> mp2["fubar"] = {"baz", "bar", 0xcafe}
        >>> mp1[0xfeed] = {998244353, "baz"}
        >>> mp2[0xfeed] = {998244353, "baz"}

        >>> mp1.change_key("foo", "fubar")
        >>> mp1 == mp2
        True

        >>> mp1.change_key("fubar", 0xfeed)
        >>> mp2[0xfeed] = {"baz", "bar", 0xcafe}
        >>> del mp2["fubar"]
        >>> mp1 == mp2
        False

        >>> mp2[0xfeed] = {998244353, "baz"}
        >>> mp1 == mp2
        False
        
        >>> mp2[0xfeed] = {"baz", "bar", 0xcafe, 998244353}
        >>> mp1 == mp2
        True
        """
        self[new].update(self[old])
        del self[old]

    def change_item(self, key, old, new):
        self[key].remove(old)
        self[key].add(new)

    def move_value(self, value, old, new):
        self.remove_item(old, value)
        self[new].add(value)

    def have_item(self, key, value):
        return value in self[key]

    def update_key(self, key, *values):
        self[key].update(values)

    def values(self):
        v = set()
        for k in self.keys():
            v.update(self[k])
        return v

    def items(self):
        l = []
        for k in self.keys():
            for v in self[k]:
                l.append((k, v))
        return l

    
if __name__ == "__main__":
    from doctest import testmod
    testmod()
