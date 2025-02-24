from django.shortcuts import render
from.models import Registration,Doctor,Staff,Patients,Booking
from django.contrib.auth.hashers import make_password,check_password 
from  django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import registerserializer
from django.middleware.csrf import get_token
@csrf_exempt
def registrationform(request):
   if request.method=='POST':
      name=request.POST.get('fname')
      email=request.POST.get('femail')
      password=request.POST.get('fpassword')
      phone=request.POST.get('fphone')
      username=request.POST.get('fusername')
      catagory=request.POST.get('fcatagory')

      if Registration.objects.filter(Username=username).exists():
           return JsonResponse({'error':'username already exists'})
      else :
          if catagory=="Doctor":
             Doctor.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
             Registration.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
            #  return JsonResponse({'success':'username registered Successfully'})
          elif catagory=="Staff":
             Staff.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
             Registration.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
             
          elif catagory=="Patients":
             Patients.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
             Registration.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
         #  else:
            #  Booking.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
          
            #  Registration.objects.create(Username=username,Password=make_password(password),Email=email,Phone=phone,Name=name,Catagory=catagory)
          return JsonResponse({'success':'username registered Successfully'})
   else: return JsonResponse({'error':'method is wrong'})  










@csrf_exempt
def loginform(request):
  
   if request.session.get('user_id'):
         return JsonResponse({'message':'USER ALREADY LOGGINED','status':'success','username':request.session.get('username')})

 

   if request.method=="POST":
      username=request.POST.get('fusername')
      password=request.POST.get('fpassword')



      if Registration.objects.filter(Username=username).exists():
             user=Registration.objects.get(Username=username) 
             if username==user.Username and check_password(password,user.Password):
                response=  JsonResponse({'success':'Logined'})

                response.set_cookie('login_cookie','cookie_value',max_age=30)
                request.session['username']=user.Username
                request.session['user_id']=user.id

                csrf_tocken = get_token(request)
                response.set_cookie('csrftocken',csrf_tocken)
                return response
               
             else :
               return JsonResponse({'error':'user not found'})
      else :
         return JsonResponse({'error':'no data'}) 


@csrf_exempt          
def logout(request):
   logout(request)
   response = JsonResponse({'message':'logout'})
   response.delete_cookie('login_cookie')
   response.delete_cookie('csrftocken')
   return response



@csrf_exempt
def displaydetailes(request):
   if request.method == 'POST':
      User_name=request.POST.get('fusername')
      if Registration.objects.filter(Username=User_name).exists():
         userpro=Registration.objects.get(Username=User_name)
         serializer=registerserializer(userpro)
         return JsonResponse({'status':'success','data':serializer.data})
      else :
         return JsonResponse({'error':'User not found'})
   else :
      return JsonResponse({'error':'method is wrong'})
   

   
   
@csrf_exempt
def updatedetailes(request):
   if request.method == 'POST':
     name=request.POST.get('fname')
     email=request.POST.get('femail')
     phone=request.POST.get('fphone')
     username=request.POST.get('fusername')
     catagory=request.POST.get('fcatagory')
     if Registration.objects.filter(Username=username).exists():
        data=Registration.objects.get(Username=username)
        data.Name=name
        data.Email=email
        data.Phone=phone
        data.save()
        if catagory == 'Doctor':
           Doctor.objects.update(Name=name,Email=email,Phone=phone)
        elif catagory  == 'Staff':
           Staff.objects.update(Name=name,Email=email,Phone=phone)
        elif catagory == 'Patients':
           Patients.objects.update(Name=name,Email=email,Phone=phone)
        return JsonResponse({'status':'updated your data'}) 
     else :
        return JsonResponse({'error':'usernot found'})
   else :
      return JsonResponse({'error':'method is wrong'})



@csrf_exempt
def deletedetails(request):
   if request.method == 'POST':
      u_sername = request.post.get('username')
      if Registration.objects.filter(Username=u_sername).exists():
          data =Registration.objects.get(Username=u_sername)
          category = data.Catagory
          if category == 'Doctor':
              Doctor.objects.get(Username=u_sername).delete()
              Registration.objects.get(Username=u_sername).delete()
              return JsonResponse({'status':'your data is successfully deleted'})
          elif category == 'Staff':
              Staff.objects.get(Username=u_sername).delete()
              Registration.objects.get(Username=u_sername).delete()
              return JsonResponse({'status':'your data is successfully deleted'})
          elif category == 'Patients':
               Patients.objects.get(Username=u_sername).delete()
               Registration.objects.get(Username=u_sername).delete()
               return JsonResponse({'status':'your data is successfully deleted'})
          else :
             return JsonResponse({'status':'invalied'})
      else :
         return JsonResponse({'status':'user not found'})
   else:
      return JsonResponse({'status':'method is wrong'})  



@csrf_exempt
def booking(request):
   if  request.method == 'POST':
      name=request.POST.get('fname')
      phone=request.POST.get('fphone')
      age=request.POST.get('fage')
      if Booking.objects.filter(Phone=phone).exists():
       return JsonResponse({'status':'you are already booked'})
      else:
              try:

                 last_tocken = Booking.objects.all().order_by('Tocken').last()
                 new_tocken = last_tocken.Tocken+1
                 Booking.objects.create(Name=name,Phone=phone,Age=age)
                 return HttpResponse(f'Booking is successfull','your tocken number is{new_tocken}')
              except: 
                  Booking.objects.create(Name=name,Phone=phone,Age=age)
                  return HttpResponse(f'Booking is successfull','your tocken number is{1}')
   else:
      return JsonResponse({'error':'method is wrong'})



@csrf_exempt
def deletebooking(request):
   if request.method == 'POST':
      phone=request.POST.get('fphone')
      if Booking.objects.filter(Phone=phone).exists():
         data=Booking.objects.get(Phone=phone).delete()
         return JsonResponse({'success':'Booking has been deleted'})
      else :
         return JsonResponse({'error':'Booking not found'})
      

def search_view(request):
     query = request.GET.get('q')
     if query: 
       result = Registration.objects.filter(Name__icontains=query) | Registration.objects.filter(Username__icontains=query) | Registration.objects.filter(Email__icontains=query) | Registration.objects.filter(Phone__icontains=query)
       result_list = registerserializer(result)
       return JsonResponse({'result':result_list},status=200)
     else:
      return JsonResponse({'results':[]},status=200)
     





   