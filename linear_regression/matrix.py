def transpose(M):
    
    row_len=0
    new_matrix=[]
    new_row=[]

    if M==[]:
        return M                                    # If M is an empty matrix, returns the empty matrix
    
    else:
        for j in range(len(M[0])):                  # Iterates through the j postition
            for i in range(len(M)):                 # Iterates through the i position
                new_row.append(M[i][j])             # Appends the value of the matrix M in the i,j position to a new row
                row_len+=1                          # Increases the value of the row length by 1
                if row_len==len(M):                 # If the row length is equal to the length of M, appends the new row to the new matrix
                    new_matrix.append(new_row)      
                    row_len=0                       # Resets the row length counter
                    new_row=[]                      # Resets what's contained in new_row
    
        return new_matrix


def powers(L,startexp,endexp):
    
    row_len=0
    new_matrix_exp=[]
    new_row=[]
    i=0                                             # Keeps track of the position i

    if L==[]:
        return L                                    # If L is an empty list, returns the empty list
    
    elif len(L)==1:
        for exp in range(startexp,endexp+1):        # Iterates the exponent value through the start value to the end value
                new_row.append(L[i]**exp)           # In a list of the length 1 the value most be taken out of the list in order to evaluate it
        
        return [new_row]                            # Returns new_row as a matrix
    
    elif len(L)==2:                                 
         while i<len(L):                            
             for exp in range(startexp,endexp+1):   
                new_row.append(L[i]**exp)           
                row_len+=1                          
                if row_len==len(L)+1:               # If the length of the list L is 2, an IndexError occur if the +1 is not in place after len(L)
                    new_matrix_exp.append(new_row)
                    row_len=0
                    new_row=[]
             i+=1                                   # Goes to the next position in L
                   
         return new_matrix_exp

    else:
         while i<len(L):
             for exp in range(startexp,endexp+1):
                new_row.append(L[i]**exp)
                row_len+=1
                if row_len==len(L):
                    new_matrix_exp.append(new_row)
                    row_len=0
                    new_row=[]
             i+=1
                   
         return new_matrix_exp


def matmul(M1,M2):
    
    new_matrix_mul=[]
    new_row=[]
    
    for r in range(len(M1)):                                # Iterates through the rows of matrix M1
        for c in range(len(M2[0])):                         # Iterates through the collumns of matrix M2    
            new_row.append(0)                               # Appends 0 to the new row
            if len(new_row)==len(M2[0]):                    # If the length of the new row is equal to the lengt of the rows of matrix M2, appends the rows of 0:s so the new matrix has the same row length as M2
                new_matrix_mul.append(new_row)
                new_row=[]                                  
    
    for i in range(len(M1)):                                
        for j in range(len(M2[0])):                         
            for n in range(len(M2)):                        # Iterates through the rows of matrix M2
                new_matrix_mul[i][j]+=(M1[i][n]*M2[n][j])   # Replaces the correct position of the matrix filled with 0:s with the product of the corresponding values in M1 and M2
        
    return new_matrix_mul


def invert(M):
    
    det = (M[0][0] * M [1][1] - (M[0][1] * M[1][0]))
    inverted_matrix = [[M[1][1]/det,-M[0][1]/det], [-M[1][0]/det, M[0][0]/det]]
    
    return inverted_matrix


def loadtxt(file):

    matrix=[]
    f = open(file,"r")
    for line in f:
        matrix.append([float(x) for x in line.split()]) # splits each line between the spaces and appends them as floats
    f.close()
    
    return matrix