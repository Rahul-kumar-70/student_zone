from django.db import models

class StudentPG(models.Model):
    Inrollment_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=64,null=False)
    AdharCard=models.BigIntegerField()
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=64)
    course_choice=[
        ('M.C.A','Master of computer Applications'),('M.Pol.Sc.','Master of Political Science'),
        ('MTS','Master of Tribal Studies'),('M.Soc.','Master of Sociology'),('MSW','Master of Social Work'),
        ('M.P.Ed.','Master of Physical Education')
    ]
    course=models.CharField(max_length=40,null=False,choices=course_choice)
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    Gender=models.CharField(max_length=10,choices=gender_choice)
    Semester_choice=[
        ('1','First'),('2','Second'),('3','Third'),('4','Four')
    ]
    Semester=models.CharField(null=False, max_length=10,choices=Semester_choice)
    photo = models.ImageField(upload_to='student_pics/', null=False)
    signature = models.ImageField(upload_to='student_signatures/', null=False,)
    Fee=models.FloatField(null=False)
    
class StudentPhd(models.Model):
    Inrollment_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=64,null=False)
    AdharCard=models.BigIntegerField(null=False,unique=True)
    Mobile=models.BigIntegerField(null=False)
    Address=models.CharField(max_length=64,null=False)
    course_choice=[
        ('PhD-CS','Phd computer science'),('PhD.Pol.Sci.','Phd Political Science'),
        ('PhD-TS','Phd Tribal Studies'),('PhD-SW','Phd Social Work'),
        ('PhD-PE','Phd in Physical Education')
    ]
    course=models.CharField(max_length=40,null=False,choices=course_choice)
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    Gender=models.CharField(max_length=10,choices=gender_choice)
    Semester_choice=[
        ('1','First'),('2','Second'),('3','Third'),('4','Four'),('5','Five'),('6','Six')
    ]
    Semester=models.CharField(null=False, max_length=10,choices=Semester_choice)
    photo = models.ImageField(upload_to='phd_student_pics/', null=False)
    signature = models.ImageField(upload_to='studentphd_signatures/', null=False,)
    Fee=models.FloatField(null=False)

class StudentEquery(models.Model):
    Name=models.CharField(max_length=64,null=False)
    Mobile=models.BigIntegerField(null=False)
    Email_id=models.CharField(max_length=64,null=False)
    Course=models.CharField(max_length=64,null=False)
    Address=models.CharField(max_length=64,null=False)


class Marksheet(models.Model):
    Inrollment_no = models.IntegerField(unique=True,null=True)
    student_name = models.CharField(max_length=64,null=True)
    course_choice=[
        ('M.C.A','Master of computer Applications'),('M.Pol.Sc.','Master of Political Science'),
        ('MTS','Master of Tribal Studies'),('M.Soc.','Master of Sociology'),('MSW','Master of Social Work'),
        ('M.P.Ed.','Master of Physical Education'),('PhD-CS','Phd computer science'),('PhD.Pol.Sci.','Phd Political Science'),
        ('PhD-TS','Phd Tribal Studies'),('PhD-SW','Phd Social Work'),
        ('PhD-PE','Phd in Physical Education')
    ]
    Course = models.CharField(max_length=40, choices=course_choice,null=True)
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    Gender = models.CharField(max_length=10, choices=gender_choice,null=True)
    Semester_choice=[
        ('1','First'),('2','Second'),('3','Third'),('4','Four')
    ]
    Semester=models.CharField(null=True, max_length=10,choices=Semester_choice)
    Subject_1 = models.IntegerField()
    Subject_2 = models.IntegerField()
    Subject_3 = models.IntegerField()
    Subject_4 = models.IntegerField()
    Subject_5 = models.IntegerField()

    Total_Obtained = models.IntegerField(editable=False, default=0)
    Total_Marks = models.IntegerField(editable=False, default=500)
    Percentage = models.DecimalField(max_digits=5, decimal_places=2, editable=False, default=0.00)
    status = models.CharField(max_length=10, editable=False, default='Fail')

    def save(self, *args, **kwargs):
        self.Total_Obtained = self.Subject_1 + self.Subject_2 + self.Subject_3 + self.Subject_4 + self.Subject_5
        self.Percentage = (self.Total_Obtained / 500) * 100
        if (self.Subject_1 >= 40 and self.Subject_2 >= 40 and 
            self.Subject_3 >= 40 and self.Subject_4 >= 40 and self.Subject_5 >= 40):
            self.status = 'Pass'
        else:
            self.status = 'Fail'
        super().save(*args, **kwargs)


