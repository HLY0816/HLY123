#coding:gbk
"""
Ŀ�꣺�±�һ�������RPSLS��Ϸ����ʯͷ����������ʷ����
���ߣ�������
"""
import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
   """
   ����Ϸ�����Ӧ����ͬ������
   """
   if(name == 'ʯͷ'): 
	   return 0
   elif(name == 'ʷ����'): 
	   return 1
   elif(name == 'ֽ'): 
	   return 2
   elif(name == '����'): 
	   return 3
   elif (name=='����'):
	   return 4
   else:
       print("Errer:No Correct Name")
def number_to_name(number):
   """
   ������(0,1,2,3 or 4)��Ӧ����ͬ����Ϸ����
   """
   if(number == 0): 
	   return 'ʯͷ'
   elif(number == 1):
	   return 'ʷ����'
   elif(number == 2): 
	   return 'ֽ'
   elif(number == 3): 
	   return '����'
   elif (number==4):
	   return '����'
   else:print("Errer:No Correct Name")
def rpsls(player_choice):
   """
   �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�����Ӧ�Ľ��
   """
   print("------------------")
   print("player_choose"+player_choice)
   player_number=name_to_number(player_choice)#���û���ѡ����name_to_number������ʾ����
   comp_number=random.randrange(0,5)#�����������0-4�������
   comp_choice=number_to_name(comp_number)#���������ѡ����=number_to_name������ʾ����
   print('computer_choice'+comp_choice)
   result=(comp_number-player_number)%5
   if result==0:
	   print("���ͼ��������һ����")
   elif result==1 or result==2:
	   print("����Ӯ��")
   elif result==3 or result==4:
	   print("��Ӯ��")
   else:
	   print("Errer:No Correct Name")
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
