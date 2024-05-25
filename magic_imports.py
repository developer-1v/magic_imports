import sys, os


'''

NOTE:
    To be properly tested, we must have:
        - Tests located in a file buried deep in subdirectories
        
TODO:
    - combined print statements when adding more than one Import_path
    either via passing multiple path arguments, or via the boolean\
    to print all of the intermediate directories between the 
    target_path and the start_path. 
    - I entered this into Cursor's AI, and didn't get an answer, but
    got enough information to help me: "To modify the easy_imports and _print_easy_imports functions so that multiple import paths are printed under a single "pt.easy_imports():" print statement, you can accumulate all the import messages and print them together at the end of the easy_imports function. Here's how you can adjust your existing functions:"
    - From that prompt, I think I shoudl accumulate the names
    of the import_paths, and if it was successful or failure, and record that on one line
    - Then add all lines that are saved up at the end, and 
    combine them into my "pt.easy_imports():" print statement. 
'''


## Adds the directory from which the script is executed 
# and the current working directory to the module search path.
## '.' refers to the directory from which the script is 
# executed, not necessarily the directory where the 
# Python file is located.
sys.path.append('.')
sys.path.append(os.getcwd())


