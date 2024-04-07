from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from books.views import books, about_us, contactus_us
from category.views import (
    create_category,
    category_index,
    update_category,
    delete_category,
    show_category,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("about_us/", about_us, name="about_us"),
    path("contact_us/", contactus_us, name="contactus_us"),
    path("create_category/", create_category, name="create_category"),
    path("category/", category_index, name="category"),
    path("update_category/<int:category_id>/", update_category, name="update_category"),
    path("delete_category/<int:category_id>/", delete_category, name="delete_category"),
    path("show_category/<int:category_id>/", show_category, name="show_category"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
