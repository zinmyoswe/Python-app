
employ_file = open("employ.txt","r")
for employee in employ_file.readlines():
# print(employ_file.readline())
# print(employ_file.read())
# print(employ_file.readlines()[3])
    print(employee)

employ_file.close()