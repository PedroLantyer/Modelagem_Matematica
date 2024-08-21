import os

def clearScreen():
    try:
        if(os.name.upper() == "NT"):
            os.system("cls")
    except Exception as err:
        print(err)

class installmentPay:
    def __init__(self, intervalStart, intervalEnd, tolerance) -> None:
        self.intervalStart = intervalStart
        self.intervalEnd = intervalEnd
        self.tolerance = tolerance

    def setInitialValue(self, initialValue):
        self.initialValue = initialValue

    def setInstallmentValue(self, installmentValue):
        self.installmentValue = installmentValue

    def setTime(self, time):
        self.time = time

    def f(self, tax):
        return ((self.initialValue * pow(1+(tax/100.0), self.time)) - (self.installmentValue*self.time))

    def GetTax(self):
        if (self.f(self.intervalStart) + self.f(self.intervalEnd)) == 0:
            print("Fail")
            return None
        
        c = (self.intervalStart+self.intervalEnd)/2.0
        while(self.intervalEnd - self.intervalStart)/ 2.0 > self.tolerance:
            if(self.f(c) == 0):
                return c
            elif(self.f(self.intervalStart) * self.f(c) < 0):
                self.intervalEnd = c
            else:
                self.intervalStart = c
            c = (self.intervalStart+self.intervalEnd)/2.0
        
        return c

if __name__ == "__main__":
    clearScreen()

    dataObj = installmentPay(intervalStart = 0, intervalEnd = 100.0, tolerance = 0.01)
    dataObj.setInitialValue(50000)
    dataObj.setInstallmentValue(4754.28)
    dataObj.setTime(48)
    print(f"Juros: {dataObj.GetTax() : .4f} % a.m")