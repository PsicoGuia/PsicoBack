from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from address.models import AddressField
from address.forms import AddressWidget

from .models import Profile, Studies, Office, Chat, HomeVisit,\
    CategoryPatology, Patology, ProfilePatologyOrCategory,\
    RequestOrderMedicDate, ScheduleAttentionChannel, ImageAttentionChannel, \
    AttentionChannel


@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):
    pass


@admin.register(Studies)
class StudiesAdmin (admin.ModelAdmin):
    list_display = ('getUserName', 'getLevel', 'title')


class StudiesInline(admin.TabularInline):
    model = Studies
    can_delete = False
    verbose_name_plural = 'Estudios'
    fk_name = 'profile'


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    inlines = (StudiesInline, )
    exclude = ['location']

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ProfileInline, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     formfield_overrides = {
#         AddressField: {'widget': AddressWidget(
#           attrs={'style': 'width: 300px;'})}
#     }
#     inlines = (ProfileInline, )
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin,
#            self).get_inline_instances(request, obj)
#     class Media:
#         js = (
#             'js/jquery-3.2.1.min.js'
#         )


admin.site.register(AttentionChannel)
admin.site.register(ScheduleAttentionChannel)
admin.site.register(ImageAttentionChannel)
admin.site.register(Office)
admin.site.register(Chat)
admin.site.register(HomeVisit)
admin.site.register(CategoryPatology)
admin.site.register(Patology)
admin.site.register(ProfilePatologyOrCategory)
admin.site.register(RequestOrderMedicDate)
