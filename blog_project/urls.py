from django.conf.urls import url, include
from django.contrib import admin
from blog.upload import upload_image


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^', include('blog.urls'))
]
