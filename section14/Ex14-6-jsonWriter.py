'''


JSON(JavaScript Object Notation)
    데이터를 키와 값의 쌍을 중괄호({})로 묶엎표현하는 형식
    - 딕셔너리와 비슷하다
    - 구조{ K : V }
'''
import json

dict_list = [
    {
        'name':'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'alice',
        'age':21,
        'spec':[
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list)

with open('dictList.json','w') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')

