## @package root
# Documentation for a function.
# @param file_name string
# \return int
def run(file_name):
     f=open(file_name)
     a, b= list(map(int, f.readline().split()))
     c=f.readline()
     if c=='+':
          return a+b
     elif c=='-':
          return a-b
     elif c=='*':
          return a*b
     elif c=='/':
          return a//b
run('test_sum.txt')




