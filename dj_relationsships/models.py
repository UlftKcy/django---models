from django.db import models

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self) :
        return (f"{self.first_name} - {self.last_name}")
    
### One to One Relation
# CASCADE: parent silinirse bu bilgileri de sil.
# PROTECT: CASCADE yerine kullanıldığında; language silinmediği sürece Creator silinemez.
class Language(models.Model):
    first_name = models.CharField(max_length=20)
    creator = models.OneToOneField(Creator,on_delete=models.CASCADE)

    
    def __str__(self) :
        return (f"{self.first_name} - {self.creator}")
    
# Many to One relation olduğu zaman "ForeignKey" kullanıyoruz.
class Frameworks(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    
    def __str__(self) :
        return (f"{self.name} - {self.language}")
    
### Many to Many relationship 
# on_delete metodu yok.
class Programmer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    frameworks = models.ManyToManyField(Frameworks)
    
    def __str__(self) :
        return (f"{self.first_name}")
