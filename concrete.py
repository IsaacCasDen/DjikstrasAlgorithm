
class Node:
    def __init__(self, id):
        self.id = id

    def __eq__(self, value):
        if value == self.id:
            return True
        
        if not isinstance(value,self.__class__):
            return False
        
        if self.id == value.id:
            return True
        
        return False
    
    def __hash__(self):
        return hash(self.id)
    
    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return self.__str__()

class Edge:
    def __init__(self, from_id, to_id, weight):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = float(weight)
    
    def __eq__(self, value):
        if not isinstance(value,self.__class__):
            return False
        
        if value.from_id == self.from_id and value.to_id == self.to_id:
            return True
        
        return False
    
    def __hash__(self):
        return hash((self.from_id),self.to_id,self.weight)
        
    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        value = \
            "From: " + str(self.from_id) + \
                " To: " + str(self.to_id) + \
                    " Weight: " + str(self.weight)
        return value
    
    def __repr__(self):
        return self.__str__()
    
class Hop:
    def __init__(self, prev, distance):
        self.prev = prev
        self.distance = distance
    
    def __str__(self):
        return "Prev: " + str(self.prev) + " Total Distance: " + str(self.distance)

    def __repr__(self):
        return self.__str__()