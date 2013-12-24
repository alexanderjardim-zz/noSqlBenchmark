from flask import Flask
from flask import render_template
from ItemService import *

app = Flask(__name__)


@app.route('/')
@app.route('/mock')
def index():
    service = ItemServiceMock()
    return render_template('index.html', items=service.list())

@app.route('/redis')
def redis_index():
    service = ItemServiceRedis()
    return render_template('index.html', items=service.list())

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
