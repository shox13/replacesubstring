def find(ori_string,old_sub,new_sub):
  #ori_string = original string
  #old_sub = old substring
  #new_sub = new substring
    if len(ori_string)>len(old_sub) or len(new_sub):
        for number in range (0,len(ori_string)):
            chunk=ori_string[number:len(old_sub)+number]
            if chunk is old_sub:
                ori_string=ori_string[0:number]+new_sub+ori_string[len(old_sub)+number:len(ori_string)]
            else:
                a=0
        print ori_string
    else:
        print "Not going to work!"
