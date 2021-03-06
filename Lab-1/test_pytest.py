import main
## @package root
# Documentation for a function.
# \test function from main.py 
def testing_sum():
     assert main.run('test_sum.txt')==5
def testing_sub():
     assert main.run('test_sub.txt')==-1
def testing_mul():
     assert main.run('test_mul.txt')==6
def testing_del():
     assert main.run('test_del.txt')==0