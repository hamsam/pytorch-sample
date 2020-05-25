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

#기존 파일 dic, 레이블 dic 저장
# metadata shuffle
# path = './all_file_metadata.txt'
# meta_list = []
# with open(path, 'r') as f :
    
#     for line in f.readlines()[0:] :
#         v = line.strip().split()
#         meta_list.append(v)

# import random

#메타 데이터 파일 셔플
# random.shuffle(meta_list)
# All_file_metadata_shuffle = open('./all_file_metadata_shuffle.txt', 'w')
# for item in meta_list :
#     data = str(item[0]) + " " + str(item[1]) +"\n"
#     All_file_metadata_shuffle.write(data)
# All_file_metadata_shuffle.close


# #셔플된 메타 데이터 파일 기반으로, 데이터셋/레이블 파일 분배 및 저장,
import shutil

path = './all_file_metadata_shuffle.txt'

shuffle_meta = []
saved_file_dic = []
with open(path, 'r') as f:
    for line in f.readlines()[0:] :
        v = line.strip().split()
        shuffle_meta.append(v)
        
print(shuffle_meta[0])

train_label = open('./data/train/train_label.txt', 'w', encoding='utf8')
validate_label = open('./data/validate/validate_label.txt', 'w', encoding='utf8')
test_label = open('./data/test/test_label.txt', 'w', encoding='utf8')

ratio_dataset = [11340,2430,2430]
print(sum(ratio_dataset))



count = 1
save_file = train_label
phase = 'train/'

num =0
num2 =0
num_e =[0,0,0]
for item in shuffle_meta :
    split_file_dic = item[0].split('\\')
    only_file_name = split_file_dic[3]
    
    lf = open(item[1], 'r', encoding='UTF8')
    
    label = lf.readline()
    
    sentence = label.strip().split()
    #print(len(word))
    # if len(word) == 1:
    #     num +=1
    # else :
    #     num2+=1
    #     if phase == 'train/' :
    #         num_e[0] +=1
    #     elif phase == 'validate/' :
    #         num_e[1] +=1
    #     elif phase =='test/' :
    #         num_e[2] +=1
    label = ''
    for word in sentence :
        label += word
    #print(label)

    # 각 데이터셋 레이블 파일에 파일 저장될 경로, 실제 레이블 저장
    data = str('./' +only_file_name) + " " + label +"\n"

    save_file.write(data)
    #shutil.copy(item[0], './data/'+phase+only_file_name)
    if count == ratio_dataset[0] :
        save_file = validate_label
        phase = 'validate/'
        
    if count == ratio_dataset[0] +ratio_dataset[1] :
        save_file = test_label
        phase = 'test/'
        
    count+=1

print(num, num2)
print(num_e)
