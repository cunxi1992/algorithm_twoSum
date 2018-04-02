class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # enumerate 将列表组合为索引序列
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index = nums.index(sub_num)
                if t_index != i:
                    return [i, t_index]

# **********  以下是调用输出的例子  ***********
# 使用列表生成式，生成一个步长为2、从0到30000的列表
nums = [x for x in range(0,30000,2)]
# 将列表按数字从大到小排列
nums.sort(reverse = True)
# 指定要查找的两个数之和
target = 16020
# 创建一个类
solution = Solution()
two_sum = solution.twoSum(nums,target)
# 输出这两个数
print(two_sum)




        # # 这种方法运算效率较低
        # # 使用for循环，从第一个元素开始，逐个遍历相加
        # for i in range(0,len(nums)-1):
        #   for j in range(i+1,len(nums)):
        #       if nums[i] + nums[j] == target:
        #           return [i,j]









