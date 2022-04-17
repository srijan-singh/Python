def row_rule(matrix, index, value):
    
    temp_set = set()
    for i in range(9):
        elm = matrix[index][i]
        if elm != 0:
            temp_set.add(elm)
	
    return value not in temp_set

def col_rule(matrix, index, value):
    
    temp_set = set()
    for i in range(9):
        elm = matrix[i][index]
        if elm != 0:
            temp_set.add(elm)
	
    return value not in temp_set

def matrix_rule(matrix, x, y, value) :
    
    temp_set = set()
    
    # Initial and final cordinates
    if (x < 3 and y < 3):
        #print(0,3)
        #print(0,3)
        x_i,x_f = (0,3)
        y_i,y_f =(0,3)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    elif (x < 3 and y < 6):
        #print(0,3)
        #print(3,6)
        x_i,x_f = (0,3)
        y_i,y_f =(3,6)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    elif (x < 3 and y < 9):
        #print(0,3)
        #print(6,9)
        x_i,x_f = (0,3)
        y_i,y_f =(6,9)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)
        

    elif (x < 6 and y < 3):
        #print(3,6)
        #print(0,3)
        x_i,x_f = (3,6)
        y_i,y_f =(0,3)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    elif (x < 6 and y < 6):
        #print(3,6)
        #print(3,6)
        x_i,x_f = (3,6)
        y_i,y_f =(3,6)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    elif (x < 6 and y < 9):
        #print(3,6)
        #print(6,9)
        x_i,x_f = (3,6)
        y_i,y_f =(6,9)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)


    elif (x < 9 and y < 3):
        #print(6,9)
        #print(0,3)
        x_i,x_f = (6,9)
        y_i,y_f =(0,3)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)
        
    elif (x < 9 and y < 6):
        #print(6,9)
        #print(3,6)
        x_i,x_f = (6,9)
        y_i,y_f =(3,6)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    elif (x < 9 and y < 9):
        #print(6,9)
        #print(6,9)
        x_i,x_f = (6,9)
        y_i,y_f =(6,9)
        for i in range(x_i, x_f):
            for j in range(y_i, y_f):
                elm = matrix[i][j]
                if elm != 0:
                    temp_set.add(elm)

    return value not in temp_set      
    
    
        
        

def isItSudoku(matrix):
    # Write your code here.
    for i in range(9):
        temp_set_x = set()
        temp_set_y = set()
        
        for j in range(9):
            temp_set_x.add(matrix[i][j])
            temp_set_y.add(matrix[j][i])

        for index in range(9):

            for value in temp_set_x:
                if not row_rule(matrix, index, value) :  return "NO"
                if not matrix_rule(matrix, i, index, value) : return "NO"

            for value in temp_set_y:
                if not col_rule(matrix, index, value) : return "NO"
                if not matrix_rule(matrix, index, i, value) : return "NO"

    
    return "YES"
        

            


