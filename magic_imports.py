import sys, os


'''
'''


## Adds the directory from which the script is executed 
# and the current working directory to the module search path.
## '.' refers to the directory from which the script is 
# executed, not necessarily the directory where the 
# Python file is located.
sys.path.append('.')
sys.path.append(os.getcwd())


