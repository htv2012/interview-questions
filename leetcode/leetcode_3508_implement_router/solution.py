from typing import List

SRC = 0
DEST = 1
TIME = 2


class Router:
    def __init__(self, memoryLimit: int):
        self.packets = []
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # Check for duplicate
        incoming_packet = [source, destination, timestamp]
        if incoming_packet in self.packets:
            return False

        # If at limit, remove oldest packet
        if len(self.packets) == self.limit:
            oldest_position = 0
            oldest_packet = self.packets[oldest_position]

            for i, packet in enumerate(self.packets):
                if packet[TIME] < oldest_packet[TIME]:
                    oldest_packet = packet
                    oldest_position = i

            self.packets.pop(oldest_position)

        # Add the packet
        self.packets.append(incoming_packet)
        return True

    def forwardPacket(self) -> List[int]:
        if self.packets:
            return self.packets.pop(0)
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return sum(
            int(packet[DEST] == destination and startTime <= packet[TIME] <= endTime)
            for packet in self.packets
        )


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
