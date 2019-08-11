#149th LeetCode Weekly Contest
#Day of the Year
'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''
class Solution(object):
    def dayOfYear(self, date):
        day_month={0:0,1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        month=int()
        answer=int()
        if int(date[:4])%4 !=0 or int(date[:4]) ==1900 : day_month[2]=28
        for k,v in day_month.items():
            if k<=(int(date[5:7])-1):
                month=month+v
        answer=month+int(date[8:])
        return answer