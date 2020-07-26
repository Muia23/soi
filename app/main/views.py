from flask import Flask,render_template,request,redirect,url_for
from . import main
from ..models import Blog, Quote
from .forms import BlogForm
from flask_login import login_required, current_user
from ..requests import get_quote


@main.route('/')
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    blogs = Blog.get_all_blogs()
    quotes = get_quote()
    return render_template('index.html', title = title, blogs = blogs, quotes = quotes)

@main.route('/create-blog', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        id = 'blog'
        title = blog_form.title.data
        content = blog_form.content.data

        new_blog = Blog( title = title, content = content, user = current_user)

        new_blog.save_blog()
        return redirect(url_for('main.index'))
    
    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = blog_form)
