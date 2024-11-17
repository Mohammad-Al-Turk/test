from django.shortcuts import render,redirect
import random                    

def Gen_num(request):
    
    if 'randomNum' not in request.session:
        request.session['randomNum']=random.randint(1, 100)
        context={
            'randomNum' : request.session['randomNum'],
        }
        return render(request,'index.html',context)
    else:
        context={
            'randomNum' : request.session['randomNum']
        }
        return render(request,'index.html',context)
    
    
    
def guess(request):
    rodNum=int(request.session['randomNum'])
    myNum=int(request.POST['number'])
    if myNum > rodNum:
        context={
            'result': 'too high',
            'go':0
        }
    elif myNum < rodNum:
        context={
            'result': 'too low',
            'go':0
        }

    else:
        context={
            'result':'good job',
            'go':1
            }
    request.session['rt']=context['result']
    request.session['go']=context['go']
    return redirect('/')
        
def playAgain(request):
    request.session['rt']=''
    request.session['go']=0
    request.session['randomNum']=random.randint(1, 100)
    return redirect('/')

    