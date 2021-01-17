class AStarNode:

    def __init__(self, node, previous, cost, id):
        self.node = node
        self.id = id
        self.previous = previous
        self.time = 0
        self.left_cost = 0  # Left turns cost
        self.cost = cost  # Total cost


    def __eq__(self, other):
        return self.id == other.id


    def __lt__(self, other):
        return self.id < other.id


    def __le__(self, other):
        return self.id <= other.id


    def __gt__(self, other):
        return self.id > other.id