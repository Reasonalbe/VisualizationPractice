import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'http://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的内容
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对每一篇文章都执行一个API调应
    url = ('https"//hacker-news.firebaseio.com/v0/item' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {'title': response_dict['title']}
    submission_dicts.append(submission_dict)
