class Track:
    def __init__(self, x=0, y=0):
        self.start_x = x
        self.start_y = y
        self.arr = []

    def add_track(self, tr):
        if type(tr) == TrackLine:
            self.arr.append(tr)

    def get_tracks(self):
        return tuple(self.arr)


    def __len__(self):
        if len(self.arr) == 0:
            print("Движения нет !")
            return
        distance = 0
        x1, y1 = self.start_x, self.start_y
        for obj in self.arr:
            x2, y2 = obj.to_x, obj.to_y
            distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            x1, y1 = x2, y2
        return int(distance)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        if isinstance(to_x, (int, float)) and isinstance(to_y, (int, float)):
            self.to_x = to_x
            self.to_y = to_y
        if isinstance(max_speed, int):
            self.max_speed = max_speed


# ((x1 - x0)**2 + (y1 - y0)**2) ** 0.5

track1, track2 = Track(), Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)
print((len(track1)))
print(len(track2))
