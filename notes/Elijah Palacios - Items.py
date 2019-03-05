class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self):
        super(Key, self).__init__("Key", "Can be used to unlock doors")
        