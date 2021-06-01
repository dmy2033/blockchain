from django.contrib import admin
from chain.models import *


# class BlockAdmin(admin.ModelAdmin):
    # list_display = ('chain.name','age', 'email') # list
    # fields = ('chain', 'data')
# Register your models here.
admin.site.register(Block)
admin.site.register(Chain)
# admin.site.register(Peer)
# admin.site.register(Transactions)