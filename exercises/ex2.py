import os
import matplotlib

def f(x):
    return (pow(x,2) + (1/x) - 5)

class problem:
    def __init__(self, intervalStart, intervalEnd, tolerance) -> None:
        self.intervalStart = intervalStart
        self.intervalEnd = intervalEnd
        self.tolerance = tolerance

    def f(self, x):
        return (pow(x,2) + (1/x) - 5)

    def getResult(self):
        if (self.f(self.intervalStart) + self.f(self.intervalEnd) == 0):
            print("Fail")
            return None

        count = 0
        
        c = (self.intervalStart+self.intervalEnd)/2.0
        while(self.intervalEnd - self.intervalStart)/ 2.0 > self.tolerance:
            if(self.f(c) == 0):
                return c
            elif(self.f(self.intervalStart) * self.f(c) < 0):
                self.intervalEnd = c
            else:
                self.intervalStart = c
            c = (self.intervalStart+self.intervalEnd)/2.0
            count += 1
        
        results = [c, count]
        return results


if __name__ == "__main__":
    problemObj = problem(intervalStart=0.0001, intervalEnd=5, tolerance=0.01)
    results = problemObj.getResult()
    print(f"Result: {results[0]: .4f}")
    print(f"Test count {results[1]}")
