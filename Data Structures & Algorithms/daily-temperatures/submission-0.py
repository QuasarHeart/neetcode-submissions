class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[idx],idx))
            
            while temperatures[idx] > stack[-1][0]:
                temperature_prev = stack.pop()
                output[temperature_prev[1]] = idx-temperature_prev[1]
                if not stack:
                    break
            stack.append((temperatures[idx],idx))
            

        return output
                

