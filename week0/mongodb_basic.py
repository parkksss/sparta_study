# DB 연결
# 패키지 설치 : pymongo, dnsython
from pymongo import MongoClient
client = MongoClient('여기에 URL 입력')
db = client.db

# 데이터 넣기
doc = {
    'name':'bob',
    'age':27
}

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})

# 사용 예시 : 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)
    print(user['age'])      # 'age'만 보기