from django import test
from django.shortcuts import render
from requests_html import HTML

class TestThreadList(test.TestCase):


    def test_render(self):

        comments = []
        for num in range(4):
            comments.append({
                'comment_id': num,
                'title': 'title'+str(num),
            })
            

        response_param = {
            'comments': comments,
        }
        rendered = render(None, 'thread_list.html', response_param)

        parser = HTML(html=rendered.content.decode())
        elements = parser.find('a')

        for index in range(len(comments)):
            element = elements[index]
            self.assertEqual(element.text, "title"+str(index))
