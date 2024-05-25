import os, sys
import inspect
import difflib
from pathlib import Path
import shutil
import textwrap
from print_tricks_delete_test import pt
# pt.easy_imports('PrintTricks')
from z_pt_tests import tests

if __name__ == '__main__':
    from print_tricks_delete_test import pt
    # pt.easy_imports('PrintTricks')
    # pt = MagicImports()


    pt.easy_imports(f'C:\\temp_delete\\pyautogui')

    
    print("\n\n------- Testing with the current working directory... -------")
    pt.easy_imports()
    
    # pt.ex()
    
    print("\n\n------- Testing by looking for a file -------")
    pt.easy_imports('__init__.py')
    
    print("\n\n------- Testing with a specific directory name... -------")
    pt.easy_imports('sg')
    
    print("\n\n------- Testing with a full path (don't put a previous path, or it will quick-exit return)... -------")
    pt.easy_imports('C:\.PythonProjects\TwitchBot')
    
    pt.ex()
    
    print("\n\n------- Testing with a non-existent directory... -------")
    pt.easy_imports('printer trick stuff')
    
    print("\n\n------- Testing with 3 paths as *arguments -------")
    pt.easy_imports('dir1', 'dir2', 'dir3')
    
    print("\n\n------- Testing a List with 3 paths -------")
    pt.easy_imports(['dir4', 'dir5', 'dir6'])
    
    print("\n\n------- Testing a tuple with 3 paths -------")
    pt.easy_imports(('dir7', 'dir8', 'dir9'))
    
    print(f"\n\n------- Testing Something without any similarities -------")
    pt.easy_imports(f"=[;;./[''='[]']] -------")
    
    print(f"\n\n ------- Testing a duplicate import_path -------")
    pt.easy_imports('sg')
    pt.c("   > (Nothing should have been printed because it should have exited immediately) -------")
