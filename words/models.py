from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.db import models


class AbstractModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        verbose_name=_('Created By'),
        related_name='%(class)s_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        verbose_name=_('Updated By'),
        related_name='%(class)s_updated_by'
    )

    class Meta:
        abstract = True


class Word(AbstractModel):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Word"),
    )

    def __str__(self):
        return self.name


class WordMeaning(AbstractModel):
    text_content = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter your text here."),
        max_length=3000,
        verbose_name=_("Text of meaning")
    )

    type = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    words = models.ForeignKey(
        "Word",
        verbose_name=_("Word"),
        related_name='word_meanings',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'meaning of {self.words.name}'


class Author(AbstractModel):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Author"),
    )

    def __str__(self):
        return self.name


class Example(AbstractModel):
    text_content = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter your example here."),
        max_length=3000,
        verbose_name=_("Text of example")
    )
    author = models.ForeignKey(
        "Author",
        blank=True,
        null=True,
        related_name='author_examples',
        verbose_name=_("Author of meaning"),
        on_delete=models.CASCADE,
    )
    meaning = models.ForeignKey(
        "WordMeaning",
        verbose_name=_("Example"),
        related_name='example_meanings',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if self.author:
            return f"example by {self.author.name}"
        else:
            return f"No author"
