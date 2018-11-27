import time
def login():    #打开界面，延时1s
    print("\n\n\n\t\t\t 学生管理系统 \n\n")
    print("\t\t\t  版本号0.1 \n\n")
    print("\n\n\n\t\t\t 2018年10月17号 \n\n")
    print("\n\n\t\t\t syim \n")

def functionList():        #初始界面
    print("\t\t\t|-------------------------------------------------|\n")
    print("\t\t\t|       *****学生管理系统*****                     |\n")
    print("\t\t\t|-------------------------------------------------|\n")
    print("\t\t\t|            1.学生成绩查看                        |\n")
    print("\t\t\t|            2.增加学生信息                        |\n")
    print("\t\t\t|            3.删除学生信息                        |\n")
    print("\t\t\t|            4.修改学生信息                        |\n")
    print("\t\t\t|            5.查找学生信息                        |\n")
    print("\t\t\t|            6.返回上一级                          |\n")
    print("\t\t\t|            7.退出学生系统                        |\n")
    print("\t\t\t|-------------------------------------------------|\n")

def functionList2():         #定义功能菜单
    print("\t\t\t---1:查看    2:增加    3:删除    4:修改----")
    print("\t\t\t-------5:查找      6:返回      7:退出------")

def sexInputDebug(sexInput):     #判断性别
    if len(sexInput) == 1 and (sexInput.lower() == "m" or sexInput.lower() == "f"):
        return True
    else:
        return False

def ageInputDebug(ageInput):      #判断年龄
    if len(ageInput) == 2 and ageInput.isdigit() == True:
        return True
    else:
        return False

def IDInputDebug(IDInput):         #判断ID
    if len(IDInput) == 8 and IDInput.isdigit() == True:
        return True
    else:
        return False

def nameListFunction():  #学生姓名信息
    nameList = []
    for i in range(len(studentList)):
        if studentList[i]["name"] not in nameList:
            nameList.append(studentList[i]["name"])
    return nameList

def findNameLocation(studentname):   #通过姓名定位学生的位置
    for j in range(len(studentList)):
        if studentList[j]["name"] == studentname:
            return j

def listFunction():        #显示现有的学生
    print("\t\t\t       姓名      性别      年龄      学号      备注      ")
    print("\t\t\t--------------------------------------------------------")
    for i in range(len(studentList)):
        studentInfo = studentList[i]
        print("\t\t\t%10s%10s%10s%10s%10s" %
              (studentInfo["name"],studentInfo["sex"],studentInfo["age"],studentInfo["studentID"],studentInfo["extra"]))

def addFunction():         #定义增加学生函数
    while True:
        numInput = input("-----修改已经存在的学生备注请输入1\n-----------增加一个新的学生请输入2 \n")
        if numInput == "2":
            while True:
                nameNoExistAdd = input("请输入您要增加的名字\n")
                nameList = nameListFunction()
                if nameNoExistAdd in nameList :
                    print("%s在学生系统中已存在\n" % nameNoExistAdd)
                    print("")
                else:
                    newstudent = {}
                    newstudent["name"] = nameNoExistAdd
                    while True:
                        sexInput = input("请输入%s的性别------f:woman --------m:man\n" % nameNoExistAdd)
                        if sexInputDebug(sexInput) == True:
                            newstudent["sex"] = sexInput
                            break
                        else:
                            print("输入错误，请重新输入\n")
                    while True:
                        ageInput = input("请输入%s的年龄\n" % nameNoExistAdd)
                        if ageInputDebug(ageInput) == True:
                            newstudent["age"] = ageInput
                            break
                        else:
                            print("输入错误，请重新输入\n")
                    while True:
                        IDInput = input("请输入%s的学号 ------8位数字\n" % nameNoExistAdd)
                        if IDInputDebug(IDInput) == True:
                            newstudent["studentID"] = IDInput
                            break
                        else:
                            print("输入错误，请重新输入\n")
                    newstudent["extra"] = input("请输入%s的备注\n" % nameNoExistAdd)
                    studentList.append(newstudent)
                    print("-----------%s已添加到学生管理系统\n" % nameNoExistAdd)
                    print("")
                    print("姓名：%s\t性别：%s\t年龄：%s\t学号：%s\t备注：%s\n" %(
                          newstudent["name"],newstudent["sex"],newstudent["age"],newstudent["studentID"],newstudent["extra"]))
                    break
                break
            break
        elif numInput == "1":
            while True:
                nameExistAdd = input("请输入您要修改备注的学生的名字\n")
                nameList = nameListFunction()
                if nameExistAdd in nameList:
                    extraExisAdd = input("请输入%s要修改的备注\n")
                    j = findNameLocation(nameExistAdd)
                    studentList[j]["extra"] = extraExisAdd
                    print("-----------备注已添加-------------")
                    print("")
                    print("姓名：%s\t性别：%s\t年龄：%s\t学号：%s\t备注：%s\n" % (
                        studentList[j]["name"], studentList[j]["sex"], studentList[j]["age"], studentList[j]["studentID"],
                        studentList[j]["extra"]))
                    break
                else:
                    print("-----------您输入的名字不存在\n")
            break
        else:
            print("输入的信息不正确\n")

def delFunction():            #删除学生函数
    while True:
        nameDel = input("请输入需要删除的学生姓名\n")
        studentNameList = nameListFunction()
        if nameDel in studentNameList:
            j = findNameLocation(nameDel)
            del studentList[j]
            print("-------学生%s已从管理系统中删除\n" % nameDel)
            print("")
            break
        else:
            print("学生不存在，请重新输入\n")

def modifiFunction():           #修改学生函数
    while True:
        modifiName = input("请输入需要修改的学生姓名\n")
        studentNameList = nameListFunction()
        if modifiName in studentNameList:
            j = findNameLocation(modifiName)
            print("--------请输入需要修改的内容选项---------")
            print("--------------1：修改姓名---------------")
            print("--------------2：修改性别---------------")
            print("--------------3：修改年龄---------------")
            print("--------------4：修改学号---------------")
            print("--------------5：修改备注---------------\n")
            while True:
                choiceInput = input()
                if choiceInput == "1":
                    newNameInput = input("请输入新名字\n")
                    studentList[j]["name"] = newNameInput
                    print("------姓名已更新-------\n")
                    print("")
                    break
                elif choiceInput == "2":
                    while True:
                        newSexInput = input("请输入新性别\n")
                        if sexInputDebug(newSexInput):
                            studentList[j]["sex"] = newSexInput
                            print("------性别已更新-------\n")
                            print("")
                            break
                        else:
                            print("输入有误\n")
                    break
                elif choiceInput == "3":
                    while True:
                        newAgeInput = input("请输入新年龄\n")
                        if ageInputDebug(newAgeInput):
                            studentList[j]["age"] = newAgeInput
                            print("------年龄已更新-------\n")
                            print("")
                            break
                        else:
                            print("输入有误\n")
                    break
                elif choiceInput == "4":
                    while True:
                        newIDInput = input("请输入新学号\n")
                        if IDInputDebug(newIDInput):
                            studentList[j]["studentID"] = newIDInput
                            print("------性别已更新-------\n")
                            print("")
                            break
                        else:
                            print("输入有误\n")
                    break
                elif choiceInput == "5":
                        newExtraInput = input("请输入新备注\n")
                        studentList[j]["extra"] = newExtraInput
                        print("------备注已更新-------\n")
                        print("")
                        break
                else:
                    print("输入有误，请重新输入\n")
            break
        else:
            print("-------姓名输入有误,请重新输入---------\n")
            print("")

def searchFunction():         #定义搜索学生函数
    nameSearch = input("-----请输入需要查找的姓名-----\n")
    nameList = nameListFunction()
    if nameSearch in nameList:
        print("------%s在学生系统中\n" % nameSearch)
        print("")
        j = findNameLocation(nameSearch)
        print("姓名：%s\t性别：%s\t年龄：%s\t学号：%s\t备注：%s" % (
        studentList[j]["name"], studentList[j]["sex"], studentList[j]["age"], studentList[j]["studentID"],
        studentList[j]["extra"]))
        print("")
    else:
        print("-----%s不在学生系统中,请重新输入------\n" % nameSearch)
        print("")

studentList = [{"name": "Frank", "sex": "f", "age": 33, "studentID": "312312", "extra": ""},
               {"name": "Jane", "sex": "m", "age": 45, "studentID": "324235", "extra": ""}]
login()
time.sleep(1)
functionList()
while True:
    userInput = input("-----------请输入您要选择的功能序号: \n")
    print("")
    if userInput == "1":
        listFunction()
        functionList2()
        continue
    elif userInput == "2":
        addFunction()
        functionList2()
        continue
    elif userInput == "3":
        delFunction()
        functionList2()
        continue
    elif userInput == "4":
        modifiFunction()
        functionList2()
        continue
    elif userInput == "5":
        searchFunction()
        functionList2()
        continue
    elif userInput == "6":
        functionList()
        continue
    elif userInput == "7":
        break
    else:
        print("输入有误")
