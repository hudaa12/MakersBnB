
class Space:
    def __init__(self,id, name, description, price, avail_from, avail_to, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.avail_from = avail_from
        self.avail_to = avail_to
        self.user_id = user_id

    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f""