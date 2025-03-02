"""
How do we detect the end game after each step?

- When numbber of robots == 0 or == 1, there will be no more collision, or
- When all robots head the same direction
- When all left robots head left and right robots head right
"""

import collections
import logging
import re
from typing import List

logging.basicConfig(level="DEBUG")
Robot = collections.namedtuple("Robot", ["position", "health", "direction", "robot_id"])


def advance(robot: Robot):
    new_position = (1 if robot.direction == "R" else -1) + robot.position
    return robot._replace(position=new_position)


def downgrade_health(robot: Robot):
    return robot._replace(health=robot.health - 1)


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        # Sort the robots by positions to make it easier to do calculations
        # robot_id are used to keep track of the robot's order
        board = sorted(
            Robot(position, health, direction, robot_id)
            for robot_id, (position, health, direction) in enumerate(
                zip(positions, healths, directions)
            )
        )

        while True:
            newboard = []
            for robot in board:
                robot = advance(robot)
                if not newboard:
                    newboard.append(robot)
                    continue

                other: Robot = newboard.pop()
                if (
                    not (
                        robot.position + 1 == other.position
                        and robot.direction == "L"
                        and other.direction == "R"
                    )
                    and robot.position != other.position
                ):
                    # Different position, but not crossing
                    newboard.append(other)
                    newboard.append(robot)
                    continue

                # At this point, the two collide (i.e. occupying the same position)
                if robot.health > other.health:
                    newboard.append(downgrade_health(robot))
                elif robot.health < other.health:
                    newboard.append(downgrade_health(other))

            # Compile the list of directions, sorted by positions
            current_directions = "".join(robot.direction for robot in newboard)
            current_directions = re.sub(r"L+", "L", current_directions)
            current_directions = re.sub(r"R+", "R", current_directions)

            # End game reached
            if len(newboard) < 2 or current_directions in {"L", "R", "LR"}:
                # Less than 2 robot survived, or there will be no mo collision
                newboard.sort(key=lambda robot: robot.robot_id)
                return [robot.health for robot in newboard]
            board = newboard
