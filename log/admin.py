from django.contrib import admin
from log.models import Subquestion,Mcqquestion
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
class SubquestionAdmin(admin.ModelAdmin):
	search_fields = ['question']
class McqquestionAdmin(admin.ModelAdmin):
	search_fields = ['question']
class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Questionator')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Questionator administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Questionator administration')
admin.site.register(Subquestion, SubquestionAdmin)
admin.site.register(Mcqquestion, McqquestionAdmin)