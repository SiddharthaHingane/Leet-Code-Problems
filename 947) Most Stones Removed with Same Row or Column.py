class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # create a completed graph, use graphX to store the node with same x axis and use graphY to store  the node with the same y axis
        # Use BFS
        # Use visited to store the passed node
        # for one conneted graph count the (node number -1), and let it be ni
        # At the end, add all the ni in each connected graphs
        # Time: O(V+E) Space:O(V+E)
        
        
        hmapX = defaultdict(list)
        hmapY = defaultdict(list)
        for st in stones:
            hmapX[st[0]].append(tuple(st))
            hmapY[st[1]].append(tuple(st))
        
        visited = set()
        
        count = 0 
        for st in stones:
            if tuple(st) not in visited:
                queue =deque([tuple(st)])
                while queue:
                    curr = queue.popleft()
                    count += 1
                    visited.add(curr)
                    for nei in hmapX[curr[0]]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                    for nei in hmapY[curr[1]]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                count -= 1
        return count
