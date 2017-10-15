from django.db import models

class Book(models.Model):

    BOOK_TYPES = (
        (u"Hardcover", u'Hardcover'),
        (u"Paperback", u'Paperback'),
        (u"E-book", u'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.CharField(choices=BOOK_TYPES,max_length=120)

    def __str__(self):
        return self.title
