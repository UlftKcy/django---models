from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about_me = models.TextField(null=True, blank=True) # null=True, blank=True=> null veya boş olursa hata veremeyecek.
    image = models.ImageField(null=True, blank=True, upload_to='media/') # images db'e yüklenmez.Sadece ismi görüntülenir.Static files db'e yüklenmiyor.(pip install Pillow)
    register_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    
    # str sayesinde database'deki veriler object olarak görünmeyecektir.str'ye göre gösterir.
    def __str__(self) :
        return (f"{self.number} - {self.first_name}")
    
    # genel optional düzenleme için Meta kullandık.Meta kullanıldığında database'de işlem yapıldığı için makemigrations ve migrate komutları tekrar çalıştırılır.
    class Meta:
        ordering= ["number"]
        verbose_name_plural = "Student_List"
        db_table = "Student_Table"
        
    
    

