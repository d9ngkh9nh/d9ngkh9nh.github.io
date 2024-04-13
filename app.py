# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database file
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/article1')
def article1():
    return render_template('article1.html')

@app.route('/article2')
def article2():
    return render_template('article2.html')

@app.route('/article3')
def article3():
    return render_template('article3.html')

@app.route('/')
def index():
    blog_posts = BlogPost.query.all()
    return render_template('index.html', blog_posts=blog_posts)

@app.route('/product_dashboard')
def index():
    blog_posts = BlogPost.query.all()
    return render_template('product_dashboard.html', blog_posts=blog_posts)


# Database Setup:
# You'll need a database to store your blog posts. 
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Blog Form and Route:
# Create a form to input blog details and a route to handle the form submission.
class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    submit = SubmitField('Publish')

@app.route('/write', methods=['GET', 'POST'])
def write():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('write.html', form=form)


# # Dynamic route for articles
# @app.route('/article/<int:article_id>')
# def view_article(article_id):
#     # Logic to fetch article content based on article_id
#     # For simplicity, let's assume you have a function get_article_content(article_id)
#     article_content = get_article_content(article_id)
    
#     return render_template('article.html', content=article_content)



if __name__ == '__main__':
    db.create_all()  # This line creates the tables when the script is run
    app.run(debug=True)



