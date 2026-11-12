class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > stack[-1][0]:
                temperature_prev = stack.pop()
                output[temperature_prev[1]] = idx-temperature_prev[1]
            stack.append((temperatures[idx],idx))
            

        return output
                

