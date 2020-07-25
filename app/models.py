class Blog:
    blog_list = []

    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content

    def save_blog(self):
        Blog.blog_list.append(self)

    @classmethod
    def clear_blogs(cls):
        Blog.blog_list.clear()

    @classmethod
    def get_blogs(cls,id):

        response = []

        for blog in cls.blog_list:
            if blog.id == id:
                response.append(blog)
        return response