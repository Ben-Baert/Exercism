class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 31557600, 2)

    def on_mercury(self):
        return round(self.seconds / 7600544, 2)

    def on_venus(self):
        return round(self.seconds / 19414149, 2)

    def on_mars(self):
        return round(self.seconds / 59354033, 2)

    def on_jupiter(self):
        return round(self.seconds / 374355659, 2)

    def on_saturn(self):
        return round(self.seconds / 929292363, 2)

    def on_uranus(self):
        return round(self.seconds / 2651370019, 2)

    def on_neptune(self):
        return round(self.seconds / 5200418560, 2)