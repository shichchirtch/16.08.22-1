class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track_lines = []

    def add_track(self, track):
        self.track_lines.append(track)

    def get_tracks(self):
        return tuple(self.track_lines)

    def __len__(self):
        ans = 0
        x1, y1 = self.start_x, self.start_y
        for obj in self.track_lines:
            x2, y2 = obj.to_x, obj.to_y
            ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            x1, y1 = x2, y2
        return int(ans)

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)

s = Track(1,2)
print(s.start_x)
 for obj in self.track_lines:
            x2, y2 = obj.to_x, obj.to_y
            ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            x1, y1 = x2, y2
