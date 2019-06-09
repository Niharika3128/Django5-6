from django.shortcuts import render


def show(request):
    no1 = 1
    no2 = 2
    no3 = 3
    no4 = 5145
    no6 = 9052492329

    return render(request,"index.html",
                  {"data1":"Hello",
                   "data2":no1,
                   "data3":no2,
                   "data4":no3,
                   "data5":no4,
                   "data6":no6,
                   }
                  )