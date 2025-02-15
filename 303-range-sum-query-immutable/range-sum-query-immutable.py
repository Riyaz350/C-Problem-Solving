class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        cur = 0;
        for i in nums:
            cur=cur+i
            self.prefix.append(cur)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left>0 else 0
        return rightSum-leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)