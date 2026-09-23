class RescueCenter:
    #attr = drones, users, missions, events
    def __init__(self):
        self.drones = []
        self.missions = []
        self.users = []
        self.missions = []


    def add_drone(self,drone):
        self.drones.append(drone)

    def remove_drone(self, drone_id):
        if drone_id == Drone.drone_id:
            self.drones.remove(drone)

    def register_user(self, user):
        self.users.append(user)

    def create_mission(self):
        self.missions.append(Mission.title)

    def assign_drone_to_mission(self):
        pass

    def search_drone(self):
        pass

    def search_mission(self):
        pass

    def search_user(self):
        pass

    def generate_report(self):
        pass

    def generate_mission(self):
        pass