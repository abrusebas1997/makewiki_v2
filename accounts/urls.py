from django.urls import path, include
from wiki.views import PageListView, PageDetailView
from accounts.views import SignUpView



urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('signup/', SignUpView.as_view(), name='templates-signup-page'),
    # path('newpage/' PageCreateView.as_view(), name='wiki-create-page')
    path('accounts/', include('django.contrib.auth.urls')),
]
