class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {char: i for i, char in enumerate(s)}
        stack = []
        used = set()

        for i, char in enumerate(s):
            if char in used:
                continue

            while (
                stack
                and char < stack[-1]
                and last_index[stack[-1]] > i
            ):
                used.remove(stack.pop())

            stack.append(char)
            used.add(char)

        return "".join(stack)
