'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

'''


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Loop through each path
        for path in paths:
            candidate = path[1]  # Get the candidate destination city from the current path
            good = True  # Flag to determine if the candidate is the destination city
            
            # Check if the candidate city is also a starting city in other paths
            for other_path in paths:
                if other_path[0] == candidate:  # If the candidate is found as a starting city in another path
                    good = False  # Update flag to indicate it's not the destination city
                    break  # Exit the loop, as we've found the candidate is not the destination
            
            if good:
                return candidate  # If the candidate is not a starting city in any other path, it's the destination city
        
        return ""  # If no destination city found (shouldn't reach here if every path is valid)


