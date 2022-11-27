# 建立類別class
# class Cars:
#     pass
# #建立物件odject
# audi=Cars() #建立Cars類別的物件
# #負責儲存物件(Object)得資訊
# audi.color='blue' 
# audi.seat=4
# print(isinstance(audi, Cars)) #確認物件跟類別之間的關係確認物件跟類別之間的關係
# print(audi.color) #執行結果：執行結果：blue
# print(audi.seat)  #執行結果：4w

# class Cars:
#     #建構式
#     def __init__(self, color,seat):
#         self.color=color
#         self.seat=seat
#         #方法(method)
#     # def move(self,meter):
#     #     print('My car moves'+str(meter)+'meter')
#     def print(self):
#         print("my car's color is"+self.color)
#         print("my car has"+str(self.seat)+'seats')
# audi=Cars('blue',4)
# audi.print()
# # audi.move(5)


# class fullname:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName
# name1=fullname('Andy','wang')
# name2=fullname('Lulu','Cheng')
# print(name1.firstName,name1.lastName)
# print(name2.firstName,name2.lastName)

# class fullname:
#     #建構式
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName

#     def printattribute(self):
#         print("my name is"+self.firstName+','+self.lastName)
# name1=fullname('Andy','wang')
# name1.printattribute()v2

class People:
    pass
Dad=People()
Dad.height=178
Dad.weigh=71
Dad.age=43
print(Dad.height)
print(Dad.weigh)
print(Dad.age)



