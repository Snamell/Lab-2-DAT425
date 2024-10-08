def transpose(M):
    row_len=0
    new_matrix=[]
    new_row=[]

    if M==[]:
        return M
    else:
        for j in range(len(M[0])):
            for i in range(len(M)):
                new_row.append(M[i][j])
                row_len+=1
                if row_len==len(M):
                    new_matrix.append(new_row)
                row_len=0
                new_row=[]
    
        return new_matrix


def powers(M,startexp,endexp):

    M == []

    if M==[]:
        return M
    else:
        pass
    
