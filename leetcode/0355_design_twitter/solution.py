import itertools
import sqlite3
from typing import List

CREATE_POST_TABLE = """
CREATE TABLE post (
    userId INTEGER,
    tweetId INTEGER,
    stamp INTEGER,
    PRIMARY KEY (userId, tweetId, stamp)
)
"""
CREATE_FOLLOW_TABLE = """
CREATE TABLE follow (
    followerId INTEGER,
    followeeId INTEGER, 
    UNIQUE(followerId, followeeId)
)
"""

GET_FOLLOWING = """
SELECT DISTINCT followeeId FROM follow
WHERE followerId = ?
"""

GET_POSTS = """
SELECT tweetId
FROM post
WHERE userId in (%s)
ORDER BY stamp DESC
LIMIT 10
"""

INSERT_FOLLOW = """
INSERT OR IGNORE INTO follow
(followerId, followeeId) VALUES (?, ?)
"""

INSERT_POST = """
INSERT INTO post
(userId, tweetId, stamp) VALUES (?, ?, ?)
"""
UNFOLLOW = "DELETE FROM follow WHERE followerId=? AND followeeId=?"


class Twitter:
    def __init__(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute(CREATE_POST_TABLE)
        self.db.execute(CREATE_FOLLOW_TABLE)
        self.db.commit()
        self.stamps = itertools.count(1001)

    def postTweet(self, userId: int, tweetId: int) -> None:
        stamp = next(self.stamps)
        self.db.execute(INSERT_POST, (userId, tweetId, stamp))
        self.db.commit()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news
        feed. Each item in the news feed must be posted by users who the
        user followed or by the user themself. Tweets must be ordered
        from most recent to least recent.
        """
        # Get the list of people which the user follows
        userIds = [record[0] for record in self.db.execute(GET_FOLLOWING, (userId,))]
        userIds.append(userId)
        sql = GET_POSTS % ", ".join(str(uid) for uid in userIds)
        tweetIds = [record[0] for record in self.db.execute(sql)]
        return tweetIds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.db.execute(INSERT_FOLLOW, (followerId, followeeId))
        self.db.commit()

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.db.execute(UNFOLLOW, (followerId, followeeId))
        self.db.commit()
