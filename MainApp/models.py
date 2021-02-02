from django.db import models

class Plan(models.Model):
    pid=models.IntegerField(primary_key=True)
    price=models.IntegerField()
    name=models.CharField(max_length=20)
    payoutNormal=models.IntegerField()
    payoutBoosted=models.IntegerField()
    normalDays=models.IntegerField()
    boostedDays=models.IntegerField()
    capping=models.IntegerField()

    def __str__(self):
        return self.name+str(self.price)

class Member(models.Model):
    userName= models.CharField(max_length=50,unique=True,default="Sample")
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    adhar = models.CharField(max_length=20,default=None,null=True)
    pan = models.CharField(max_length=20,default=None,null=True)
    planDetails=models.ForeignKey(Plan,on_delete=models.CASCADE)
    joiningData=models.DateTimeField(auto_now=True)
    boosted= models.BooleanField(default=False)
    maching= models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    adjustBinary = models.BooleanField(default=False)
    gpid=models.IntegerField(default=0)
    reference=models.BooleanField(default=False)
    leftChild=models.BooleanField(default=False)
    rightChild = models.BooleanField(default=False)
    parentId=models.IntegerField(default=0,blank=True,null=True)
    leftId = models.IntegerField(default=0, blank=True,null=True)
    childId=models.IntegerField(default=0,blank=True,null=True)
    rightId = models.IntegerField(default=0, blank=True,null=True)
    gleftleftId = models.IntegerField(default=0, blank=True, null=True)
    gleftrightId = models.IntegerField(default=0, blank=True, null=True)
    grightleftId = models.IntegerField(default=0, blank=True, null=True)
    grightrightId = models.IntegerField(default=0, blank=True, null=True)
    payOutTotal=models.IntegerField(default=0)
    payWithdrawable=models.IntegerField(default=0)
    mobile = models.CharField(max_length=20)
    photo=models.ImageField(upload_to='images',default=None,null=True)
    email=models.EmailField()
    day=models.IntegerField(default=0)
    accountNumber=models.IntegerField(default=0)
    ifscCode=models.CharField(max_length=50,default=None, blank=True, null=True)
    bankName=models.CharField(max_length=50,default=None, blank=True, null=True)
    def __str__(self):
        return self.name+" "+str(self.mid)
class GuestUser(models.Model):
    gid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)

class ContactUs(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return self.name+" "+self.phone
class Feedback(models.Model):
    memberid=models.ForeignKey(Member,on_delete=models.CASCADE)
    message=models.TextField()
