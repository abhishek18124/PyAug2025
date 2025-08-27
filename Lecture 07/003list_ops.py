nums = [20, 30, 40, 50, 60]
print(nums, len(nums))
nums.insert(0, 10)
print(nums, len(nums)) # linear time op

nums.append(70) # const time op
print(nums, len(nums)) 

print(nums.pop(0)) # linear time op.
print(nums, len(nums))

print(nums.pop()) # pops the value at the end of the list # const time op
print(nums, len(nums))

nums1 = [10, 20, 30, 40]
nums2 = [50, 60, 70, 80]

print(nums1, len(nums1))
nums1.extend(nums2)
print(nums1, len(nums1))