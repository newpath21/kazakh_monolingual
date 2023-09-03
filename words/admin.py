from django.contrib import admin

from words.models import Author, WordMeaning, Word, Example


# Register your models here.
@admin.register(WordMeaning)
class WordMeaningAdmin(admin.ModelAdmin):
    list_display = ('type', 'words', 'text_content')
    search_fields = ('words',)


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('author', 'meaning')
    search_fields = ('author',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
