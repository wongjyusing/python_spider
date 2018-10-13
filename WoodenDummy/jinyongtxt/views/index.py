from tornado.web import RequestHandler
from .data import new_txt,txt_detail

class MainHandler(RequestHandler):
    def get(self):
        context = new_txt.books

        self.render('home.html',context=context)

class ChapterHandler(RequestHandler):
    def get(self,chapter_link):
        if chapter_link in new_txt.chapter_list:     #get(chapter_link) == True:
            context = new_txt.chapter_list.get(chapter_link)
            book = {'slug':chapter_link}
            self.render('chapter_list.html',context=context,book=book)
        else:
            self.write('你失败了哟')


class DetailHandler(RequestHandler):
    def get(self,chapter_link,num):
        if chapter_link in new_txt.books and num in txt_detail.detail_list[chapter_link]['chapter_list']:
            context = {}
            context['content'] = txt_detail.detail_list[chapter_link]['chapter_list'][num]
            
            self.render('book_detail.html',context=context)
        else:
            self.write('你失败了哟')
