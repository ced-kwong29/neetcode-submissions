class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites.sort(key= lambda p: p[0])

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not graph[course]:
                return True

            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True