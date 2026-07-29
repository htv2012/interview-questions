def towerBreakers(n: int, m: int) -> int:
    """
    Player 1 always plays first.

    If there is a single tower (n = 1) and that tower has height (m = 1),
    then player 1 will lose as there is no more move. However if (m > 1)
    then player 1 can always reduce the tower's height to (m = 1) and win.

    If there are 2 towers with (m = 1), then player 1 will lose since
    there is no more moves. If (m > 1) then no matter which move player
    1 did, player 2 will mirror that and win.

    If there are 3 towers with (m = 1), the player 1 will lose. If (m
    > 1), then player 1 can reduce the first tower to (m = 1) and win
    because that reduce the game to a 2 x m scenario.

    In short:
    - If (m = 1) then player 1 will lose.
    - If n even, then player 1 will lose.
    """
    return 2 if (m == 1 or n % 2 == 0) else 1
