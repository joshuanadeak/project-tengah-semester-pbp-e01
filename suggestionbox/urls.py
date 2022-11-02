import suggestionbox.views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'suggestionbox'

urlpatterns = [
    path('', suggestionbox.views.showFeedback, name='showFeedback'),
    path('giveFeedback/', suggestionbox.views.giveFeedback, name='giveFeedback'),
    path('replyFeedback/<str:id>/', suggestionbox.views.replyFeedback, name='replyFeedback'),
    path('showJson/', suggestionbox.views.showJson, name='showJson'),
    path('deleteFeedback/<str:id>/', suggestionbox.views.deleteFeedback, name='deleteFeedback'),
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)