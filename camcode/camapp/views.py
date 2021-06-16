from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
#model
from .models import AddCamera
#Cam CODE
from .camera import VideoCamera, IPWebCam, LiveWebCam
from django.http.response import StreamingHttpResponse
# Create your views here.
def index(request):
    if request.user.is_superuser:
        return render(request,"admin_page.html")
    elif request.user.is_authenticated:
        if request.method=="POST":
            name=request.POST.get('name')
            passw=request.POST.get('password')
            ipadd=request.POST.get('ipaddress')
            camno=request.POST.get('cname')
            fm=AddCamera(Name=name,Password=passw,Ip_Adderss=ipadd,Camera_Number=camno)
            fm.save()
        else:
            return render(request,"index.html")
    return redirect(login)
def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"login.html",{'error':"Invalide User Password"})
    return render(request,"login.html")
def singup(request):
    if request.user.is_superuser:
        f_name=request.POST.get("f_name")
        l_name=request.POST.get("l_name")
        email=request.POST.get("email")
        passw=request.POST.get("password")
        cpassw=request.POST.get("confirmpassword")
        if request.method=="POST":
            if passw==passw:
                try:
                    user=User.objects.get(username=email)
                    return render(request,"singup.html",{'error':"User already exists"})  
                except User.DoesNotExist:
                    user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                    return render(request,"singup.html",{'success':"user created successfully"})    
        else:
            return render(request,"singup.html") 
    else:
        return redirect(index) 
def client_details(request):
    if request.user.is_superuser:
        return render(request,"client_details.html")
    return redirect(index)
def admin_page(request):
    if request.user.is_superuser:
        user=User.objects.all()
        sendvar={
          "user":user  
        }
        return render(request,"admin_page.html",sendvar)
    return redirect(index)
def delete(request,id):
    if request.method=="POST":
        pk=User.objects.get(pk=id)
        pk.delete()
        return redirect(admin_page)
def logout(request):
    auth.logout(request)
    return redirect(index)





#CAM Code.........
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')


'''def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')'''
					
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')