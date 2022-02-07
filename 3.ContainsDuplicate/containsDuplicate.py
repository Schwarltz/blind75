'''
given sol using hashset
t: 368 ms
m: 24 MB
'''
def containsDuplicateSol(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False


'''
blind run
sort and see if adjacents match
t: 605 ms
m: 22.3 MB
'''
def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if prev == num:
                return True
            prev = num
        return False

if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))