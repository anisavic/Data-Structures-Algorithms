class Solution:
    """
    Return whether true/false can complete all courses
    ex: [a,b] a is dependent on b so a->b, try to detect cycle

    Need to find whether cycle or not, need to go through each branch and see
    need a safe set to keep track of which nodes are safe()
    when going through dfs, start at that node, hold visited and if we encounter again, return false

    new state array state [0,1,2] unvisited, visited this pass, no cycles from this point forward

    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        #Adj-list conversion # list of lists

        adj_list = {}
        for p in prerequisites: # for every a, we append their neighbor (b)
            node = p[0]
            neighbor = p[1]
            if node not in adj_list:
                adj_list[node] = list()
            if neighbor not in adj_list:
                adj_list[neighbor] = list()
            adj_list[node].append(neighbor)
        
        state = {} #state set
        
        def dfs(node):
            #base case, visited already in the path, CYCLE!
            if state.get(node) == 1:
                return False
            if state.get(node) == 2:
                return True
            
            state[node] = 1

            #explore all neighbs
            for n in adj_list[node]:
                if dfs(n) is False:
                    return False
            
            state[node] = 2
            return True
        
        #Now to really check: check if cycle in any of the nodes:

        for node in adj_list.keys():
            if dfs(node) is False:
                return False
        return True