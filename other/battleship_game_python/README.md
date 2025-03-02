# The Problem

Implement the `shoot` method in the Battleship game. Include
initialization code for the game board. This method takes in a coordinate
and return miss, hit, or sunk.

# Terminolog

The game consists of two players, each possesses two grids: one to
place their ships which usually called primary- or my-ships grid; the
other grid is to track the result of their firing called tracking-,
enermy-ships or target grid.

![](http://d33y93cfm0wb4z.cloudfront.net/ACTIVITIES_JO/Images%20resized/battleship-game-main.jpg)

# Ideas

The key to this problem is in shooting: a function which takes an
opponent's firing coordinate and return a miss, hit, or sunk. From the
current player's point of view, this method does not really "shoot" or
"fire" at the opponent, but but the opposit. Therefore, I will call this
function "assess" from now on.

To implement the assess function, I need to keep track of a few pieces
of information:

- The primary grid--the grid where I place my ships
- My ships
- Damage information for each ship (intact, partially damaged, or sunk)

After trying out various ideas, I came to the following design:

- I present coordinates as 'A1', 'C5', 'I10', ... I choose 1-based
  instead of zero based rows to be more user friendly
- Instead of creating a data structure representing a grid, I only track
  the ships positions. For example, the following respresent my patrol
  boat:

        {'A1': 2, 'A2': 2}
        
- The key in this dictionary represents the coordinates where I place a
  ship, the value is a bitmap combination: the least significant bit
  represents a hit (1) or intact (0). The first ship is represent by a
  2, the next one a 4, an 8, 16, and 32. For example, a value of 8 means
  ship #3 is occupying the grid position and still in tact. A 9 means
  ship #3 has been fired at.


