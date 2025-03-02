import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que = collections.deque(senate)
        while True:
            senator = que.popleft()
            opponent = "R" if senator == "D" else "D"

            try:
                # Ban the next opponent in line
                que.remove(opponent)
            except ValueError:
                # No opponent left, declare victory
                return "Radiant" if senator == "R" else "Dire"

            # This senator goes back into the voting queue
            que.append(senator)
