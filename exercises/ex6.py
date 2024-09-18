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
            lineMult = (matrix[y][xPosition]/float(pivot))
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
        for i in range(len(row)):
            element = row[i] - lineMultiplier * firstRow[i]
            replacedRow.append(element)

        return replacedRow

    except Exception as err:
        print("Failed row replacement")
        print(err)
        return None

def gaussianElimination(matrix: list):
    """
    I - Fase de eliminação: 
    Para uma matriz n x n, este processo terá (n-1) etapas

    A) Montar a matriz aumenta [a|b]
    B) Detereminação do pivô: Akk
    C) Definir os multiplicadores de linha: (Mik = (Aik/Akk))
    D) Atualização das linhas: Line - Mik * Lpivô -> Line
    """
    try:
        printMatrix(matrix=matrix ,lineBreakAfter=True)

        steps = [matrix]
        
        result = matrix.copy()
        for iter in range(0, len(matrix)-1):
            pivot = result[iter][iter]
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

        for arr in steps:
            printMatrix(arr)

    except Exception as err:
        print(err)
        return None
    


if __name__ == "__main__":
    #matrix = [[1.0, 2.0, 3.0, 360.0],[2.0, 4.0, 5.0, 660.0],[2.0, -1.0, 0, 0]]
    matrix = [[3, 2, 4, 1],[1,1,2,2],[4,3,-2,3]]
    gaussianElimination(matrix=matrix)