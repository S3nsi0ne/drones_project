from abc import ABC, abstractmethod
class Drone(ABC):
    #attr = drone_id, name, battery, status, mission_count

    def can_accept(self, mission):
        pass

    def accept_mission(self, mission):
        pass

    def release_mission(self):
        pass

    def charge(self):
        pass

    def send_to_maintenance(self):
        pass

class searchDrone(Drone):
    #attr = search_capability

    def can_accept(self, mission):
        paa

    def search(self, area):
        pass

class CargoDrone(Drone):
    #attr = max_capacity

    def can_accept(self, mission):
        pass
    def carry_equipment(self):
        pass

    def send_to_maintenance(self, equipment):
        pass

class MedicalDrone(Drone):
    #attr = medical_capacity

    def can_accept(self, mission):
        pass
    def carry_medical_package(self, package):
        pass

