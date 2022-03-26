from pymongo import MongoClient
client = MongoClient('여기에 URL 입력')
db = client.db

# find, update 연습하기

# (1) 영화제목 '가버나움'의 평점을 가져오기
target_movie = db.movies.find_one({'title':'가버나움'})
print(target_movie['star'])

# (2) '가버나움'의 평점과 같은 평점의 영화 제목들을 가져오기
target_star = target_movie['star']
samestar_movies = list(db.movies.find({'star': target_star}, {'_id':False}))
for movie in samestar_movies:
    print(movie['title'])

# (3) '가버나움' 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})