#replacesubstring
================

#Give it a string and then search for a substring. Replace that substring with a new substring. 

def find (ori_string, sub_old, sub_new):
    if sub_old in ori_string:        
        print ori_string.count(sub_old)
        
        new_string=ori_string.replace(sub_old, sub_new)
        print new_string
    
    else:
        print 0

-
-
-
