from django.contrib import admin

# Register your models here.
from award_declaration import models


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["org_name", "create_time", "update_time"]


class AwardAdmin(admin.ModelAdmin):
    list_display = ["belonging_org", "award_level", "award_name", "status", "create_time", "start_time", "end_time",
                    "apply_person_num", "award_person_num", "update_time"]




admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Award, AwardAdmin)