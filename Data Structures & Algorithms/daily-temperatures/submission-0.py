class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:

        answer = [0] * len(temps)
        stack = []

        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i- prev
            stack.append(i)

        return answer
        