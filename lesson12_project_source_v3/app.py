from flask import Flask, request, render_template, send_from_directory
from functions import upload_post
import uuid
from functions import get_posts_all
import os
from functions import search_for_posts

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', title='Home', posts=get_posts_all())


@app.route("/list")
def page_tag():
    posts = search_for_posts(request.args.get("s"))
    return render_template('post_list.html', title=f'search by {request.args.get("s")}', len=len(posts), posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/posts", methods=["POST"])
def page_post_upload():
    pic = request.files['picture']
    content = request.values.get('content')
    filename = os.path.join('static/imgs', f'{uuid.uuid4()}.png')
    pic.save(filename)
    upload_post(content, filename)
    return render_template('post_uploaded.html', content=content, pic=filename)


@app.route("/uploads/<path:path>")

def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

