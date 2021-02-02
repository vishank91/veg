from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages import success,error
from django.contrib.auth.forms import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import *
def home(request):
    feed=Feedback.objects.all()
    return render(request,"index.html",{"Feed":feed})

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def plans(request):
    data=Plan.objects.all()
    return render(request,"plans.html",{"Data":data})

def contact(request):
    if(request.method=="POST"):
        try:
            contact=ContactUs()
            contact.name=request.POST.get('Name')
            contact.phone=request.POST.get('Phone')
            contact.email=request.POST.get('Email')
            contact.message=request.POST.get('Message')
            contact.save()
            success(request,"Your Request Submitted")
        except:
            error(request,"Something Went Wrong")
    return render(request,"contact.html")

def news(request):
    return render(request,"blog.html")


@login_required(login_url='/login/')
def feedback(request):
    if(request.method=='POST'):
        feed=Feedback()
        feed.message=request.POST.get('Message')
        feed.save()
        success("Your FeedBack is Saved")
    return render(request,"feedback.html")

def member(request):
    return render(request,"member.html")

def register(request,pid):
    p=Plan.objects.get(pid=pid)
    if(request.method=="POST"):
        m=Member()
        fname=m.name=request.POST.get('Name')
        m.adhar=request.POST.get('Adhar')
        m.pan=request.POST.get('Pan')
        pi=request.POST.get('Parent')
        if(pi==None or int(pi)==0):
            m.parentId=0
        else:
            m.parentId=int(pi)
            parent=Member.objects.get(mid=m.parentId)
        gpi = request.POST.get('gParent')
        if (gpi == None or int(gpi)==0):
            m.gpid = 0
        else:
            m.gpid = int(gpi)
        uemail=m.email=request.POST.get('Email')
        pward=m.password=request.POST.get('Password')
        m.photo=request.FILES.get('img')
        m.planDetails=p
        m.mobile=request.POST.get('Phone')
        uname=m.userName=request.POST.get('User')
        User.objects.create_user(username=uname,
                                 first_name=fname,
                                 email=uemail,
                                 password=pward, )
        m.save()
        if(m.parentId != 0):
            parent.childId=m.mid
            parent.save()
        success(request,"Account is Created")
        return HttpResponseRedirect("/login/")
    else:
        return render(request,"register.html",{"Pid":p.name})

def login(request):
    if(request.method=="POST"):
        username=request.POST.get('Name')
        password=request.POST.get('Password')
        try:
            user=auth.authenticate(username=username,password=password)
            auth.login(request, user)
            if(user is not None):
                auth.login(request, user)
                if(user.is_superuser):
                    return HttpResponseRedirect('/adminProfile/')
                else:
                    return HttpResponseRedirect('/profile/')
        except:
            error(request, "Invalid User Name of Password")
            return HttpResponseRedirect('/login/')
    return render(request,"login.html")

@login_required(login_url='/login/')
def adminProfile(request):
    user=request.user
    if(not user.is_superuser):
        return HttpResponseRedirect('/profile/')
    m=Member.objects.all()
    data=[]
    for i in m:
        plan=Plan.objects.get(pid=i.planDetails.pid)
        if((i.boosted==True and i.day>plan.boostedDays) or (i.boosted==False and i.day>plan.payoutNormal)):
            data.append(i)
    return render(request,"adminProfile.html",{"Data":data,"Data2":m})

@login_required(login_url='/login/')
def profile(request):
    m = Member.objects.filter(userName=request.user)
    if(m[0].leftId==0):
        lc = None
    else:
        lc = Member.objects.get(mid=m[0].leftId)
    if(m[0].rightId==0):
        rc = None
    else:
        rc = Member.objects.get(mid=m[0].rightId)
    if(m[0].gleftleftId==0):
        llc = None
    else:
        llc = Member.objects.get(mid=m[0].gleftleftId)
    if(m[0].gleftrightId==0):
        lrc = None
    else:
        lrc = Member.objects.get(mid=m[0].gleftrightId)
    if(m[0].grightleftId==0):
        rlc = None
    else:
        rlc = Member.objects.get(mid=m[0].grightleftId)
    if(m[0].grightrightId==0):
        rrc = None
    else:
        rrc = Member.objects.get(mid=m[0].grightrightId)
    return render(request,"profile.html",{"Member":m[0],
                                          "Left":lc,
                                          "Right":rc,
                                          "LeftLeft":llc,
                                          "LeftRight":llc,
                                          "RightLeft":rlc,
                                          "RightRight":rrc
                                          })

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def updateAll(request):
    user = request.user
    if (not user.is_superuser):
        return HttpResponseRedirect('/profile/')
    m=Member.objects.all()
    for i in m:
        if(i.status==False):
            continue
        total=0
        plan=Plan.objects.get(pid=i.planDetails.pid)
        if((i.boosted==False and i.day<plan.normalDays) or i.day<plan.boostedDays):
            if(i.boosted==False):
                total+=plan.payoutNormal
            else:
                total+=plan.payoutBoosted
            if(i.maching==True):
                left  = Member.objects.get(mid=i.leftId)
                right = Member.objects.get(mid=i.rightId)
                if(left.payWithdrawable<=right.payWithdrawable):
                    total=total+left.payWithdrawable//100*5
                else:
                    total=total + right.payWithdrawable // 100 * 5
            if(total>plan.price*50//100):
                total=plan.price
            i.payOutTotal+=total
            i.payWithdrawable+=total
            i.day+=1
            i.save()
    return HttpResponseRedirect("/adminProfile/")

@login_required(login_url='/login/')
def updateProfile(request,num):
    m=Member.objects.get(mid=num)
    if(request.method=="POST"):
        m.name=request.POST.get('Name')
        m.email=request.POST.get('Email')
        m.mobile=request.POST.get('Phone')
        img=request.FILES.get('img')
        if(img is not None):
            m.photo=img
        m.save()
        return HttpResponseRedirect("/profile/")
    return render(request,"updateprofile.html",{"Member":m})

@login_required(login_url='/login/')
def updateBankDetails(request,num):
    m=Member.objects.get(mid=num)
    if(request.method=="POST"):
        m.accountNumber=request.POST.get('accnumber')
        m.ifscCode=request.POST.get('ifsc')
        m.bankName=request.POST.get('bankname')
        m.save()
        return HttpResponseRedirect("/profile/")
    return render(request,"bankdetails.html")

@login_required(login_url='/login/')
def binary(request,p,c):
    child=Member.objects.get(mid=c)
    m = Member.objects.get(mid=p)
    if(request.method=="POST"):
        selected = request.POST.get("option")
        if(selected=="1"):
            m.leftId=child.mid
            m.leftChild=True
        else:
            m.rightId=child.mid
            m.rightChild=True

        if(m.leftChild==True and m.rightChild==True):
            lchild=Member.objects.get(mid=m.leftId)
            rchild = Member.objects.get(mid=m.rightId)
            if(m.planDetails.price<=lchild.planDetails.price and m.planDetails.price<=rchild.planDetails.price and m.day<=7):
                m.boosted=True
        if(child.gpid !=0):
            gparent=Member.objects.get(mid=child.gpid)
            if(gparent.boosted==True and gparent.planDetails.price<=child.planDetails.price):
                gparent.maching=True
            else:
                child.gpid=m.parentId
        elif(m.parentId != 0):
            gparent = Member.objects.get(mid=m.parentId)
            child.gpid=gparent.mid
        else:
            gparent=0
        if(gparent!=0 and gparent.leftId !=0 and gparent.leftId==m.mid and child.mid==m.leftId):
            gparent.gleftleftId=child.mid
        elif(gparent!=0 and gparent.leftId !=0 and gparent.leftId==m.mid):
            gparent.gleftrightId=child.mid
        elif (gparent!=0 and gparent.rightId != 0 and gparent.rightId == m.mid and child.mid == m.leftId):
            gparent.grightleftId = child.mid
        elif (gparent!=0 and gparent.rightId != 0 and gparent.rightId == m.mid):
            gparent.grightrightId = child.mid

        m.adjustBinary=False
        m.save(update_fields=['leftId','leftChild','rightId','rightChild','boosted','adjustBinary'])
        child.save(update_fields=['parentId','gpid'])
        if(gparent!=0):
            gparent.save(update_fields=['gleftleftId', 'gleftrightId','grightleftId', 'grightrightId','maching'])
        return HttpResponseRedirect('/profile/')
    return render(request,"binary.html",{"Parent":m,"Child":child})

@login_required(login_url='/login/')
def deactivateAccount(request):
    user = request.user
    if (not user.is_superuser):
        return HttpResponseRedirect('/profile/')
    m = Member.objects.all()
    for i in m:
        plan = Plan.objects.get(pid=i.planDetails.pid)
        if ((i.boosted == True and i.day > plan.boostedDays) or (i.boosted == False and i.day > plan.payoutNormal)):
            i.status=False
            i.save()
    return HttpResponseRedirect('/adminProfile/')

@login_required(login_url='/login/')
def resetAll(request):
    user = request.user
    if (not user.is_superuser):
        return HttpResponseRedirect('/profile/')
    m=Member.objects.all()
    for i in m:
        i.payWithdrawable=0
        i.save()
    return HttpResponseRedirect('/adminProfile/')

@login_required(login_url='/login/')
def activate(request,num):
    user = request.user
    if (not user.is_superuser):
        return HttpResponseRedirect('/profile/')
    m=Member.objects.get(mid=num)
    if(m.parentId!=0):
        p=Member.objects.get(mid=m.parentId)
        p.adjustBinary=True
        p.save()
    m.status=True
    m.save()
    return HttpResponseRedirect('/adminProfile/')
# def sample():
#     if (m.parentId != 0):
#         parent = Member.objects.get(mid=m.parentId)
#         if (parent.parentId != 0):
#             gparent = Member.objects.get(mid=parent.parentId)
#         else:
#             gparent = 0
#         if (parent.leftChild == 0):
#             parent.leftId = m.mid
#             parent.leftChild = True
#             parent.save(update_fields=['leftId', 'leftChild'])
#             if (gparent != 0 and gparent.leftId == parent.mid):
#                 gparent.gleftleftId = m.mid
#                 gparent.save()
#             elif (gparent != 0):
#                 gparent.rightleftId = m.mid
#                 gparent.save()
#         elif (parent.rightChild == 0):
#             parent.rightId = m.mid
#             parent.rightChild = True
#             parent.boosted = True
#             parent.save()
#             if (gparent != 0 and gparent.rightId == parent.mid):
#                 gparent.grightleftId = m.mid
#                 gparent.save()
#             elif (gparent != 0):
#                 gparent.rightrightId = m.mid
#                 gparent.save()