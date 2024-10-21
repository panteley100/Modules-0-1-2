grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students) #перевожу множество в список
res=students.sort() #привожу список к алфавитному порядку как в grades
a=grades[0]
a_av=sum(a)/len(a)
b=grades[1]
b_av=sum(b)/len(b)
c=grades[2]
c_av=sum(c)/len(c)
d=grades[3]
d_av=sum(d)/len(d)
e=grades[4]
e_av=sum(e)/len(e)
grades1=[a_av,b_av,c_av,d_av,e_av]
st_and_gr=dict(zip(students,grades1))
print(st_and_gr)