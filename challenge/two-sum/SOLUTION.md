# [Niyousha Mohammadshafie](https://stackoverflow.com/a/66954724/6474744)'s solution on SO

I found 3 main ways to solve this question, the 1st approach is brute force with time complexity of O(n^2) and space complexity of O(1):

```python
def twoNumberSum(array, targetSum):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return ([array[i], array[j]])
    return []
```

The 2nd approach is using hash map with time complexity of O(n) and space complexity of O(n):

```python
def twoNumberSum(array, targetSum):
    matches = {}
    for number in array:
        match = targetSum - number
        if match in matches:
            return [match, number]
        else:
            matches[number] = True
    return []
```

The 3rd approach is with two pointers of left and right.
This method has time complexity of O(nlogn) and space complexity of O(1):

```python
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left +=1
        elif array[left] + array[right] > targetSum:
            right -=1
    return []
```