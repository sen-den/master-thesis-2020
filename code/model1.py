class Speciality(DataObject):
    speciality_group = models.ForeignKey(SpecialityGroup)
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
