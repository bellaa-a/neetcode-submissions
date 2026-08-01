class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets)-1, -1, -1):
            if self.tweets[i][0] == userId or self.tweets[i][0] in self.following[userId]:
                res.append(self.tweets[i][1])
            if len(res) >= 10:
                return res

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId) 
