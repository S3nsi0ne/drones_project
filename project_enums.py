from enum import Enum
class MissionStatus(Enum):
    PENDING = 1
    ASSIGNED = 2
    IN_PROGRESS = 3
    COMPLETED = 4
    FAILED = 5
    CANCELED = 6

class DroneStatus(Enum):
    AVAILABLE = 1
    IN_MISSION = 2
    CHARGING = 3
    MAINTENANCE = 4

class SearchAreaSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class PackageSensitivity(Enum):
    LOW = 1
    SENSITIVE = 2
    CRITICAL = 3

