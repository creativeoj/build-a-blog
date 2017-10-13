from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


#Add MySQL server connection statement with id and password.


class Blog(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(120))
	content = db.Column(db.String(500))
    #created = db.DateTimeProperty(auto_now_add = True)## oj add 10/11 11:38pm
    

	def __init__(self, title, content):
		self.title = title
		self.content = content

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect('/blog')

@app.route('/blog', methods =['POST', 'GET'])
def blog():
    
    blog_id = request.args.get('id')

    if not blog_id : 
        posts = Blog.query.all()
        return render_template('blog.html', title = 'Build a Blog', posts = posts)
    else:
        added_blog = Blog.query.get(blog_id)
        return render_template('individual.html', title = added_blog.title, blog_content=added_blog.content)

@app.route('/newpost', methods =['POST', 'GET'])
def newpost():

    return render_template('newpost.html', title = 'Add a Blog Entry', blog_title = '', blog_content ='', title_error ='', newBlog_error ='')


@app.route('/add_blog', methods =['POST', 'GET'])
def add_blog():
    title_error = ''
    newBlog_error = ''

    if request.method == 'POST':
        blog_title = request.form['blog_title']
        blog_content = request.form['blog_content']
    #Create error variables.
    
    
    if blog_title == '' :
        title_error = "Please fill in the title."
    
    if blog_content == '' :
        newBlog_error = "Please fill in the body."
    
    if title_error != '' or newBlog_error !='':

        return render_template('newpost.html', title = 'Add a Blog Entry', title_error = title_error, newBlog_error = newBlog_error)
    
    else:
        new_post = Blog(blog_title, blog_content)
        db.session.add(new_post)
        db.session.commit()

        #temp = Blog.query.all()
        #max_id = len(temp)
        return redirect('/blog?id=' +str(new_post.id))

    if blog_title  and  blog_content :
        return redirect(url_for('blog', id = max_id))
        #return redirect(url_for('blog', id = max_id))

#@app.route('/blog?id=<post_id>')
#def nim(post_id):
 #   if request.args: 
  #      print(request.args)

        #post_id =='':
   #     posts = Blog.query.all()
    #    return render_template('blog.html', title = "haha", posts=post)
    #else:
     #   added_blog = Blog.query.get(post_id)
      #  return render_template('individual.html', title = added_blog.title, blog_content=added_blog.content)


if __name__ == '__main__':
    app.run()   