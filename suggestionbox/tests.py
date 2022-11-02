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

    def test_show_feedback(self):
        response = self.client.get('/suggestionbox/')
        self.assertEqual(response.status_code, 302)

    def test_give_feedback(self):
        response = self.client.post('/suggestionbox/giveFeedback/', {'feedback': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_reply_feedback(self):
        response = self.client.post('/suggestionbox/replyFeedback/1/', {'reply': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_show_json(self):
        response = self.client.get('/suggestionbox/showJson/')
        self.assertEqual(response.status_code, 200)

    def test_delete_feedback(self):
        response = self.client.post('/suggestionbox/deleteFeedback/1/')
        self.assertEqual(response.status_code, 302)
    
