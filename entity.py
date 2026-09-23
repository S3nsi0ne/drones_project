from project_enums import SearchAreaSize


class Equipment:
    #attr = title, weight, category
    def __init__(self, title, weight: int, category):
        self.title = title
        self.weight = weight
        self.category = category

    def is_heavy(self):
        return self.weight > 30

    def __str__(self):
        return f"title = {self.title}, weight = {self.weight}, category = {self.category}"

class SearchArea:
    #attr = size, location
    def __init__(self, size:SearchAreaSize, location:str):
        self.size = size
        self.location = location
    def calculate_battery_consumption(self):
        pass
    #ask from mentor how can i handle this method
    #i know if self.size == SearchAreaSize.SMALL --> battery drone -10


class MedicalPackage:
    #attr = type, sensitivity
    pass

class Event:
    #attr = event_id, date, description, related_object

    def create_log(self):
        pass
