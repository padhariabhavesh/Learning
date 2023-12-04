


'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.

 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""  # Initialize an empty string to store the result
        empty = ""  # Initialize an empty string for a special case
        temp = 0  # Initialize a variable to store the largest digit found
        check = True  # Initialize a flag to check for a specific condition

        # Loop through the string to find the largest digit occurring thrice consecutively
        for i in range(len(num) - 2):
            # Check if the current digit is the same as the next two digits
            if i + 2 < len(num) and num[i] == num[i + 1] == num[i + 2]:
                # Convert the character digit to its integer equivalent and update 'temp'
                temp = max(temp, int(num[i]))
                check = False  # Update the flag to indicate the condition was met

        # If the condition was met (i.e., a triplet was found)
        if not check:
            # Append the largest digit found three times to the 'ans' string
            ans += str(temp) * 3

        else:  # If no such triplet found
            return empty  # Return the empty string

        return ans  # Return the result containing the largest good integer

