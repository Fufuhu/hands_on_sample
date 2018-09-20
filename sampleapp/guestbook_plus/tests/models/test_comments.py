from guestbook_plus.models.comments import Comment
from guestbook_plus.models.users import Commentator
from django.test import TestCase

class TestComment(TestCase):

    def test_get_thread_single(self):
        commentator = Commentator(
            name="test"
        )
        commentator.save()

        comment = Comment(
            title="test",
            comment="test_comment",
            commentator=commentator,
            parent=None
        )
        comment.save()
        comments = comment.get_thread()

        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0], comment)

        # テストケース終了後の掃除
        commentator.delete()
        comment.delete()
    
    def test_get_thread_multiple(self):
        
        commentators = {}
        for name in ["hoge", "piyo", "fuga", ]:
            commentator = Commentator(
                name=name
            )
            commentator.save()
            commentators[name] = commentator
        
        comments = {}
        for name in ["hoge", "piyo", "fuga", ]:
            comment = Comment(
                title="test",
                comment="test_comment",
                commentator=commentator,
                parent=None
             )
            comment.save()
            comments[name] = comment
        
        comments["piyo"].parent = comments["hoge"]
        comments["piyo"].save()

        thread = comments["piyo"].get_thread()

        self.assertEqual(len(thread), 2)
        self.assertEqual(thread[0], comments["hoge"])
        self.assertEqual(thread[1], comments["piyo"])

        # テストケース終了後のお掃除
        for _, comment in comments.items():
            comment.delete()
        
        for _, commentator in commentators.items():
            commentator.delete()