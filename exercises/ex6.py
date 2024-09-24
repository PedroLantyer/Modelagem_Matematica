"""
Uma editora publica um best-seller em 3 apresentaçõa diferentes:
brochura, clube do livro e deluxe.
Cada brochura leva 1 minuto para costurar e 2 minutos para colar
Cada clube do livro leva 2 minuto para costurar e 4 minutos para colar
Cada deluxe leva 3 minuto para costurar e 5 minutos para colar
Se a maquina de costurar fica disponível por 6h/dia e a de colar por 11h/dia
Quantos livros de cada tipo podem ser produzidos de tal maneira que as maquinas sejam aproveitadas ao máximo
e a quantidade de livros do clube do livro seja metade da quantidade de livros brochura
"""

"""
1*B + 2*C + 3*D = 360
2*B + 4*C + 5*D = 660
B = (C/2)


5*X_1 + 3*X_2 = 360
10*X_1 + 5*X_2 = 660
"""

from decimal import *
import os

def clearScreen():
    if os.name.upper() == "NT":
        os.system("cls")

def printMatrix(matrix: list, lineSize=35, lineBreakAfter = True):
    try:
        strArr = []
        for i in range(len(matrix)):
            lineStr = "| "
            for j in range(len(matrix[i])):
                lineStr += f"{matrix[i][j]:.2f} "
            strArr.append(lineStr)

        for str in strArr: #Checks if any line has a length bigger than lineSize
            if(len(str) > lineSize):
                lineSize = (len(str) + 1)

        for i in range(len(strArr)): #Fills the rest of the line
            sizeDelta = (lineSize-len(strArr[i]))
            strArr[i] += " " * (sizeDelta-1)
            strArr[i] += "|"
        
        for str in strArr:
            print(str)

        if(lineBreakAfter):
            print()
    except Exception as err:
        print("Failed to print Matrix")
        print(err)

def getLineMultArr(pivot: float, matrix: list, start:int, xPosition: int):
    try:
        lineMultArr = []
        for y in range(start,len(matrix)):
            getcontext().prec = 4
            lineMult = (Decimal(matrix[y][xPosition])/Decimal(pivot))
            lineMultArr.append(lineMult)

        return lineMultArr
    except Exception as err:
        print("Failed to get Number Modifier")
        print(err)
        return None

def rowReplacement(row: list, lineMultiplier: float, firstRow: list):
    try:
        if(len(row) != len(firstRow)):
            raise Exception("Rows must have the same length")
        
        replacedRow = []
        getcontext().prec = 4
        for i in range(len(row)):
            element = Decimal(row[i]) - Decimal(lineMultiplier) * Decimal(firstRow[i])
            replacedRow.append(element)

        return replacedRow

    except Exception as err:
        print("Failed row replacement")
        print(err)
        return None

def getEquations(arr:list):
    try:
        equationArr = []
        for i in range(len(arr)):
            elementCount = len(arr[i])
            equationStr = ""
            for j in range(elementCount):
                if(j < elementCount-1):
                    equationStr += f"({(arr[i][j]):.2f})"
                    equationStr+= f"*X_{(j+1)}"
                    if(j < elementCount-2):
                        equationStr+= " + " 
                else:
                    equationStr += " = "
                    equationStr += f"({(arr[i][j]):.2f})"
                

            equationArr.append(equationStr)
        return equationArr
    except Exception as err:
        print(err)
        return []
   
def gaussianElimination(matrix: list):
    """
    I - Fase de eliminação: 
    Para uma matriz n x n, este processo terá (n-1) etapas

    A) Montar a matriz aumenta [a|b]
    B) Detereminação do pivô: Ajj
    C) Definir os multiplicadores de linha: (Mij = (Aij/Ajj))
    D) Atualização das linhas: Line - Mij * L_Pivot -> Line
    """
    try:
        #printMatrix(matrix=matrix ,lineBreakAfter=True)

        steps = [matrix]
        
        result = matrix.copy()
        getcontext().prec=4
        for iter in range(0, len(matrix)-1):
            pivot = Decimal(result[iter][iter])
            lineStart = iter+1

            lineMultArr = getLineMultArr(pivot=pivot, matrix=result, start=lineStart, xPosition=iter)
            if(lineMultArr == None):
                raise Exception(f"Failed to get Line Mult Arr #{iter}")
            
            adjustedMatrix = []
            adjustedMatrix = result.copy()
            for i in range(lineStart, len(result)):
                adjustedRow = rowReplacement(row=result[i], lineMultiplier=lineMultArr[i-lineStart], firstRow=result[iter])
                if(rowReplacement == None):
                    raise Exception("Failed to get adjusted row")
                adjustedMatrix[i] = adjustedRow
            
            result = adjustedMatrix.copy()
            steps.append(result)

        
        print("Passos da matriz")
        for arr in steps:
            printMatrix(arr)

        equationArr = getEquations(steps[-1])
        print("Sistema de equações:")
        for equation in equationArr:
            print(equation)
        print()

    except Exception as err:
        print(err)
        return None
    


if __name__ == "__main__":
    clearScreen()
    getcontext().prec = 2
    matrix = [[Decimal('5'), Decimal('3'), Decimal('360')], [Decimal('2'), Decimal('1'), Decimal('132')]]
    gaussianElimination(matrix=matrix)

    #RESULT:
    """
    BROCHURA = 72
    CLUBE DO LIVRO = 36
    DELUXE = 60
    """