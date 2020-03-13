class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        #参考：https://www.cnblogs.com/grandyang/p/8503476.html
        #先排序，以右边界为关键字排序，右边界相同的，按左边界降序排序，先处理长度较小的区间
        intervals.sort(key = lambda x:(x[1],-x[0]))
        #print(intervals)

        #贪心算法，遍历数组。
        #分三种情况，1二者完全没有交集，2二者有一个数字的交集，3有两个以上的数字交集。
        li = [-1,-1]
        for x in intervals:
            if x[0] <= li[-2]:
                continue
            if x[0] > li[-1]:
                li.append(x[1]-1)
            li.append(x[1])
            #print(li)

        return len(li) - 2

obj=Solution()
print(obj.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))