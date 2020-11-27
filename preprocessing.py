import json
# mo file json
with open('train.json', 'r',encoding='utf8') as openfile:
    json_object = json.load(openfile) #  ham .load() tra ve mot list


lst = []
for i in range(len(json_object)):
    tmp = str(json_object[i]['label']) + " " +json_object[i]['question'] +" "+ json_object[i]['title'] +" "+ json_object[i]['text']
    lst.append(tmp)
lst =[
    "True Quang Hải giành được chức vô địch U21 quốc gia năm bao nhiêu tuổi Nguyễn Quang Hải (sinh 1997) Năm 2013 , Nguyễn Quang Hải giành chức vô địch U21 quốc gia 2013 cùng với đội trẻ Hà Nội T&T và tạo nên cú sốc khi trở thành cầu thủ 16 tuổi đầu tiên giành được danh hiệu vô địch U21 quốc gia .",
    "le thi thao linh"
]
with open('nhap.txt', 'w',encoding='utf8') as f:
    for item in lst:
        item = item.split()[0]
        f.write("%s\n" % item)


# for i in range(len(json_object)):
#     dic = {
#         "id": json_object[i]['id'],
#         "question": json_object[i]['question'],
#         "title": json_object[i]['title'],
#         "text": json_object[i]['text'],
#         "label": json_object[i]['label']
#     }
#     lst.append(dic)


# viet vao 1 file json
# with open('trainpre.json', 'w', encoding='utf-8') as f:
#     json.dump(lst, f, ensure_ascii=False, indent=4)