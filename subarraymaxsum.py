def maxSum(arr ):
    left=0
    right=1
    prevsum = arr[left] + arr[right]
    i=2
    while i < len(arr):
        if prevsum < prevsum +arr[i]:
            right= right+1
            prevsum = prevsum + arr[i]
        else:
            left = left+1
            right = left+1
            prevsum = arr[left] + arr[right]
        i= i +1

        return left, right, prevsum

print(maxSum([-1, 2, 4, -3, 5, 2, -5, 2]))
