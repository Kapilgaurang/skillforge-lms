from django.contrib import admin

from .models import (
    SocialLink,
    TopicCategory,
    TopicContent,
    SiteOption,
    Profile
)

admin.site.register(SocialLink)

admin.site.register(TopicCategory)

admin.site.register(TopicContent)

admin.site.register(SiteOption)

admin.site.register(Profile)