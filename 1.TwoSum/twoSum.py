from bisect import bisect

'''
Two pointer provided solution. Much more efficient.
'''
def twoSumSol(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            return dict({'low_index': i+1, 'high_index': j+1})



'''
Own solution given no hints
'''
def twoSum(numbers, target):
    # Assuming non-negative numbers, we can exclude elements <= target as
    # everything larger than the target cannot be added with something else.
    max_i = bisect(numbers,target)

    for high in numbers[max_i::-1]:
        # low + high <= target so low <= target - high
        low_i = bisect(numbers, target - high)
        for low in numbers[:low_i]:
            # found pair
            if low+high == target:
                high_index = numbers.index(high) + 1
                low_index = numbers.index(low) + 1
                return dict({'low_index': low_index, 'high_index': high_index})
    
    # no pair found
    return dict({'low_index': -1, 'high_index': -1})


if __name__ == '__main__':
    numbers = [2,7,9,11,15]
    target = 9
    print(twoSum(numbers, target))
