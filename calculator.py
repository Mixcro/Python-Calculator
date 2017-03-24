def CheckInv(input):
    """确认输入字符的合法性"""
    INV=""
    for i in range(0,len(input)):
        if input[i] in ["+","-","*","/","^","%","(",")"," ","."]:
            pass
        elif input[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            pass
        else:
            INV=INV+str(input[i])+" "
    return INV

def TypeCheck(object):
    """确定对象为操作符或操作数"""
    try:
        float(object)
        return 1
    except:
        return 0

def Priority(char):
    """确定操作符的优先级"""
    if char in ["+","-"]:
        return 1
    elif char in ["*","/","%"]:
        return 2
    elif char in ["^"]:
        return 3
    elif char in ["(",")"]:
        return 0

def SYA(crr,L=None):
    """调度场算法"""
    if L==None:
        arr,brr=[],[]
    for i in range(0,len(crr)):
        char=crr[i]
        if TypeCheck(char) == 1:
            brr.append(char)
        elif char in ["+","-","*","/","^","%"]:
            while arr!= []:
                if Priority(char) <= Priority(arr[-1]) and Priority(arr[-1]) != 3:
                   brr.append(arr.pop())
                else:
                   break
            arr.append(char)
        elif char == "(":
            arr.append(char)
        elif char == ")":
            while arr[-1] != "(":
                brr.append(arr.pop())
            arr.pop()
    while arr != []:
        brr.append(arr.pop())
    return brr

def RPN(arr,L=None):
    """逆波兰求值"""
    if L==None:
        brr=[]
    for i in range(0,len(arr)):
        if TypeCheck(arr[i]) == 1:
            brr.append(float(arr[i]))
        else:
            tempa,tempb=brr.pop(),brr.pop()
            if arr[i] == "+":
                brr.append(tempb+tempa)
            elif arr[i] == "-":
                brr.append(tempb-tempa)
            elif arr[i] == "*":
                brr.append(tempb*tempa)
            elif arr[i] == "/":
                brr.append(tempb/tempa)
            elif arr[i] == "%":
                brr.append(tempb%tempa)
            elif arr[i] == "^":
                brr.append(tempb**tempa)
    if len(brr)==1:
        return brr[0]
    else:
        return "ERROR"
        
print("一个用python3写的简单计算器")
print("支持运算符{\"+\",\"-\",\"*\",\"/\",\"%（取余）\",\"^（次方）\",\"(\",\")\"},空格将被忽略")
print("一个例子:((2+3)*2)/2^2")

while True:
    print()
    ORI=input("请输入算式:")
    tmp,crr="",[]
    if CheckInv(ORI) != "":
        print("Warming! “"+str(CheckInv(ORI))+"” may crash the program")
    ORI=ORI+"~" #结束符
    for i in range(0,len(ORI)):
        if ORI[i] in ["+","-","*","/","%","^","(",")"]:
            if tmp != "":
                crr.append(tmp)
                tmp=""
            crr.append(ORI[i])
        elif ORI[i] == " ":
            pass
        elif ORI[i] == "~":
            if tmp != "":
                crr.append(tmp)
        else:
            tmp=tmp+ORI[i]
    print("Result:"+str(RPN(SYA(crr))))