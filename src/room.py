# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name='', description='', n_to='', s_to='', e_to='', w_to='', items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def on_take(self, item_take):
        for item in self.items:
            if item_take.name.lower() == item.name.lower():
                self.items.remove(item_take)
                return print(f'You have picked up {item.name.capitalize()}')

    def on_drop(self, item_drop):
        self.items.append(item_drop)
        return print(f'You have dropped {item_drop.name.capitalize()}')