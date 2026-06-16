import bisect
from typing import List


class Router:
    def __init__(self, memoryLimit: int):
        self.packets = []
        self.seen = set()
        self.destination_to_time_stamps = {}
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # Check for duplicate
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False

        # If at limit, remove oldest packet
        if len(self.packets) == self.limit:
            self.forwardPacket()

        # Add the packet
        self.packets.append(packet)
        self.seen.add(packet)
        time_stamps = self.destination_to_time_stamps.setdefault(destination, [])
        bisect.insort(time_stamps, timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        packet = source, destination, timestamp = self.packets.pop(0)
        self.seen.remove(packet)
        self.destination_to_time_stamps[destination].remove(timestamp)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time_stamps = self.destination_to_time_stamps.get(destination, [])
        start_index = bisect.bisect_left(time_stamps, startTime)
        end_index = bisect.bisect_right(time_stamps, endTime)
        return end_index - start_index


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
