from abc import ABC, abstractmethod

class User(ABC):
    # attr = user_id , name , username, password

    def login(self):
        pass

    def deactivate(self):
        pass


class Operator(User):
    # attr = missions_created

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

