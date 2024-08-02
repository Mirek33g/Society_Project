# admin.py

from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from . import models


class UserPostFilter(admin.SimpleListFilter):
    title = _('User')
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        users_with_posts = models.User.objects.filter(post__isnull=False).distinct()
        sorted_users = sorted(users_with_posts, key=lambda user: (user.first_name, user.last_name))
        return [(user.id, f"{user.first_name} {user.last_name} ({user.post_set.count()})") for user in sorted_users]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__id=self.value())
        return queryset


class UserAddressFilter(admin.SimpleListFilter):
    title = _('User')
    parameter_name = 'user_post'

    def lookups(self, request, model_admin):
        users_with_address = models.User.objects.filter(address__isnull=False).distinct()
        sorted_users = sorted(users_with_address, key=lambda user: (user.first_name, user.last_name))
        return [(user.id, f"{user.first_name} {user.last_name} ({user.address_set.count()})") for user in sorted_users]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__id=self.value())
        return queryset


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    actions = ['clear_post_amount']
    readonly_fields = ['post_amount']
    list_display = ['last_name', 'first_name', 'email', 'phone', 'registered_at', 'post_amount']
    list_editable = ['email', 'phone']
    list_per_page = 10
    search_fields = ['last_name__istartswith', 'first_name__istartswith', 'last_name', 'first_name']

    @admin.action(description='Clear post amount')
    def clear_post_amount(self, request, queryset):
        updated_count = queryset.update(post_amount=0)
        self.message_user(
            request,
            f'{updated_count} post amount were successfully updated',
            messages.SUCCESS)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['address', 'user_name']
    list_filter = [UserAddressFilter]

    @staticmethod
    def user_name(address):
        url = reverse('admin:playground_user_change', args=[address.user.id])
        return format_html('<a href="{}">{}</a>', url,
                           address.user.first_name + ' ' + address.user.last_name)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['title', 'posted_by', 'description', 'post_type', 'placed_at']
    list_filter = [UserPostFilter]

    @staticmethod
    def posted_by(post):
        url = reverse('admin:playground_user_change', args=[post.user.id])
        return format_html('<a href="{}">{}</a>', url,
                           post.user.first_name + ' ' + post.user.last_name)
