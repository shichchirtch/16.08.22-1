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

    def get_lenth(self, i):
        return (((self.arr[i - 1].to_x - self.arr[i].to_x) ** 2 + (
                    self.arr[i - 1].to_y - self.arr[i].to_y) ** 2) ** 0.5)

    def __len__(self):
        len_1 = ((self.start_x - self.arr[0].to_x) ** 2 + (self.start_y - self.arr[0].to_y) ** 2) ** 0.5
        s = 0
        for i in range(1, len(self.arr)):
            x = self.get_lenth(i)
            s += x
        return int(len_1 + s)

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
