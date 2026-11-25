class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course, visited):
            if course in visited:
                return False
            if not graph[course]:
                return True

            # visited.add(course)
            for prereq in graph[course]:
                if dfs(prereq, visited + [course]):
                    continue
                return False
            # visited.remove(course)
            graph[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i, []):
                return False
        return True
