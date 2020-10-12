'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.


'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort the input array alphabetically and the create a dict from each source to destination. This is done to greedily create a minimum lexical order. This happens cause in case of JFK, SFO and JFK, ATL...we would ultimately want ATL first thuse having ATL first in the oroginal list would also help in traversing the same airport (ATL) would pop first
        # do a dfs traversal on the dict starting from JFK 
        tickets.sort(reverse=True)
        # print(tickets)
        resDict = collections.defaultdict(list)
        for src, dest in tickets:
            resDict[src].append(dest)
        # print(resDict)
        res = []
        def help(airport):
            while resDict[airport]:
                visited = resDict[airport].pop()
                # print(visited)
                help(visited)
            res.append(airport) # basically making the list backwards by going deep into the the first hand route and then popping back up to apend the airport 
        help('JFK')
        return res[::-1]