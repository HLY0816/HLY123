#coding:gbk
"""
目标：新编一程序，完成RPSLS游戏，即石头剪刀布蜥蜴史波克
作者：黄龙艳
"""
import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(name):
   """
   将游戏对象对应到不同的整数
   """
   if(name == '石头'): 
	   return 0
   elif(name == '史波克'): 
	   return 1
   elif(name == '纸'): 
	   return 2
   elif(name == '蜥蜴'): 
	   return 3
   elif (name=='剪刀'):
	   return 4
   else:
       print("Errer:No Correct Name")
def number_to_name(number):
   """
   将整数(0,1,2,3 or 4)对应到不同的游戏对象
   """
   if(number == 0): 
	   return '石头'
   elif(number == 1):
	   return '史波克'
   elif(number == 2): 
	   return '纸'
   elif(number == 3): 
	   return '蜥蜴'
   elif (number==4):
	   return '剪刀'
   else:print("Errer:No Correct Name")
def rpsls(player_choice):
   """
   用户玩家任意给出一个选择，根据RPSLS游戏规则在屏幕输出对应的结果
   """
   print("------------------")
   print("player_choose"+player_choice)
   player_number=name_to_number(player_choice)#将用户的选择用name_to_number函数表示出来
   comp_number=random.randrange(0,5)#电脑随机产生0-4的随机数
   comp_choice=number_to_name(comp_number)#将计算机的选择用=number_to_name函数表示出来
   print('computer_choice'+comp_choice)
   result=(comp_number-player_number)%5
   if result==0:
	   print("您和计算机出的一样呢")
   elif result==1 or result==2:
	   print("机器赢了")
   elif result==3 or result==4:
	   print("您赢了")
   else:
	   print("Errer:No Correct Name")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
