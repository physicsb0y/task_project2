from django.urls import path

from .views import IndexView, AboutView, JobPostView, JobListView, JobDescriptionView, BlogCreateView, BlogPage, SingleBlogView, contact, SearchView, JobSearchView, JobApplicationView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('createjob', JobPostView.as_view(), name='create_job'),
    path('joblist/', JobListView.as_view(), name='job_list'),
    path('joblist/jobdescription/<int:pk>', JobDescriptionView.as_view(), name='job_detail'),
    path('jobapply/', JobApplicationView.as_view(), name='apply_job'),
    path('blog', BlogPage.as_view(), name='blog_page'),
    path('blog/<int:pk>', SingleBlogView.as_view(), name='blog_content'),
    path('blog/blog_create', BlogCreateView.as_view(), name='create_blog'),
    path('contact', contact, name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('jobsearch', JobSearchView.as_view(), name='job_search'),
]
