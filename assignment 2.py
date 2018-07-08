# Create a list with user defined inputs.
l1 = [input('enter the elements:')]
print l1

#  Append the following list in the above created list:
#  ["google","apple","facebook","microsoft","tesla"
l1.append("google")
l1.append("apple")
l1.append("facebook")
l1.append("microsoft")
l1.append("tesla")
print l1

#  Count the number of time an object occurs in the list.
l2 = [1,2,3,5,2,4,1,3,6,4,1,2,5,3,5,4]
print l2.count(1)

# Create a list with numbers and sort it in ascending order.
l3 = [25,14,85,36,12,75,60]
l3.sort()
print l3

# Given are two one dimensional arrays A and B which are sorted in ascending order. write a  program to merge into a single sorted
#array C which contain every elements of A and B

A = [54,63,12,40] #
A.sort() 
print A
B = [78,36,15,23]
B.sort()
print B
C = A+B
C.sort()
print C