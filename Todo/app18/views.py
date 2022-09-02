from django.shortcuts import render,redirect
from app18.models import Todo
from app18.forms import Task

# Create your views here.
def index(request):
    Data=Todo.objects.all()
    return render(request,'index.html', {'Data': Data})
    

def update(request):
    return render(request,'update.html')

def conform(request):
    return render(request,'conform.html')

def info(request):
    form=Task()
    if request.method=="POST":
        form=Task(request.POST)
        Taskname=request.POST['task_name']
        Priority=request.POST['priority']
        Date=request.POST['date']
        add=Todo(Taskname=Taskname,Priority=Priority,Date=Date)
        add.save()
        Data=Contact.objects.all()
    
        return render(request, 'index.html',{'Data': Data})
        
    else:
        return render(request, 'index.html')

# def form(request):
#     form=Task()

#     if request.method=='POST':
#         form=Task(request.POST)
#         if form.is_valid():
#             print("form validation success.print in console")  
#             print("Taskname"+form.cleaned_data['Taskname']) 
#             print("Priority"+form.cleaned_data['Priority']) 
#             print("Date"+form.cleaned_data['Date'])
            
#     return render(request,'form.html',{'form':form})

def formupdate(request,id):
     
    if request.method=="POST":
        
        add=Todo.objects.get(id=id)
        
        add.Taskname=request.POST['task_name']
        add.Priority=request.POST['priority']
        add.Date=request.POST['date']
        add.save()
        return redirect("index")
    else:
        Data=Todo.objects.all()
        return render(request, 'update.html',{'Data':Data})

def edit(request,id):
    Data=Todo.objects.get(id=id)
    return render(request,'update.html',{'Data':Data})


def delete(request,id):
    if request.method=="POST":
        add=Todo.objects.get(id=id)
        add.delete()
        return redirect('index')
    else:
        Data=Todo.objects.all()
        return render(request, 'conform.html',{'Data':Data})




 

