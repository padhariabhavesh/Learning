"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        results = []

        adjacent_list = []
        indegrees = []

        for i in range(numCourses):
            adjacent_list.append([])
            indegrees.append(0)

        for prerequisite in prerequisites:
            adjacent_list[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1

        queue = []

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)
            results.append(course)

            for adj_course in adjacent_list[course]:
                indegrees[adj_course] -= 1

                if indegrees[adj_course] == 0:
                    queue.append(adj_course)

        if len(results) < numCourses:
            return []

        return results
