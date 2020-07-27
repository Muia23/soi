from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title:', validators=[Required()])
    content = TextAreaField('Blog:', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):    
    comment = TextAreaField('Comment:', validators=[Required()])
    name = StringField('Name:')
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):    
    email = StringField('Your Email Address', validators = [Required()])
    subscribe = BooleanField('I choose to subscibe to new post Alert!')
    submit = SubmitField('Submit')
