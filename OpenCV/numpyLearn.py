import numpy as np


def main():
    print("Welcome to numpy")
    np.random.seed(101)
    # print(np.random.randint(0, 100, 10))
    numpy_arr = np.random.randint(0, 100, 10)
    print(numpy_arr)
    print(numpy_arr.max())
    print(numpy_arr.min())
    # argmax returns index
    print(numpy_arr.argmax())
    # argmin returns
    print(numpy_arr.argmin())
    # mean
    print(numpy_arr.mean())
    # reshape: to calculate the number of element 2 * 5 or rows * cols
    print(numpy_arr.reshape(2,5))
    # matrix
    mat = np.arange(0, 100).reshape(10,10)
    print(mat)
    # use indexing to get single data from the array
    print(mat[0][1])
    print(mat[0,1])
    # target is 76
    print(mat[7,7])
    # splicing
    print(mat[:,1])
    print("\n")
    first_col = mat[:,1].reshape(10,1)
    print(first_col)
    print("\n")
    # print rows
    print(mat[0,:])
    print(mat[1,:])
    print(mat[0:3, 0:3])
    # re-assign value
    mynewmat = mat.copy()
    mynewmat[0:3, 0:3]  = 0
    print(mynewmat)



if __name__ == "__main__":
    main()