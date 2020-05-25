#from openpyxl import load_workbook
#from openpyxl import Workbook
import os
import numpy as np
import cv2

#디렉토리 확인

'''
f= 'a'
ff = 'bb'
test = f +" " +ff
file1.write(test)
file1.close
'''

#메타 데이터 정리
# base_dic = './10_voice_download_5_child_Korean'
# All_file_metadata = open('./all_file_metadata.txt', 'w')

# file_list1 = os.listdir(base_dic)
# print(file_list1[0])


# for item in file_list1 :
#     dic2 = os.path.join(base_dic, str(item))
    
#     #print(item)
#     dic_file = []
#     dic_file.append('G'+str(item)+'_OFC')
#     dic_file.append('I'+str(item)+'_OFC')
#     dic_file.append('M'+str(item)+'_OFC')
#     dic_Label = 'TXT'+str(item)
#     #print(item)
#     dic_each = []
#     for item2 in dic_file :
#         dic_each.append(os.path.join(base_dic, item, item2))
#         #print(dic_each)
    
#     dic_Label = os.path.join(base_dic, item, dic_Label)
#     Label_list = os.listdir(dic_Label)
#     #print(dic_each[0])
#     #print(dic_each[1])
#     #print(dic_each[2])
#     #print(dic_Label)
    
#     dic_each_Label = []
#     for item2 in Label_list :
#         dic_each_Label.append(os.path.join(dic_Label, item2))

#     #print(dic_each_Label)
#     for item2 in dic_each :
#         n =0
#         each_file_list = os.listdir(item2)
#         for item3 in each_file_list :
#             dic_each_file = os.path.join(item2, item3)
#             print(dic_each_file)
#             print(dic_each_Label[n])

#             data = str(dic_each_file) + " " + str(dic_each_Label[n] + '\n')
#             All_file_metadata.write(data)
#             n+=1
    
# All_file_metadata.close()

# metadata shuffle
# path = './all_file_metadata.txt'
# meta_list = []
# with open(path, 'r') as f :
    
#     for line in f.readlines()[0:] :
#         v = line.strip().split()
#         meta_list.append(v)

# import random

# random.shuffle(meta_list)
# All_file_metadata_shuffle = open('./all_file_metadata_shuffle.txt', 'w')
# for item in meta_list :
#     data = str(item[0]) + " " + str(item[1]) +"\n"
#     All_file_metadata_shuffle.write(data)
# All_file_metadata_shuffle.close