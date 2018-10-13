from views import index

urlpatterns = [
    (r'/', index.MainHandler),
    (r'/(?P<chapter_link>[\w-]+)', index.ChapterHandler),
    (r'/(?P<chapter_link>[\w-]+)/(?P<num>[\w-]+)', index.DetailHandler),

]
