from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    objects = models.Manager()


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Tank(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30)
    caliber = models.IntegerField()
    penetration = models.IntegerField()
    armor = models.IntegerField()
    crew_amount = models.IntegerField()
    autoloader = models.BooleanField()
    time_reload = models.FloatField()
    date_created = models.DateField()
    nation = models.CharField(max_length=30)


class Human(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=30)
    school = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class School(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Class(models.Model):
    objects = models.Manager()
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    char = models.CharField(max_length=1)


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default="example@example.com")
    birthday = models.DateField()
    password = models.CharField(max_length=257, default="qwerty")
    phone = models.CharField(max_length=12, default="1234567890")

    def publish(self):
        self.save()


class Stuff(models.Model):
    stuff_name = models.CharField(max_length=30)
    stuff_desc = models.CharField(max_length=257)
    photo = models.CharField(max_length=100)
    price = models.IntegerField()

    def publish(self):
        self.save()


from django.db import models


class Measure(models.Model):
    class Measurements(models.TextChoices):
        METERS = 'M', 'М'  # Use string for the first value
        FEET = 'F', 'Ф'
        YARDS = 'Y', 'Я'

    # Define a mapping of float values for each unit
    UNIT_CONVERSION = {
        'M': 1.0,
        'F': 0.3048,
        'Y': 0.9144,
    }

    measurement = models.CharField(
        max_length=1,
        choices=Measurements.choices,
        default=Measurements.METERS
    )

    def get_conversion_factor(self):
        return self.UNIT_CONVERSION[self.measurement]


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField('Course')


class Course(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    students = models.ManyToManyField('Student')


class LibraryCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='library_card')
    issue_date = models.DateField()
    expiration_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Library Card: {self.student.student_card_number}"


class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.author})"


class BookBorrowing(models.Model):
    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE, related_name='borrowed_by')
    borrow_date = models.DateField(auto_now_add=True)
    librarian_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.library_card.student.first_name} {self.library_card.student.last_name}"


class Bb(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
