from flask import Flask,render_template,request,redirect,url_for
from . import main
from ..models import User, Blog, Quote, Comment, Subscriber
from .forms import BlogForm, CommentForm, SubscribeForm, UpdateBio
from flask_login import login_required, current_user
from ..requests import get_quote
from .. import db #photos

@main.route('/')
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    blogs = Blog.get_all_blogs()
    quotes = get_quote()
    return render_template('index.html', title = title, blogs = blogs, quotes = quotes)

@main.route('/user/<uname>', methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form_bio = UpdateBio()

    if form_bio.validate_on_submit():
        user.bio = form_bio.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    #if 'photo' in requestfiles:
    #    filename = photos.save(request.files['photo'])
    #    path = f'photos/{filename}'
    #    user.profile_pic_path = path
    #    db.session.commit()
    #return redirect(url_for('main.profile',uname=user.username))

    
    return render_template("profile/profile.html", user = user, form_bio = form_bio)

@main.route('/create-blog', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    delete = new_blog.clear_blog()

    if blog_form.validate_on_submit():
        id = 'blog'
        title = blog_form.title.data
        content = blog_form.content.data

        new_blog = Blog( title = title, content = content, user = current_user, delete = delete)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    
    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = blog_form)

@main.route('/comment', methods = ['GET','POST'])
def new_comment():
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        name = comment_form.name.data

        new_comment = Comment(comment = comment, name = name)

        new_comment.save_comment()
        return redirect(url_for('main.new_comment'))    

    comments = Comment.get_comments()
    
    title = 'Comments'
    return render_template('comment.html', title = title, comment_form = comment_form, comments = comments)

@main.route('/subscribe', methods = ['GET','POST'])
def new_subsciber():
    subscribe_form = SubscribeForm()

    if subscribe_form.validate_on_submit():
        email = subscribe_form.email.data

        new_subsciber = Subscriber(email = email)

        new_subsciber.save_subscriber()
        return redirect(url_for('main.new_subscriber'))

    title = 'Subscriber'
    return render_template('subscribe.html', title = title, subscribe_form = subscribe_form)
