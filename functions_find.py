def find(ori_string,old_sub,new_sub):
  count=0
  for number in range(len(old_sub),len(ori_string)):
    chunk_start=len(ori_string)-number
    print chunk_start
    chunk=ori_string[chunk_start:len(ori_string)-1]
    if chunk==old_sub:
      count=count+1
      ori_string[chunk_start]=new_sub
    else:
       print"blah"
  