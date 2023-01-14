import json
import os


def load_posts():
    # загрузит данные из файла
    with open(os.path.join('posts.json'), 'r', encoding='utf-8') as dat:
        data = json.load(dat)
        return data


def get_posts_all():
    return load_posts()



def search_for_posts(query):
    posts_with_word = []
    for post in load_posts():
        if post['content'].lower().find(query.lower()) >= 0:
            posts_with_word.append(post)
    return posts_with_word


def upload_post(post, pic):
    posts = get_posts_all()
    posts.append({"pic": f'../{pic}', "content": post})
    with open('posts.json', 'w') as f:
        js = json.dumps(posts, indent=4)
        f.write(js)

