from django.test import TestCase
from suggestionbox.models import *
from django.contrib.auth.models import User

# Create your tests here
class SuggestionBoxTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.feedback = UserFeedback.objects.create(
            user=self.user,
            username=self.user.username,
            feedback='test',
            reply='test',
        )

    def test_feedback(self):
        self.assertEqual(self.feedback.feedback, 'test')
        self.assertEqual(self.feedback.reply, 'test')

    def test_user(self):
        self.assertEqual(self.user.username, 'test')

    def test_user_feedback(self):
        self.assertEqual(self.feedback.user, self.user)
        self.assertEqual(self.feedback.username, self.user.username)

    def test_reply_feedback(self):
        self.feedback.reply = 'test reply'
        self.feedback.save()
        self.assertEqual(self.feedback.reply, 'test reply')

    def test_delete_feedback(self):
        self.feedback.delete()
        self.assertEqual(UserFeedback.objects.count(), 0)


