class Screen:
    def __init__(self, name, capacity, seating_plan):
        self._id = ObjectId()
        self.name = name
        self.capacity = capacity
        self.seating_plan = seating_plan

    def to_dict(self):
        return {
            "_id": str(self._id),
            "name": self.name,
            "capacity": self.capacity,
            "seating_plan": self.seating_plan
        }
