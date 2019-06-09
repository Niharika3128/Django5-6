from django.shortcuts import render

def showIndex(request):
    a = 1
    text1 = "This is Sathya's"
    text2 = "hello"
    marks = [45,55,65,75,85,95]
    date = "03 may 2019"
    return render(request,"index.html",
                  {"data1":a,
                   "data2":text1,
                   "data3":text2,
                   "data4":marks,
                   "data5":date})