from collections import defaultdict


class multimap(defaultdict):
    def __init__(self, **kwargs):
        super().__init__(set, **kwargs)

    def __str__(self):
        return "multimap(" + str(dict(self)) + ")"

    def __repr__(self):
        return str(self)

    def remove_value(self, value):
        for k in self.keys():
            self[k].discard(value)

    def remove_item(self, key, value):
        self[key].remove(value)

    def change_key(self, old, new):
        self[new].update(self[old])
        del self[old]

    def change_value(self, old, new):
        for k in self.keys():
            if old in self[k]:
                self[k].remove(old)
                self[k].add(new)

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
        v = []
        for k in self.keys():
            v.extend(self[k])
        return v
