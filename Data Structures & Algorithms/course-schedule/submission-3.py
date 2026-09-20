class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        g=defaultdict(list)
        for u,v in pre:
            g[u].append(v)

        state=[0]*numCourses
        
        def helper_dfs(course):
            if state[course]==1:
                return True
            if state[course]==2:
                return False

            state[course]=1
            for i in g[course]:
                if helper_dfs(i):
                    return True
            state[course]=2
            return False 
        
        for i in range(numCourses):
            if(helper_dfs(i)):
                return False
        return True
        # s = {i: set() for i in range(numCourses)}
        # for c, p in pre: 
        #     s[c].add(p)
        
        # # Iteratively remove courses with 0 remaining prerequisites
        # while (free := [c for c, p in s.items() if not p]):
        #     for c in free: 
        #         del s[c]
        #         for p in s.values(): 
        #             p.discard(c)
            
        # return len(s) == 0