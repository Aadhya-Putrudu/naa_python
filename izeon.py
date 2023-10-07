
name_list=["Mahesh","Aadhya","Rafi","Shifa"]
domain_list=["@gmail.com","@zohomail.in","@yahoomail.com","@outlook.com"]
name_list2=[]
count=1
for i in name_list:
    j=i[0:-2]+str(count)+str(count+1)
    count+=2
    name_list2.append(j)

for i in range(4):
    print(f"{name_list[i]:<10} {domain_list[i]:<15} {name_list[i]+domain_list[i]:<25} {name_list2[i]+domain_list[i]:<25}")
