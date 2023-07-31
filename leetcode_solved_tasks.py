from typing import List, Dict
import functools

# TWO SUM
nums1 = [2, 7, 11, 15]
target = 9
def twoSum(nums: List[int], target: int) -> List[int]:
    # iterations over nums in order to find a sequence number
    for a in range(len(nums1)):
        for b in range(len(nums1)):
            # using sn from previous loop adding two numbers to compare it with target number
            # if target is equal, and not to equal repeating sn in a list, return their sn
            if target == (nums[a] + nums[b]) and a != b:
                return f"twoSum result {[a, b]}"
print(twoSum(nums1, target))


# Remove Duplicates from Sorted Array
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
def removeDuplicates(nums: List[int]) -> int:
    # 'nums[:]' replaces element in place, by creating new list object
    # the sorted() function returns a sorted list of the specified iterable object
    # the set() function returns unique values from an object
    nums[:] = sorted(set(nums))
    return f"removeDuplicates result {nums}"
print(removeDuplicates(nums2))


# Remove Element
nums3 = [3, 3, 2, 3]
val = 2
def removeElement(nums: List[int], val: int) -> int:
    # while while 'val' in nums3 it interacts over it, with each interaction it will remove val from a list till it becomes False
    while val in nums:
        nums.remove(val)
print(removeElement(nums3, val))


# Length of Last Word
s = " hello world "
def lengthOfLastWord(s: str) -> int:
    result = 0
    # iterate throughout the list from right to left
    for i in range(len(s)-1):
        # ignore all whitespaces
        if s[i] != " ":
            result += 1
        # when reaching the alphabet character count all adjacent non-whitespace elements and return the result when reaching a whitespace element
        elif result:
            return f"lengthOfLastWord result {result}"
    return f" last return {result}"
print(lengthOfLastWord(s))


# Is Palindrome
x = 31
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    # convert given number into string and compare it with the reversed string
    return str(x) == str(x)[::-1]
print(isPalindrome(x))


# Majority Element
nums4 = [6, 5, 5]
def majorityElement(nums: List[int]) -> int:
    none = None
    count = 0
    for i in nums:
        if count == 0:
            # if count eq 0, reassign none variable to iteration value
            none = i
        # add to count 1, if iteration equal reassigned value
        count += (1 if i == none else -1)
    return none
print(majorityElement(nums4))


# Contains Duplicate
nums5 = [1, 2, 3, 4]
def containsDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        uniq_num = set()
        for i in nums:
           if i in uniq_num:
               return True
           else:
             print(uniq_num)
             uniq_num.add(i)
containsDuplicate(nums5)


# Defanging an IP Address
address = "1.1.1.1"
def defangIPaddr(address: str) -> str:
    # using method 'replace' we change '.' values, to '[.]'
    return address.replace(".", "[.]")
print(defangIPaddr(address))


nums6 = [1, 2, 1]
def getConcatenation(nums: List[int]) -> List[int]:
    return nums * 2
print(getConcatenation(nums6))


# Maximum Number of Words Found in Sentences
sentences = ["please wait", "continue to fight", "continue to win"]
def mostWordsFound(sentences: List[str]) -> int:
    list_values = []
    for i in sentences:
        values = len(i.split())
        list_values.append(values)
    return max(list_values)
# more sophisticated example in one line where we get number as a integer then interact over each elem in order to get max value
# def mostWordsFound(sentences: List[str]) -> int:
#   return max([len(i.split()) for i in sentences])
print(mostWordsFound(sentences))



# Create Target Array in the Given Order
index = [0, 1, 2, 2, 1]
nums7 = [0, 1, 2, 3, 4]
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    target = []
    # zip function returns a zip object, which is paired index and value together
    for value, place in zip(nums, index):
        # insert place and values together into new target empty list
        target.insert(place, value)
    return target
print(createTargetArray(nums7, index))



# How Many Numbers Are Smaller Than the Current Number
nums8 = [8, 1, 2, 2, 3]
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    # return len of all elements, compare 'i' with number
    return [len([i for i in nums if i < number]) for number in nums]
print(smallerNumbersThanCurrent(nums8))


# Sum of Unique Elements
nums9 = [1, 2, 3, 2]
def sumOfUnique(nums: List[int]) -> int:
    uniq = []
    # Count() is a Python built-in function that returns the number of times an object appears in a list.
    [uniq.append(num)for num in nums if nums.count(num) == 1]
    return sum(uniq)
print(sumOfUnique(nums9))


nums10 = [914,894,448,946,7,835,858,896,56,224,565,971,112,14,116,196,28]
original = 7
def findFinalValue(nums: List[int], original: int) -> int:
    nums=set(nums)
    while original in nums:
        original *=2
    return original

print(findFinalValue(nums10, original))