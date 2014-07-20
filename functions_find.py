def find(ori_string,old_sub,new_sub):
  
  count=0
  
  for number in range (len(old_sub)-1,len(ori_string)):#for loop runs from 0 index to the remaining length of the string.
  
    chunk_start=number
  #  print chunk_start
    inch=len(old_sub)-chunk_start# should be the length of old_sub
    chunk=ori_string[chunk_start:inch]
  
    if chunk==old_sub:
        count=count+1
        print count
        new_sub=ori_string[chunk_start]
  
  else:
       print"blah"
  
