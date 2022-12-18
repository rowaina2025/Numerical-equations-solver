from unicodedata import decimal


class Commands:
    a = [[0 for x in range(100)] for y in range(100)]
    b = []
    def __init__(self):
        self.nEquations = ""
        self.method = ""
        self.LUForm = ""
        self.ARE = "0.000001"
        self.precision = "5"
        self.stopCondition = "Number of Iterations"
        self.nIterations = "2"
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"

    def setNEquations(self, n):
        self.nEquations = n

    def setMethod(self, method):
        self.method = method

    def setARE(self, ARE):
        self.ARE = ARE

    def setLUForm(self, LUForm):
        self.LUForm = LUForm

    def setPrecision(self, precision):
        self.precision = precision

    def setStopCondition(self, stopCondition):
        self.stopCondition = stopCondition

    def setNIterations(self, n):
        self.nIterations = n

    def getTitle(self):
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"
        return self.title

    # Check validity and form arrays
    def areFilled(self, a, b):
        for i in range(0, int(self.nEquations)):
            if b[i].text() == "":
                return False
            self.b.append(decimal(b[i].text()))
            for j in range(0, int(self.nEquations)):
                if self.a[i][j].text() == "":
                    return False
                self.a[i][j] = decimal(a[i][j].text())
                print(self.a[i][j].text())
            print(self.nEquations)
        return True

    #Calls the methods
    def calculate(self):
        if self.method == "Gauss Elimination":
            print("Gauss")






