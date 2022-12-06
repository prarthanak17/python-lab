list1=["Nature",5,"is",9.06,56,"beautiful",7.34]
print("The original list is:")
print(list1)
res_str=[element for element in list1 if isinstance(element,str)]
res_int=[element for element in list1 if isinstance(element,int)]
res_float=[element for element in list1 if isinstance(element,float)]
print("Integer list is: " +str(res_int))
print("String list is:" +str(res_str))
print("Float list is:" +str(res_float))
