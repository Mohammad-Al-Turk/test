from django.shortcuts import render, HttpResponse

def page(request):
    return render(request,"index.html")

def show(request):
    context={
        'name':request.POST['name'], 
        'location':request.POST['location'],
        'language':request.POST['language'],
        'Comments':request.POST['Comments']
    }
    return render(request,"show.html",context)
#لانه استخدما  ميثود بوست ما لازن انردر دايرت الزم نعمل ريداريكت  على باث ثاني ثم بنرندر مع استخدام السيشن