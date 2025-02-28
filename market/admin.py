from django.contrib import admin
from .models import Musician, Album, Person, Tank, Human, School, Stuff, Measure, LibraryCard, LibraryBook, \
    BookBorrowing, Student, Course

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Person)
admin.site.register(Tank)
admin.site.register(Human)
admin.site.register(School)
admin.site.register(Stuff)
admin.site.register(Measure)

admin.site.register(Student)
admin.site.register(LibraryCard)
admin.site.register(LibraryBook)
admin.site.register(BookBorrowing)

admin.site.register(Course)
