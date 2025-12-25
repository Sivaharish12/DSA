class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #in the stack we are going to store the temperature and the index
        for index,temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                stackTemperature, stackIndex = stack.pop()
                res[stackIndex] = index-stackIndex
            stack.append([temperature,index])
        return res