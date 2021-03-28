# 广度优先搜索算法----找芒果销售商

from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj"."peggy"]
graph["alice"] =["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
