from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersform
from django.shortcuts import render
from django.core.files.storage import default_storage
from .ml_model import predict_image

def aboutUs(request):
    return HttpResponse("MY NAME IS PRAKHAR PANDEY WELCOME TO MY JOURNEY")

def homepage(request):
    data={'title':'Home of pp',
          'clist':['python','java','c','maths'],
          'iden':[{'name':'Prakhar Pandey','Quality':'Smart and Good in sports'},
                  {'name':'Abhishek','Quality':'Sanki and Good in sports '},
                  {'name':'Harsh','Quality':' Cyco with anime and good in sports'}],
            'List':[10,20,30,40,50,60,70,80,90]
          }
    
    return render(request,"sam.html", data)

def scan(request):
    # Redirect to our new plant scan upload view
    return redirect('upload_scan')

def calc(request):
    return render(request,"calc.html")


def scan2(request):
    # Redirect to the scan history view
    return redirect('scan_history')

def guide(request):
    # Render the guide page (plant A-Z)
    return render(request, "enfinal.html")

def index(request):
     if request.method=="GET":
         output=request.GET.get('output')

     data={'title':'Home of pp',
          'clist':['python','java','c','maths'],
          'iden':[{'name':'Prakhar Pandey','Quality':'Smart and Good in sports'},
                  {'name':'Abhishek','Quality':'Sanki and Good in sports '},
                  {'name':'Harsh','Quality':' Inamorato with anime and good in sports'}],
            'List':[10,20,30,40,50,60,70,80,90]
          }
    
     return render(request,"index.html",{'output':output})
# myapp/views.py

def predict_view(request):
    if request.method == "POST" and request.FILES.get("image"):
        # Save uploaded image temporarily
        image_file = request.FILES["image"]
        file_path = default_storage.save(f"temp/{image_file.name}", image_file)

        # Make prediction
        result = predict_image(file_path)

        # Delete temp file
        default_storage.delete(file_path)

        return render(request, "result.html", {"result": result})

    return render(request, "upload.html")


def userform(request):
    answ=0
    fn=usersform()
    data={'form':fn}
    
    try:
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            answ=int(n1+n2)
            
            data={ 
                 'form':fn,
                 'output':answ,

            }
            url="/index/?output={}".format(answ)
            return HttpResponseRedirect(url)
    except:
        pass

    
    return render(request,"userform.html",data)

    


 
 

