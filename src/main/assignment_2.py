import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def nevilles_method(x_points,y_points,value):
    size: int = len(x_points)
    matrix: np.array = np.zeros((size,size))


    for counter, row in enumerate (matrix):
        row[0]=y_points[counter]
    
    num_of_points = len(x_points)
    for i in range(1, num_of_points):
        for j in range(1,i+1):
            first_multipliction  = (value - x_points[i-j])*    matrix[i][j-1]   
            second_multipliction = (value - x_points[i])*  matrix[i-1][j-1] 
          
            denominator = x_points[i] - x_points[i-j]
            coefficient = (first_multipliction - second_multipliction)/denominator
            
            matrix[i][j]=coefficient 
            

    out=matrix[2][2];             
    print(out)  

def divided_difference_table(x_points, y_points):
    # set up the matrix
    size: int = len(x_points)
    matrix: np.array = np.zeros((size,size))
    # fill the matrix
    for index, row in enumerate(matrix):
        row[0]= y_points[index]
        
    # populate the matrix (end points are based on matrix size and max operations we're using)
    for i in range(1, size):
        for j in range(1,i+1):
            # the numerator are the immediate left and diagonal left indices...
            numerator = matrix[i][j-1] - matrix[i-1][j-1] 
            # the denominator is the X-SPAN...
            denominator  = x_points[i] - x_points[i-j] 
            operation = numerator / denominator
            # cut it off to view it more simpler
            matrix[i][j] = operation
     
    num_of_points=(len(x_points))
    out = np.zeros(num_of_points-1)
    for index in range(1,len(matrix)):
        out[index-1]=(matrix[index][index])
    print(out)
    return matrix



def get_approximate_result(matrix, x_points, value):
    # p0 is always y0 and we use a reoccuring x to avoid having to recalculate x 
    reoccuring_x_span = 1
    reoccuring_px_result = matrix[0][0]
    
    # we only need the diagonals...and that starts at the first row...
    for index in range(1, len(x_points)):
        polynomial_coefficient = matrix[index][index]
        # we use the previous index for x_points....
        reoccuring_x_span *= (value - x_points[index-1])
        
        # get a_of_x * the x_span
        mult_operation = polynomial_coefficient * reoccuring_x_span
        # add the reoccuring px result
        reoccuring_px_result += mult_operation
    
    # final result
    return reoccuring_px_result


def apply_div_diff(matrix: np.array):
    size= len(matrix)
    round=0
    for i in range(2,size):
        for j in range(2,i+2):    
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            
            #print(" this is the start") 
            left: float = matrix[i][j-1]
            
            diagonal_left: float = matrix[i-1][j-1]
            
            numerator: float = left -diagonal_left   

            denominnator=  matrix[i][0]- matrix[i-j+1][0]   
            operation= numerator/denominnator
            
            
           # print(operation,"")
            matrix[i][j]= operation
            
    #print(matrix)
    return matrix        
            

def hermite_interpolation():
    x_points= [3.6 ,3.8 ,3.9 ]
    y_points= [1.675 ,1.436 ,1.318]
    
    slopes = [-1.195,-1.188 ,-1.182 ]
    
    num_of_points=(len(x_points))
    matrix = np.zeros((num_of_points*2,num_of_points*2))

    index =0
    for x in range(0, len(matrix),2):
        matrix[x][0]=x_points[index]
        matrix[x+1][0]=x_points[index]
        index +=1
        
    index =0
    for x in range(0, len(matrix),2):
        matrix[x][1]=y_points[index]
        matrix[x+1][1]=y_points[index]
        index +=1       
    
    index =0    
    for x in range(1, len(matrix),2):
        matrix[x][2]= slopes[index]
        index+=1 
        
 
    filled_matrix = apply_div_diff(matrix)
    print(filled_matrix)   




def Cubix_spline(x_points,y_points):

    num_of_points=(len(x_points))
    matrixA = np.zeros((num_of_points,num_of_points))
    matrixA[0][0]=1
    matrixA[num_of_points-1][num_of_points-1]=1
    matrixH= np.zeros(num_of_points)
    n=0
    n1=1
    for i in range(0,num_of_points-1):
        for j in range(1,num_of_points-1):    
            if i==j:
                
             #   print (matrixH)
                matrixA[i][j-1]=(x_points[n+1]-x_points[n])
                
                n=n+1
                matrixA[i][j+1]=(x_points[n+1]-x_points[n])
                
                matrixH[n1-1]=(matrixA[i][j-1])
                matrixH[n1]=(matrixA[i][j+1])
                n1=n1+1
             #   print (matrixH)
                matrixA[i][j]=(2*(matrixA[i][j-1]+ matrixA[i][j+1]))
                
    matrixB = np.zeros(num_of_points)
    
    
    
    n=np.zeros(num_of_points)
    #print(matrixH)
    
    for i in range(1,num_of_points-2):
        
        left=(3/matrixH[i+1])*(y_points[i+2] - y_points[i+1])
        
        right=(3/matrixH[i])*(y_points[i+2] - y_points[i])
        
        matrixB[i]=left -right
        
                

            
    
    
    print(matrixA)
   # print(matrixB)
    

if __name__ == "__main__": 
    
    x_points=np.array([3.6,3.8,3.9])
    y_points=np.array([1.675,1.436,1.318])
    value=3.7
    nevilles_method(x_points,y_points,value) 
    
    x_points = [7.2 , 7.4 , 7.5 , 7.6]
    y_points = [23.5492, 25.3913 , 26.8224, 27.4589]
    divided_table = divided_difference_table(x_points, y_points)
    
    # find approximation
    approximating_x = 7.3
    test=final_approximation = get_approximate_result(divided_table, x_points, approximating_x)
    print(test) 
    
    hermite_interpolation()  

    x_points = np.array([2,5,8,10])
    y_points = np.array([3,5,7,9])
    
    Cubix_spline(x_points,y_points)        