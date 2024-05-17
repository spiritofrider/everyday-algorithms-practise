def binary_search(arr, N, x):
    l = 0
    r = N-1
    while l<=r:
        m = l + (r-l)//2

        if arr[m] == x:
            return m
        
        if arr[m] < x:
            l = m+1
        else:
            r = m-1
    return -1

if __name__ == "__main__":
    arr = [2,3,4,10,40]
    N = len(arr)
    x = 3

    result = binary_search(arr, N, x)

    if result == -1:
        print(f'{x} not present in the given array')
    else:
        print(f'{x} is present at index {result}')
       