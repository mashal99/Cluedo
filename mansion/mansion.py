class Mansion:
    def __init__(self):
        # adjacency list for each room
        self.rooms = {
            "Kitchen":        ["Dining Room", "Ballroom"],
            "Dining Room":    ["Kitchen", "Conservatory"],
            "Conservatory":   ["Dining Room", "Billiard Room", "Library"],
            "Billiard Room":  ["Conservatory", "Library", "Hall"],
            "Library":        ["Billiard Room", "Study", "Conservatory"],
            "Study":          ["Library", "Hall"],
            "Hall":           ["Study", "Billiard Room", "Lounge"],
            "Lounge":         ["Hall", "Ballroom"],
            "Ballroom":       ["Lounge", "Kitchen"],
        }

    def adjacent_rooms(self, room_name):
        return self.rooms.get(room_name, [])

    def all_rooms(self):
        return list(self.rooms.keys())