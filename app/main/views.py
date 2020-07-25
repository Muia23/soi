from flask import render_template,request,redirect,url_for
from . import main
from ..models import Blog
from .forms import BlogForm

@main.route('/')
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    
    return render_template('index.html', title = title)

@main.route('/create-blog')
def new_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        title = pitch_form.title.data
        content = pitch_form.content.data

        new_blog = Blog(id = id, title = title, content = content)