# import requests
# def images(url, n):
#     response = requests.get(url)    
#     open(f"image{n}.jpg", "wb").write(response.content)

# url = "https://picsum.photos/200/300"
# for i in range(1, 5):
#     images(url, i)
# class Solution(object):
#     def twoSum(self, nums, target):
#         dict = {}
#         for i in range(len(nums)):
#             diff = target - nums[i] 
#             if diff in dict:
#                 return [dict[diff], i]
#             else:
#                 dict[nums[i]] = i
# nums = [2, 3, 5, 7, 5]
# target =8
# obj = Solution()
# print(obj.twoSum(nums, target))

