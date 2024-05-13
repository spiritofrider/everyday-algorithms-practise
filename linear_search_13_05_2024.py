def linear_search(arr,N,x):
    for i in range(0,N):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    result = linear_search(arr, N, x)
    if result == -1:
        print(f'{x} not present in the given array')
    else:
        print(f'{x} is present at index {result}')
