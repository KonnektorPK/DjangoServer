from django.db import models

class Cabinets(models.Model):
    cabinetsId = models.CharField(
        max_length = 8,
        verbose_name = "location"
    )
    cabinetsName = models.CharField(
        max_length = 14,
        verbose_name = "name"
    )
    xCoord = models.IntegerField(
        verbose_name = "x_coord",
        default = 0
    )
    yCoord = models.IntegerField(
        verbose_name = "y_coord",
        default = 0
    )

class ErrorReport(models.Model):
    file = models.FileField(
        upload_to='error_reports/',
        blank=True,
        null=True
    )
    user = models.CharField(
        max_length=30,
        verbose_name="userName"
    )
    description = models.TextField(
        max_length=400,
        verbose_name="description"
    )
    createdAt = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date"
    )
    is_fixed = models.BooleanField(
        default=False,
        verbose_name="BugFixed"
    )
    # screenshot = models.ImageField(
    #     upload_to='error_reports/',  # Укажите путь, куда сохранять изображения
    #     validators=[validate_file_extension],  # Проверка расширения
    #     verbose_name="Screenshot",
    #     blank=True,  # Делает поле необязательным
    #     null=True
    # )
    def __str__(self):
        return f"{self.user}: {'Fixed' if self.is_fixed else 'Not Fixed'}"