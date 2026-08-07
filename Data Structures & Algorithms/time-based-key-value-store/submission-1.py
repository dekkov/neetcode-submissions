from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list) #key: [[timestamp, value]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage or self.storage[key][0][0] > timestamp:
            return ""
        l, r = 0, len(self.storage[key]) - 1

        while l <= r:
            m = (l+r) // 2
            time = self.storage[key][m][0]
            if time == timestamp:
                return self.storage[key][m][1]
            elif time > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return self.storage[key][r][1]
