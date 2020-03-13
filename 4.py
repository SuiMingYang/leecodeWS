def findMedianSortedArrays(nums1, nums2) -> float:
    import math
    tar=nums1+nums2
    tar=sorted(tar)
    length=len(tar)
    if length%2==0:
        return (tar[int(length/2-1)]+tar[int(length/2)])/2
    else:
        return tar[int(math.floor(length/2))]
    



print(findMedianSortedArrays([1,2],[3,4]))