from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.following = defaultdict(set) #userId:{userIds}
        self.tweet = defaultdict(list) #userId:[tweets]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.following[userId].add(userId)
        for user in self.following[userId]:
            for tweet in self.tweet[user]:
                heap.append(tweet)
        


        heapq.heapify_max(heap)
        while heap and len(res) < 10:
            res.append(heapq.heappop_max(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, erId: int, weeId: int) -> None:
        
        if weeId in self.following[erId]:
            self.following[erId].remove(weeId)
