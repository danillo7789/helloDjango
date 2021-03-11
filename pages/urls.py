# to power url patterns
from django.urls import path
#to import the homePageview form our views
from .views import homePageView, dashboardView, authorPage, postPage
#from .views import dashboardView
#from .views import authorPage

urlpatterns = [
    path("", homePageView),
    path("dashboard", dashboardView),
    path("authors", authorPage),
    path("authors/posts", postPage)
]