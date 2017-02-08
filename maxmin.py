def find_max_min(num):
  if min(num)!=max(num):
    num_list=[]
    num_list.append(min(num))
    num_list.append(max(num))
    return num_list
  else:
    num_list=[]
    num_list.append(len(num))
return num_list