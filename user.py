from abc import ABC, abstractmethod

class User(ABC):
    # attr = user_id , name , username, password
    def __init__(self, user_id, name, username, password):
        self.user_id = user_id
        self.name = name
        self.username = username
        self._password = password
        self.is_active = True

    def login(self):
        if not self.is_active:
            raise Exception("User is not active")
        if len(self._password) < 8:
            raise Exception("Password is too short")
        print(f"user {self.username} logged in")

    def deactivate(self):
        self.is_active = False
        print(f"user {self.username} is deactivated")

    @abstractmethod
    def get_type(self):
        pass


class Operator(User):
    # attr = missions_created
    def __init__(self, user_id, name, username, password):
        super().__init__(user_id, name, username, password)
        self.mission_created = []

    def create_mission(self):
        pass

    def assign_mission(self):
        pass

    def start_mission(self):
        pass

    def view_mission(self):
        pass

    def view_drones(self):
        pass

class Admin(User):
    def add_drone(self):
        pass

    def remove_drone(self):
        pass

    def create_user(self):
        pass

    def activate_user(self):
        pass

    def deactivate_user(self):
        pass

    def send_drone_to_maintenance(self):
        pass

    def finish_repair(self):
        pass

    def generate_report(self):
        pass

