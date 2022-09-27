"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # We're going to be using a queue to simulate the dominoes falling left and right
        import collections

        # turn our dominoes string into a list
        dominoes = list(dominoes)

        # our queue
        queue = collections.deque()

        # Just initializing our queue with dominoes falling left or right
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                queue.append((i, dominoes[i]))

        # While we have a queue
        while queue:

            # our current index and currVal = if we're moving left or right
            currIndex, currVal = queue.popleft()

            # if we're moving left...
            if currVal == 'L':
                # Check if the left val is in our index and if the value is a standing domino
                if currIndex > 0 and dominoes[currIndex - 1] == '.':
                    # We'll change the value and add it to our queue
                    dominoes[currIndex - 1] = 'L'
                    queue.append((currIndex - 1, 'L'))

            # If we're moving to the right
            elif currVal == 'R':

                # First check if we need to make sure there isn't a domino falling to the left
                # To counteract our pushing to the right
                if currIndex + 2 in range(len(dominoes)):

                    # If it's not and the right domino is standing, change value to R
                    # Add the new domino falling right to our queue
                    if dominoes[currIndex + 2] != 'L':
                        if dominoes[currIndex + 1] == '.':
                            dominoes[currIndex + 1] = 'R'
                            queue.append((currIndex + 1, 'R'))

                    # If there is a left falling domino, we need to account for that here
                    elif dominoes[currIndex + 2] == 'L':
                        if dominoes[currIndex + 1] == '.':
                            if queue:
                                # We pop the left value since we don't need to consider it
                                queue.popleft()

                # Else, we have an edge case: 'R, .' where we just want to change the last
                # the last domino to falling right but not to add it to our queue
                elif currIndex + 1 in range(len(dominoes)):
                    if dominoes[currIndex + 1] == '.':
                        dominoes[currIndex + 1] = 'R'

        # Return the list joined as a string
        return "".join(dominoes)