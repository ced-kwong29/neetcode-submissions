class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for prereq in graph[course]:
                if dfs(prereq):
                    continue
                return False

            graph[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
