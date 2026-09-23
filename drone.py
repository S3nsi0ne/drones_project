from abc import ABC, abstractmethod

from entity import Equipment
from project_enums import DroneStatus, SearchAreaSize, PackageSensitivity


class Drone(ABC):
    #attr = drone_id, name, battery, status, mission_count
    def __init__(self, drone_id, name, battery):
        self.drone_id = drone_id
        self.name = name
        self.battery = battery
        self.status = DroneStatus.AVAILABLE
        self.mission_count = 0
        self.mission_history = []

    @abstractmethod
    def can_accept(self, mission):
        pass

    def accept_mission(self, mission):
        if self.status != DroneStatus.AVAILABLE:
            raise ValueError("Drone is not available")
        if self.battery < 20:
            raise ValueError("Battery is low")
        self.status = DroneStatus.AVAILABLE
        self.mission_count += 1
        self.battery -= 25

    def release_mission(self):
        pass

    def charge(self):
        self.battery = 100
        self.status = DroneStatus.AVAILABLE

    def send_to_maintenance(self):
        self.status = DroneStatus.MAINTENANCE

    def finish_repair(self):
        self.status = DroneStatus.AVAILABLE

    def get_battery_status(self):
        return self.battery

    @property
    def is_available(self):
        return self.status == DroneStatus.AVAILABLE and self.battery > 20

class SearchDrone(Drone):
    #attr = search_capability
    def __init__(self, drone_id, name, battery):
        super().__init__(drone_id, name, battery)

    def can_accept(self, mission):
        pass

    def search(self, area):
        pass



class CargoDrone(Drone):
    #attr = max_capacity
    def __init__(self, drone_id, name, battery, max_capacity):
        super().__init__(drone_id, name, battery)
        self.max_capacity = max_capacity

    def can_accept(self, mission):
        pass

    def carry_equipment(self, equipment: Equipment):
        if equipment.weight > self.max_capacity:
            raise ValueError(f"equipment {equipment.title} exceeds capacity {self.max_capacity}")
        return f"equipment{equipment.title} carried successfully"



    def send_to_maintenance(self, equipment):
        pass

class MedicalDrone(Drone):
    #attr = medical_capability
    def __init__(self, drone_id, name, battery):
        super().__init__(drone_id, name, battery)
        self.medical_capability = True

    def can_accept(self, mission):
        pass
    def carry_medical_package(self, package):
        if package.sensitivity == PackageSensitivity.CRITICAL and not self.medical_capability:
            raise ValueError("Medical drone cannot carried Critical package")
        return f"medical package{package.title} carried successfully"

