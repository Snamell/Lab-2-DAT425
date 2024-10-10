def transpose(M):
    new_matrix=[]
    new_row=[]

    if M==[]:
        return M                                    # If M is an empty matrix, returns the empty matrix
    
    else:
        for j in range(len(M[0])):                  # Iterates through the j postition
            for i in range(len(M)):                 # Iterates through the i position
                new_row.append(M[i][j])             # Appends the value of the matrix M in the i,j position to a new row 
                if len(new_row)==len(M):            # If the new row's length is equal to the length of M, appends the new row to the new matrix
                    new_matrix.append(new_row)      
                    new_row=[]                      # Resets what's contained in new_row
    
        return new_matrix


def powers(List,startexp, endexp):
    new_matrix_pow = []
    
    if startexp > endexp:                                    # If the exponents are in the wrong order, returns an empty matrix
        
        return([[]])
    
    exponents = list(range(startexp,endexp+1))              # Creates a list ranging from startexp to endexp. +1 because of how ranges work

    for i in range(len(exponents)):                         # Iterates the i position of the exponents
        for j in range(len(List)):                          # Iterates the j position of the inputted list
            if i == 0:                                      
                new_matrix_pow.append([])
            new_matrix_pow[j].append(List[j]**exponents[i])
    
    return(new_matrix_pow)


def matmul(M1,M2):
    new_matrix_mul=[]
    new_row=[]
    
    for i in range(len(M1)):                                # Iterates through the rows of matrix M1
        for j in range(len(M2[0])):                         # Iterates through the collumns of matrix M2    
            new_row.append(0)                               # Appends 0 to the new row
            if len(new_row)==len(M2[0]):                    # If the length of the new row is equal to the length of the rows of matrix M2, appends the rows of 0:s so the new matrix has the same row length as M2
                new_matrix_mul.append(new_row)
                new_row=[]                                  
    
    for i in range(len(M1)):                                
        for j in range(len(M2[0])):                         
            for n in range(len(M2)):                        # Iterates through the rows of matrix M2
                try:
                 new_matrix_mul[i][j]+=(M1[i][n]*M2[n][j])  # Replaces the correct position of the matrix filled with 0:s with the product of the corresponding values in M1 and M2
                except IndexError:                          # IndexError sometimes occure. This fixes it
                    break
    
    return new_matrix_mul


def invert(M):
    det=(M[0][0]*M[1][1])-(M[0][1]*M[1][0])
    inverted_matrix=[[M[1][1]/det,-M[0][1]/det],
                     [-M[1][0]/det,M[0][0]/det]]
    
    return inverted_matrix


def loadtxt(file):

    matrix=[]
    f = open(file,"r")
    for line in f:
        matrix.append([float(x) for x in line.split()])     # Splits each line between the spaces and appends them as floats
    f.close()
    
    return matrix