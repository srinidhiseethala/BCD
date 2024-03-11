class Solution:
	def countPairs(self, m1, m2, n, x):
		c=0
		s=set()
		for i in m1:
		    for j in i:
		        s.add(j)
		for i in m2:
		    for j in i:
		        if x-j in s:
		            c+=1
		return c
