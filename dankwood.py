class PlaceParams:
    def __init__(self, area):
        self.complete = False
        self.happy = False
        self.area = area
        if area == "DankWood":
            self.hatobtained = False
