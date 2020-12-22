class Subcategory():
    def __init__(self, *, id, name, description=''):
        self.id = id
        self.name = name
        self.description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, str):
            self._id = id
        else:
            raise TypeError(f'invalid type for id: {type(id)}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError(f'invalid type for name: {type(name)}')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise TypeError(f'invalid type for description: {type(description)}')
