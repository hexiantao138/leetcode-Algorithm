## 基础python语法实验
# def demo(**args_v):
#     for k, v in args_v.items():
#         print(k,v)
    
# print(demo(name = 'hxt', 'llq'))

# def demo(*args_v):
#     for k in args_v:
#         print(k)
# print(demo("hxt", "llq","a"))



# 面试题：去除数组中重复值，不使用新数组
# def dropduplicate(array):
#     array.sort()
#     nums = array[-1]
#     for i in range(len(array)-2,-1,-1):
#         if(nums == array[i]):
#             del array[i]
#         else:
#             nums = array[i]
#     return array

# # main function
# array = [3,4,3,6,4,7,23,4,3,8]
# print(dropduplicate(array))


# # leetcode 985. 查询后的偶数和
# 以下算法使用两个for循环，时间复杂度为O(n^2),leetcode上提交超时
# def sumEvenAfterQueries(A, queries):
#     new_array = []
#     for i in range(0, len(queries)):
#         sum = 0
#         pos = queries[i][1]              #0   1   0
#         val = queries[i][0]              #1  -3  -4
#         A[pos] = A[pos] +  val           #A[0] = A[0] + 1;  A[1] = A[1] + (-3); A[0] = A[0] + (-4)
#         for j in range(0, len(A)):
#             if(A[j] % 2 == 0):
#                 sum = sum + A[j]
#         new_array.append(sum)
#     return new_array

# A = [1,2,3,4]
# queries = [[1,0],[-3,1],[-4,2],[2,3]]
# New_array = sumEvenAfterQueries(A, queries)
# print(New_array)



#leetcode 1588. 所有奇数长度子数组的和
# def sumOddLengthSubarrays(array):
#     sum = 0
#     for i in range(0, len(array) + 1):         #找到输入数组的所有子集
#         n = i + 1                              #定义n为数组长度下界
#         while n <= len(array):                 #限制n的大小不得大于数组长度
#             sub = array[i:n]                   #循环的得到子集
#             if (len(sub) % 2 == 1):            #判断所有子集长度为奇数
#                 for j in range(0, len(sub)):
#                     sum = sum + sub[j]
#             n = n + 1
#     return sum

# array = [1,4,2,5,3]
# print(sumOddLengthSubarrays(array))



#leetcode 1281. 整数的各位积和之差
# def subtractProductAndSum(n):
#     val = 0
#     sum = 0
#     mul = 1
#     while n > 0:
#         val = n % 10
#         n = n // 10
#         sum = sum + val
#         mul = mul * val
#         result = mul - sum
#     return result
# n = 4421
# print(subtractProductAndSum(n))



# leetcode 1480. 一维数组的动态和
# def runningSum(array):
#     new_array = []
#     sum = 0
#     for i in range(0, len(array) + 1):
#         temp_array = array[0:i]
#     for j in range(0, len(temp_array)):
#         sum = sum + temp_array[j]
#         new_array.append(sum)
#     return new_array

# array = [1,2,3,4]
# print(runningSum(array))
    


# leetcode 1486. 数组异或操作
# def xorOperation(n, start):
#     new_array = []
#     result = 0
#     for i in range(0,n):
#         nums = start + 2 * i
#         result = result ^ nums
    
#     return result

# print(xorOperation(10,5))



#leetcode 1. 两数之和
# def twoSum(nums, target):
#     result = []
#     for i in range(0, len(nums)):
#         n = i + 1
#         for j in range(n, len(nums)):
#             if (nums[i] + nums[j] == target):
#                 result.append(i)
#                 result.append(j)
#     return result

# array = [2, 7, 11, 15]
# target = 9
# print(twoSum(array, target))



#leetcode 167. 两数之和 II - 输入有序数组 暴力枚举法：
#此类算法超出时间限制，O(n^2)
# def twoSum(numbers, target):
#     result = []
#     for i in range(0, len(numbers)):
#         n = i + 1
#         for j in range(n, len(numbers)):
#             if ((numbers[i] + numbers[j] == target) and (i < j)):
#                 result.append(i+1)
#                 result.append(j+1)
#     return result

# array = [2, 7, 11, 15]
# target = 9
# print(twoSum(array, target))



##leetcode 167. 两数之和 II - 输入有序数组(优化版) 双指针法：
# def twoSum(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         if(numbers[left] + numbers[right] == target):
#             return [left + 1, right + 1]
#         elif(numbers[left] + numbers[right] > target):
#             right = right - 1
#         else:
#             left = left + 1

# array = [2, 25, 50]
# target = 75
# print(twoSum(array, target))



#leetcode 905. 按奇偶排序数组
# 升序排列， key内为排序原则。若list中元素是偶数，则为0，奇数为1，服从升序排列
# def sortArrayByParity(array):
#     A = sorted(array, key = lambda x: 0 if x % 2 == 0 else 1)  
#     return A
    
# array = [3,1,2,4]
# print(sortArrayByParity(array))



#leetcode 1470. 重新排列数组  想半天，但其实很简单,时间复杂度O(n)解决
# def shuffle(nums, n):
#     new_array = []
#     j = n
#     for i in range(0, n):
#         new_array.append(nums[i])
#         new_array.append(nums[j])
#         j = j + 1
#     return new_array
# nums = [2,5,1,3,4,7]  #[2,3,5,4,1,7]
# n = 3
# print(shuffle(nums, n))



#leetcode 1672. 最富有客户的资产总量
# def maximumWealth(list):
#     sum_list = []
#     for i in range(0, len(accounts)):
#         sum = 0
#         for j in range(0, len(accounts[0])):
#             sum = sum + accounts[i][j]
#         sum_list.append(sum)
#     sum_list.sort(reverse = True)
#     result = sum_list[0]
#     return result

# accounts = [[1,5],[7,3],[3,5]]
# print(maximumWealth(accounts))



# leetcode 1512. 好数对的数目
# def numIdenticalPairs(nums):
#     sum = 0
#     for i in range(0, len(nums)):
#         n = i + 1
#         for j in range(n, len(nums)):
#             if(nums[i] == nums[j]):
#                 sum = sum + 1
#     return sum

# nums = [1,1,1,1]
# print(numIdenticalPairs(nums))



#leetcode 643. 子数组最大平均数 I
# def findMaxAverage(nums, k):
    
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(findMaxAverage(nums, k))
# nums = [4,2,1,3,3]
# k = 2
# print(findMaxAverage(nums, k))



#leetcode 1365. 有多少小于当前数字的数字
# def smallerNumbersThanCurrent(nums):
#     nums.sort()
    
#     return new_array
# nums = [8,1,2,2,3]
# print(smallerNumbersThanCurrent(nums))



# leetcode 5617. 设计 Goal 解析器
# def interpret(command):
#     idx = 0
#     result = ""
#     while (idx < len(command)):
#         if(command[idx] == "G"):
#             result = result + "G"
#             idx = idx + 1
#         elif(command[idx] == "("):
#             if(command[idx + 1] == ")"):
#                 result = result + "o"
#                 idx = idx + 1
#             elif(command[idx + 1] == "a"):
#                 result = result + "a" + "l"
#                 idx = idx + 1
#         else:
#             idx = idx + 1
#             continue
#     return result

# command = "(al)G(al)()()G"
# print(interpret(command))



#leetcode LCP 01. 猜数字
# def game(guess, answer):
#     result = 0
#     idx = 0
#     while (idx < len(guess)):
#         if(guess[idx] == answer[idx]):
#             result = result + 1
#             idx = idx + 1
#         else:
#             idx = idx + 1
#             continue
#     return result


# guess = [2,2,3]
# answer = [3,2,1]
# print(game(guess, answer))



#leetcode 1295. 统计位数为偶数的数字
# def findNumbers(nums):
#     result = 0
#     for i in range(0, len(nums)):
#         if(len(str(nums[i])) % 2 == 0):
#             result = result + 1
#     return result

# nums = [555,901,482,1771]
# print(findNumbers(nums))



#leetcode 1389. 按既定顺序创建目标数组
# def createTargetArray(nums, index):
#     target = []
#     for i in range(0, len(index)):
#         target.append(nums[index[i]])
#     return target

# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
# print(createTargetArray(nums, index))



#leetcode 5625. 比赛中的配对次数
# def numberOfMatches(n):
#     count = 0
#     i = 0
#     val = n
#     if (val == 3):
#         count = 2
#     elif (val == 5):
#         count = 4
#     else:
#         while i < (n - 1) / 2:
#             if (val % 2 == 0):
#                 count = count + val / 2
#                 i = i + 1
#                 val = val - val / 2
#             else:
#                 count = count +  val // 2
#                 i = i + 1
#                 val = val - val // 2
#     count = int(count)
#     return count

# n = 5
# print(numberOfMatches(n))



#leetcode 5609. 统计一致字符串的数目
# def countConsistentStrings(allowed, words):
#     a = set(allowed)
#     nums = 0
#     for i in range(0, len(words)):
#         if (a | set(words[i]) == set(a)):
#             nums = nums + 1
#     return nums
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]
# print(countConsistentStrings(allowed, words))



#leetcode 1662. 检查两个字符串数组是否相等
# def arrayStringsAreEqual(word1, word2):
#     word1_sum = ""
#     word2_sum = ""
#     for i in range(0, len(word1)):
#         word1_sum = word1_sum + word1[i]
#     for j in range(0, len(word2)):
#         word2_sum = word2_sum + word2[j]

#     return word1_sum == word2_sum

# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# print(arrayStringsAreEqual(word1, word2))



#leetcode 217. 存在重复元素
# def containsDuplicate(nums):
#     nums.sort()
#     if (nums == [] or len(nums) == 1):
#         return False
#     else:
#         count = 0
#         for i in range(0, len(nums) - 1):
#             if (nums[i] != nums[i+1]):
#                 count = count + 1
#         return count != len(nums) - 1

# nums = [1,1,1,3,3,4,3,2,4,2]
# print(containsDuplicate(nums))



#leetcode 1365. 有多少小于当前数字的数字
# def smallerNumbersThanCurrent(nums):
#     array = []
#     for i in range(0, len(nums)):
#         count = 0
#         for j in range(0, len(nums)):
#             if(nums[j] < nums[i]):
#                 count = count + 1
#         array.append(count)
#     return array

# nums = [8,1,2,2,3]
# print(smallerNumbersThanCurrent(nums))



#leetcode 738. 单调递增的数字  时间复杂度太高，可优化
# def monotoneIncreasingDigits(N):
#     for i in range(N, 0, -1):
#         count = 0
#         for j in range(0, len(str(i)) - 1):
#             if(str(i)[j] <= str(i)[j+1]):
#                 count = count + 1
#             else:
#                 break
#         if(count == len(str(i)) - 1):
#             return i
# N = 393457075
# print(monotoneIncreasingDigits(N))



## leetcode 1518. 换酒问题
# def numWaterBottles(numBottles, numExchange):
#     sum = numBottles
#     while(numBottles >= numExchange):
#         val = numBottles // numExchange
#         sum = sum + val
#         numBottles = numBottles % numExchange + val
#     return sum

# m = 2
# n = 3
# print(numWaterBottles(m,n))



## leetcode 509. 斐波那契数 经典递归算法
# def fib(n):
#     if(n == 1 or n == 2):
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(4))



## leetcode 1385. 两个数组间的距离值  注：双循环暴力解法可以通过
## 时间复杂度过于高，需要优化
# def findTheDistanceValue(arr1, arr2, d):
#     sum = 0
#     for i in range(0, len(arr1)):
#         count = 0
#         for j in range(0, len(arr2)):
#             if(abs(arr1[i] - arr2[j]) > d):
#                 count = count + 1
#         if(count == len(arr2)):
#             sum = sum + 1
#     return sum

# arr1 = [2,1,100,3]
# arr2 = [-5,-2,10,-3,7]
# d = 6
# print(findTheDistanceValue(arr1, arr2, d))



## leetcode 1394. 找出数组中的幸运数 依然是双循环暴力解法
# def findLucky(arr):
#     result = []
#     for i in range(0, len(arr)):
#         count = 0
#         for j in range(0, len(arr)):
#             if(arr[i] == arr[j]):
#                 count = count + 1
#         if(count == arr[i]):
#             result.append(arr[i])
#         else:
#             result.append(-1)
#     result.sort(reverse = True)
#     return result[0]

# arr = [2,2,3,4]
# print(findLucky(arr))



## leetcode 349. 两个数组的交集 暴力求解法，时间复杂度太高
# def intersection(nums1, nums2):
#     result = []
#     result2 = []
#     for i in range(0, len(nums1)):
#         for j in range(0, len(nums2)):
#             if(nums1[i] == nums2[j]):
#                 result.append(nums1[i])
#     for idx in range(0, len(result)):
#         if(result[idx] not in result2):
#             result2.append(result[idx])
#     return result2
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(intersection(nums1, nums2))



## leetcode 551. 学生出勤记录 I
# def checkRecord(s):
#     late = 0
#     count = 0
#     for i in range(0, len(s)):
#         if(s[i] == 'A'):
#             count = count + 1
#     for j in range(0, len(s) - 2):
#         if(s[j] == 'L' and s[j] == s[j+1] and s[j+1] == s[j+2]):
#             late = late + 1
#     if(count <= 1 and late < 1):
#         return True
#     else:
#         return False
    
# s = "PPALLL"
# print(checkRecord(s))



## leetcode 728. 自除数
# def selfDividingNumbers(left, right):
#     result = []
#     for i in range(left, right+1):
#         count = 0
#         for j in range(0, len(str(i))):
#             if(int(str(i)[j]) != 0 and i % int(str(i)[j]) == 0):
#                 count = count + 1
#         if(count == len(str(i))):
#             result.append(i)
#     return result

# left = 1
# right = 22
# print(selfDividingNumbers(left, right))



##leetcode 1528. 重新排列字符串
# def restoreString(s, indices):
#     arr = [0] * (len(s))
#     result = ""
#     for i in range(0, len(s)):
#         arr[indices[i]] = s[i]
#     for j in range(0, len(arr)):
#         result = result + arr[j]
#     return result

# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# print(restoreString(s, indices))



## leetcode 1668. 最大重复子字符串
# def maxRepeating(word, sequence):
#     count = 0
#     word_sum = word 
#     while(len(word_sum) <= len(sequence)):
#         len_word = len(word_sum)
#         for i in range(0, len(sequence)):
#             if(sequence[i:i+len_word] == word_sum):
#                 count = count + 1
#                 break
#         word_sum = word_sum + word
#     return count 
# sequence = "ababc"
# word = "ab"
# print(maxRepeating(word, sequence))



## leetcode 1550. 存在连续三个奇数的数组
# def threeConsecutiveOdds(arr):
#     for i in range(0, len(arr)-2):
#         if(arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1):
#             return True
#     return False
# arr = [1,2,34,3,4,5,7,23,12]
# print(threeConsecutiveOdds(arr2))



## leetcode 704. 二分查找
# def search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while(left <= right):
#         mid = (left + right) // 2
#         if(nums[mid] == target):
#             return mid
#         elif(nums[mid] > target):
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1

# nums = [-1,0,3,5,9,12]
# target = 9
# print(search(nums, target))



## leetcode 1304. 和为零的N个唯一整数
# def sumZero(n):
#     if(n % 2 == 1):
#         arr = []
#         j = 1
#         for i in range(0, n):
#             if(i == n // 2):
#                 arr.append(0)
#             elif(i < n // 2):
#                 arr.append(i + 1)
#             else:
#                 arr.append(-j)
#                 j = j + 1
#     else:
#         arr = []
#         for i in range(1, n+1):
#             if(i % 2 == 1):
#                 arr.append(i)
#             else:
#                 arr.append(-(i-1))
#     return arr

# print(sumZero(9))



##leetcode 448. 找到所有数组中消失的数字
# def findDisappearedNumbers(nums):
#     if(nums == []):
#         return nums
#     else:
#         result = []
#         left = 1
#         right = len(nums) + 1
#         for i in range(left, right):
#             result.append(i)
#     return list(set(result) - set(nums))

# nums = [1, 1]
# print(findDisappearedNumbers(nums))

