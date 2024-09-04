#Q15.3Sum
#https://leetcode.com/problems/3sum/description/
nums = [-1,0,1,2,-1,-4]
new=[]
nums.sort()
for i , a in enumerate(nums):
    if i >0 and a==nums[i-1]:
        continue
        
    l,r=i+1, len(nums)-1
    while l<r:
        threesum= a+nums[l]+nums[r]
        if threesum>0:
            r-=1
        elif threesum<0:
            l+=1
        else:
            new.append([a,nums[l],nums[r]])
            l+=1
            while nums[l]==nums[l-1] and l<r:
                l+=1
print(new)
#sort=o(nlogn)+o(n^2) this is complete o(n^2) as it has 2 loops
#######################################################################################
#Q18.4Sum
#https://leetcode.com/problems/4sum/
        new=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i >0 and nums[i]==nums[i-1]:
                continue       
            for j in range(i+1,len(nums)-2):
                if j >i+1 and nums[j]==nums[j-1]:
                   continue
                
                l,r=j+1, len(nums)-1
                while l<r:
                   foursum= nums[i]+nums[j]+nums[l]+nums[r]
                   if foursum>target:
                       r-=1
                   elif foursum<target:
                       l+=1
                   else:
                       new.append([nums[i],nums[j],nums[l],nums[r]])
                       while l<r and nums[l]==nums[l+1]:
                          l+=1
                       while l<r and nums[r]==nums[r-1]:
                          r-=1
                       l+=1
                       r-=1
        return new
