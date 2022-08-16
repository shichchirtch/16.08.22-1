class Track:
    def __init__(self, x=0, y=0):
        self.start_x = x
        self.start_y = y

    def add_track(self, tr):
        pass


    def get_tracks(self):
        pass


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        if isinstance(to_x, (int, float)) and isinstance(to_y, (int, float)):
            self.to_x = to_x
            self.to_y = to_y
        if isinstance(max_speed, int):
            self.max_speed = max_speed



#((x1 - x0)**2 + (y1 - y0)**2) ** 0.5

track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
