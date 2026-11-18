from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
            self.tweets[userId].append((self.time,tweetId))
            self.time+=1   

    def getNewsFeed(self, userId: int) -> List[int]:
        total = list(self.tweets[userId])
        for user in self.following[userId]:
            if user in self.tweets:
                total += self.tweets[user]

        total.sort(reverse=True)
        return [tweetId for _, tweetId in total[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
