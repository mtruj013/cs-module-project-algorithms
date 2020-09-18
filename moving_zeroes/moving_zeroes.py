'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    length = len(arr)
    
    for i in range(length):
        if arr[i] != 0:
            # arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]
            arr[count] = arr[i]
            count += 1

    while count < length:
        arr[count] = 0
        count += 1

    return arr
            


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")