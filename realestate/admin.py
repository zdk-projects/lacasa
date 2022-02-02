from django.contrib import admin
from realestate.models import AboutUs, HouseListing, Agent, Team, Achievement


class StateAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'show_phone_number', 'second_phone_number')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True
    active.boolean = True

    # def has_delete_permission(self, request, obj=None):
    #     return False
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        # or
        extra_context['really_hide_save_and_add_another_damnit'] = True
        return super(StateAdmin, self).change_view(request, object_id,
                                                   form_url, extra_context=extra_context)

    def has_add_permission(self, request):
        if AboutUs.objects.count() > 0:
            return False
        else:
            return True


admin.site.register(AboutUs, StateAdmin)

admin.site.register(Agent)
admin.site.register(HouseListing)
admin.site.register(Team)
admin.site.register(Achievement)
