import json
import os

path_dir = './1_word/'

print(path_dir)
file_list = os.listdir(path_dir)

print("파일 갯수", len(file_list))

# Train, Test set 분류기 만들어아햠
# 30만:6만으로 무작위 분류
# 레이블도 같이 나눠지도록 조정

#json 파일에서 해당되는 데이터 파싱 (image id, text)
with open('./handwriting_data_info1.json', "r",  encoding='UTF8') as json_file:
    data = json.load(json_file)

parse = data["annotations"]


count =0
for i in range(0,len(parse)) :
    if parse[i]['attributes']['type'] == '단어(어절)' :
        print("image id :", parse[i]['image_id'], 'text :', parse[i]['text'])
        count+=1
print(count)