class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegree, completionOrder = [0] * numCourses, []
        queue = deque()

        for dependentCourse, dependencyCourse in prerequisites:
            adjList[dependencyCourse].append(dependentCourse)
            inDegree[dependentCourse] += 1
        
        for course, dependencyCount in enumerate(inDegree):
            if dependencyCount == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            completionOrder.append(course)

            for nextCourse in adjList[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return completionOrder if len(completionOrder) == numCourses else []