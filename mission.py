from project_enums import MissionStatus
from project_enums import DroneStatus
from drone import Drone

class Mission:
    #attr = mission_id, title, priority, creator, assigned_drone, status
    def __init__(self, mission_id, title, priority, creator, assigned_drone:Drone = None, status= MissionStatus.value):
        self.mission_id = mission_id
        self.title = title
        self.priority = priority
        self.creator = creator
        self.assigned_drone = assigned_drone
        self.status = status

    def assign_drone(self, drone):
        if self.status != MissionStatus.PENDING:
            raise ValueError(f"mission {self.mission_id} assigned a drone")
        if drone.battery < 20:
            raise ValueError("battery less than 20")

        self.assigned_drone = drone
        drone.status = DroneStatus.IN_MISSION
        drone.mission_count += 1
        drone.mission_history.append(self.mission_id, self.status)
        self.status = DroneStatus.IN_MISSION


    def start(self):
        self.status = MissionStatus.IN_PROGRESS

    def complete(self):
        self.status = MissionStatus.COMPLETED


    def fail(self):
        self.status = MissionStatus.FAILED

    def cancel(self):
        self.status = MissionStatus.CANCELLED
