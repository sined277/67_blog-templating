# Importing required libraries
from flask import Flask, render_template
import requests
from post import Post

# Retrieving the data from a JSON API endpoint and storing it in a list of dictionaries
posts = requests.get("https://api.npoint.io/6f8b2752f302e4dceae2").json()

# Creating a list of Post objects by iterating over the dictionaries in the above list
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post)

# Initializing the Flask app
app = Flask(__name__)

# Defining a route to display all the blog posts
@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

# Defining a route to display a specific blog post based on its index
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
