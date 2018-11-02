#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/10/20 19:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0

示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5


-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    x = m + n
    i = 0
    j = 0
    kk = []
    while i + j < int(x / 2) + 1 and i < m and j < n:
        if nums1[i] <= nums2[j]:
            kk.append(nums1[i])
            i += 1
        else:
            kk.append(nums2[j])
            j += 1
    while i + j < int(x / 2) + 1:
        if i < m:
            kk.append(nums1[i])
            i += 1
        else:
            kk.append(nums2[j])
            j += 1
    if x % 2:
        res = kk[int(x / 2)]
    else:
        res = (kk[int(x / 2 - 1)] + kk[int(x / 2)]) / 2
    idd = int(x / 2)
    print("idd=  ", idd)
    print("all num", x, "   ", len(kk), "  ", kk)
    return res


ss1 = [1, 3]
ss2 = [2]
print(findMedianSortedArrays(ss1, ss2))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))

"""
解决方案
方法：递归法

为了解决这个问题，我们需要理解“中位数的作用是什么”。在统计中，中位数被用来：

    将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。

如果理解了中位数的划分作用，我们就很接近答案了。

首先，让我们在任一位置 iii 将 A\text{A}A 划分成两个部分：

          left_A             |        right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]

由于 A\text{A}A 中有 mmm 个元素， 所以我们有 m+1m+1m+1 种划分的方法（i=0∼mi = 0 \sim mi=0∼m）。

我们知道：

    len(left_A)=i,len(right_A)=m−i\text{len}(\text{left\_A}) = i, \text{len}(\text{right\_A}) = m - ilen(left_A)=i,len(right_A)=m−i.

    注意：当 i=0i = 0i=0 时，left_A\text{left\_A}left_A 为空集， 而当 i=mi = mi=m 时, right_A\text{right\_A}right_A 为空集。

采用同样的方式，我们在任一位置 jjj 将 B\text{B}B 划分成两个部分：


          left_B             |        right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

将 left_A\text{left\_A}left_A 和 left_B\text{left\_B}left_B 放入一个集合，并将 right_A\text{right\_A}right_A 和 right_B\text{right\_B}right_B 放入另一个集合。 再把这两个新的集合分别命名为 left_part\text{left\_part}left_part 和 right_part\text{right\_part}right_part：

          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

如果我们可以确认：

        len(left_part)=len(right_part)\text{len}(\text{left\_part}) = \text{len}(\text{right\_part})len(left_part)=len(right_part)
        max⁡(left_part)≤min⁡(right_part)\max(\text{left\_part}) \leq \min(\text{right\_part})max(left_part)≤min(right_part)

那么，我们已经将 {A,B}\{\text{A}, \text{B}\}{A,B} 中的所有元素划分为相同长度的两个部分，且其中一部分中的元素总是大于另一部分中的元素。那么：

median=max(left_part)+min(right_part)2 \text{median} = \frac{\text{max}(\text{left}\_\text{part}) + \text{min}(\text{right}\_\text{part})}{2} median=2max(left_part)+min(right_part)​

要确保这两个条件，我们只需要保证：

        i+j=m−i+n−ji + j = m - i + n - ji+j=m−i+n−j（或：m−i+n−j+1m - i + n - j + 1m−i+n−j+1） 如果 n≥mn \geq mn≥m，只需要使 i=0∼m,j=m+n+12−i i = 0 \sim m, j = \frac{m + n + 1}{2} - i \\i=0∼m,j=2m+n+1​−i

        B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 以及 A[i−1]≤B[j]\text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j]

ps.1 为了简化分析，我假设 A[i−1],B[j−1],A[i],B[j]\text{A}[i-1], \text{B}[j-1], \text{A}[i], \text{B}[j]A[i−1],B[j−1],A[i],B[j] 总是存在，哪怕出现 i=0i=0i=0，i=mi=mi=m，j=0j=0j=0，或是 j=nj=nj=n 这样的临界条件。 我将在最后讨论如何处理这些临界值。

ps.2 为什么 n≥mn \geq mn≥m？由于0≤i≤m0 \leq i \leq m0≤i≤m 且 j=m+n+12−ij = \frac{m + n + 1}{2} - ij=2m+n+1​−i，我必须确保 jjj 不是负数。如果 n<mn < mn<m，那么 jjj 将可能是负数，而这会造成错误的答案。

所以，我们需要做的是：

    在 [0，m][0，m][0，m] 中搜索并找到目标对象 iii，以使：

    B[j−1]≤A[i]\qquad \text{B}[j-1] \leq \text{A}[i] B[j−1]≤A[i] 且  A[i−1]≤B[j],\ \text{A}[i-1] \leq \text{B}[j],  A[i−1]≤B[j], 其中 j=m+n+12−ij = \frac{m + n + 1}{2} - ij=2m+n+1​−i

接着，我们可以按照以下步骤来进行二叉树搜索：

    设 imin=0\text{imin} = 0imin=0，imax=m\text{imax} = mimax=m, 然后开始在 [imin,imax][\text{imin}, \text{imax}][imin,imax] 中进行搜索。

    令 i=imin+imax2i = \frac{\text{imin} + \text{imax}}{2}i=2imin+imax​， j=m+n+12−ij = \frac{m + n + 1}{2} - ij=2m+n+1​−i

    现在我们有 len(left_part)=len(right_part)\text{len}(\text{left}\_\text{part})=\text{len}(\text{right}\_\text{part})len(left_part)=len(right_part)。 而且我们只会遇到三种情况：

        B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 且 A[i−1]≤B[j]\text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j]：
        这意味着我们找到了目标对象 iii，所以可以停止搜索。

        B[j−1]>A[i]\text{B}[j-1] > \text{A}[i]B[j−1]>A[i]：
        这意味着 A[i]\text{A}[i]A[i] 太小，我们必须调整 iii 以使 B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i]。
        我们可以增大 iii 吗？
              是的，因为当 iii 被增大的时候，jjj 就会被减小。
              因此 B[j−1]\text{B}[j-1]B[j−1] 会减小，而 A[i]\text{A}[i]A[i] 会增大，那么 B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 就可能被满足。
        我们可以减小 iii 吗？
              不行，因为当 iii 被减小的时候，jjj 就会被增大。
              因此 B[j−1]\text{B}[j-1]B[j−1] 会增大，而 A[i]\text{A}[i]A[i] 会减小，那么 B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 就可能不满足。
        所以我们必须增大 iii。也就是说，我们必须将搜索范围调整为 [i+1,imax][i+1, \text{imax}][i+1,imax]。 因此，设 imin=i+1\text{imin} = i+1imin=i+1，并转到步骤 2。

        A[i−1]>B[j]\text{A}[i-1] > \text{B}[j]A[i−1]>B[j]： 这意味着 A[i−1]\text{A}[i-1]A[i−1] 太大，我们必须减小 iii 以使 A[i−1]≤B[j]\text{A}[i-1]\leq \text{B}[j]A[i−1]≤B[j]。 也就是说，我们必须将搜索范围调整为 [imin,i−1][\text{imin}, i-1][imin,i−1]。
        因此，设 imax=i−1\text{imax} = i-1imax=i−1，并转到步骤 2。

当找到目标对象 iii 时，中位数为：

    max⁡(A[i−1],B[j−1]),\max(\text{A}[i-1], \text{B}[j-1]), max(A[i−1],B[j−1]), 当 m+nm + nm+n 为奇数时

    max⁡(A[i−1],B[j−1])+min⁡(A[i],B[j])2,\frac{\max(\text{A}[i-1], \text{B}[j-1]) + \min(\text{A}[i], \text{B}[j])}{2}, 2max(A[i−1],B[j−1])+min(A[i],B[j])​, 当 m+nm + nm+n 为偶数时

现在，让我们来考虑这些临界值 i=0,i=m,j=0,j=ni=0,i=m,j=0,j=ni=0,i=m,j=0,j=n，此时 A[i−1],B[j−1],A[i],B[j]\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]A[i−1],B[j−1],A[i],B[j] 可能不存在。 其实这种情况比你想象的要容易得多。

我们需要做的是确保 max(left_part)≤min(right_part)\text{max}(\text{left}\_\text{part}) \leq \text{min}(\text{right}\_\text{part})max(left_part)≤min(right_part)。 因此，如果 iii 和 jjj 不是临界值（这意味着 A[i−1],B[j−1],A[i],B[j]\text{A}[i-1], \text{B}[j-1],\text{A}[i],\text{B}[j]A[i−1],B[j−1],A[i],B[j] 全部存在）, 那么我们必须同时检查 B[j−1]≤A[i]\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 以及 A[i−1]≤B[j]\text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j] 是否成立。 但是如果 A[i−1],B[j−1],A[i],B[j]\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]A[i−1],B[j−1],A[i],B[j] 中部分不存在，那么我们只需要检查这两个条件中的一个（或不需要检查）。 举个例子，如果 i=0i = 0i=0，那么 A[i−1]\text{A}[i-1]A[i−1] 不存在，我们就不需要检查 A[i−1]≤B[j]\text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j] 是否成立。 所以，我们需要做的是：

    在 [0，m][0，m][0，m] 中搜索并找到目标对象 iii，以使：

    (j=0(j = 0(j=0 or i=mi = mi=m or B[j−1]≤A[i])\text{B}[j-1] \leq \text{A}[i])B[j−1]≤A[i]) 或是 (i=0(i = 0(i=0 or j=nj = nj=n or A[i−1]≤B[j]),\text{A}[i-1] \leq \text{B}[j]),A[i−1]≤B[j]), 其中 j=m+n+12−ij = \frac{m + n + 1}{2} - ij=2m+n+1​−i

在循环搜索中，我们只会遇到三种情况：

        (j=0(j = 0(j=0 or i=mi = mi=m or B[j−1]≤A[i])\text{B}[j-1] \leq \text{A}[i])B[j−1]≤A[i]) 或是
        (i=0(i = 0(i=0 or j=nj = nj=n or A[i−1]≤B[j])\text{A}[i-1] \leq \text{B}[j])A[i−1]≤B[j])
        这意味着 iii 是完美的，我们可以停止搜索。
        j>0j > 0j>0 and i<mi < mi<m and B[j−1]>A[i]\text{B}[j - 1] > \text{A}[i]B[j−1]>A[i]
        这意味着 iii 太小，我们必须增大它。
        i>0i > 0i>0 and j<nj < nj<n and A[i−1]>B[j]\text{A}[i - 1] > \text{B}[j]A[i−1]>B[j]
        这意味着 iii 太大，我们必须减小它。

感谢 @Quentin.chen 指出： i<m  ⟹  j>0i < m \implies j > 0i<m⟹j>0 以及 i>0  ⟹  j<ni > 0 \implies j < ni>0⟹j<n 始终成立，这是因为：

    m≤n,i<m  ⟹  j=m+n+12−i>m+n+12−m≥2m+12−m≥0m \leq n, i < m \implies j = \frac{m+n+1}{2} - i > \frac{m+n+1}{2} - m \geq \frac{2m+1}{2} - m \geq 0m≤n,i<m⟹j=2m+n+1​−i>2m+n+1​−m≥22m+1​−m≥0

    m≤n,i>0  ⟹  j=m+n+12−i<m+n+12≤2n+12≤nm \leq n, i > 0 \implies j = \frac{m+n+1}{2} - i < \frac{m+n+1}{2} \leq \frac{2n+1}{2} \leq nm≤n,i>0⟹j=2m+n+1​−i<2m+n+1​≤22n+1​≤n

所以，在情况 2 和 3中，我们不需要检查 j>0j > 0j>0 或是 j<nj < nj<n 是否成立。
JAVA:
class Solution {
    public double findMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        if (m > n) { // to ensure m<=n
            int[] temp = A; A = B; B = temp;
            int tmp = m; m = n; n = tmp;
        }
        int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            if (i < iMax && B[j-1] > A[i]){
                iMin = i + 1; // i is too small
            }
            else if (i > iMin && A[i-1] > B[j]) {
                iMax = i - 1; // i is too big
            }
            else { // i is perfect
                int maxLeft = 0;
                if (i == 0) { maxLeft = B[j-1]; }
                else if (j == 0) { maxLeft = A[i-1]; }
                else { maxLeft = Math.max(A[i-1], B[j-1]); }
                if ( (m + n) % 2 == 1 ) { return maxLeft; }

                int minRight = 0;
                if (i == m) { minRight = B[j]; }
                else if (j == n) { minRight = A[i]; }
                else { minRight = Math.min(B[j], A[i]); }

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}

Python:
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

复杂度分析

    时间复杂度：O(log⁡(min(m,n)))O\big(\log\big(\text{min}(m,n)\big)\big)O(log(min(m,n)))，
    首先，查找的区间是 [0,m][0, m][0,m]。 而该区间的长度在每次循环之后都会减少为原来的一半。 所以，我们只需要执行 log⁡(m)\log(m)log(m) 次循环。由于我们在每次循环中进行常量次数的操作，所以时间复杂度为 O(log⁡(m))O\big(\log(m)\big)O(log(m))。 由于 m≤nm \leq nm≤n，所以时间复杂度是 O(log⁡(min(m,n)))O\big(\log\big(\text{min}(m,n)\big)\big)O(log(min(m,n)))。

    空间复杂度：O(1)O(1)O(1)， 我们只需要恒定的内存来存储 999 个局部变量， 所以空间复杂度为 O(1)O(1)O(1)。

"""