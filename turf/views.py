from django.shortcuts import render, HttpResponse,redirect
from .models import turf_add,turf,turf_facility,Pricing_chart,Booking_slot3,M_Host
# from accounts.models import Booking_slot
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from datetime import datetime


# Create your views here.

# def location(request):
#     s='<p><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11042.434577300048!2d75.39473829730063!3d11.89880837626124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba43d2df822155d%3A0xefcf23cac7bbe11f!2sTiki%20Taka%20Football%2FCricket%20Turf%20Kannur%20(%20Net%20Practice%20%2CBowling%20Machine)!5e0!3m2!1sen!2sin!4v1618498319189!5m2!1sen!2sin" width="200" height="200" style="border:0;" allowfullscreen="" loading="lazy"></iframe></p>'
#     return render(request,'temp.html', {'s':s})


def new_turf(request):
    if request.method == 'POST':
        oname = request.POST['oname']
        tname = request.POST['tname']
        addr = request.POST['addr']
        sports = request.POST['sports']
        mob_no = request.POST['mob_no']

        t = turf_add(owner_name=oname, turf_nm=tname, address=addr, sports=sports, contact_no=mob_no)
        t.save()

        return HttpResponse('Awaiting confirmation ')

    return render(request, 'temp.html')


def turf_view(request):
    if request.method=='POST':
        place=request.POST['place']
        if place=='kannur':
            list=turf.objects.filter(place='Kannur')
            return render(request,'turf_view.html',{'list':list})
        elif place=='Kozhikode':
            list=turf.objects.filter(place='Kozhikode')
            return render(request,'turf_view.html',{'list':list})
        else:
            return redirect(turf_view)


    list=turf.objects.all()
    return render(request,'turf_view.html',{'list':list})

def turf_booking(request,id):
    s=turf.objects.filter(turf_name=id)
    for i in s:
        t_id=i.id
        break
    f=turf_facility.objects.filter(turf_id=t_id)
    c=Pricing_chart.objects.filter(turf_id=t_id)


    d1={'s':s,'f':f,'c':c}

    return render(request,'booking.html',d1)

def turf_booking2(request):
    if request.method =='POST':
        t_name = request.POST['t_name']
        s_time=request.POST['start_time']
        e_time = request.POST['end_time']
        d = request.POST['b_date']
        s_type=request.POST['example']
        s = turf.objects.filter(turf_name=t_name)
        for i in s:
            id=i.id
            break

        if Booking_slot3.objects.filter(t_name=t_name).filter(s_type=s_type).filter(date=d).filter(s_time=s_time).filter(e_time=e_time).exists():
            # if Booking_slot3.objects.filter(s_type=s_type).exists():
            #     if Booking_slot3.objects.filter(date=d).exists():
            #       if Booking_slot3.objects.filter(s_time=s_time).exists():
            #           if Booking_slot3.objects.filter(e_time=e_time).exists():
                          return HttpResponse('Timing slot Already booked <a href=''http://127.0.0.1:8000/turf/turf_view''>click here</a>')



        else:


            p_calc=Pricing_chart.objects.filter(turf_id=id)
            d3=d
            t1=[k.timing for k in p_calc]
            # print(t1)
            # print(s_time)
            # print(s_type)
            for l in p_calc:
               if  s_type in l.s_type:
                    for i in t1:
                        if s_time[0:2]>=i[0:2] and s_time[0:2]<i[6:8]:
                            t=i

                            break
                    break



            # print(datetime.today())
            t1 = str(d)
            year = int(t1[0:4])
            month = int(t1[5:7])
            day = int(t1[8:10])

            t2=datetime(year,month,day,0,0,0)
            d1=t2.weekday()

            if  d1<5:
                a='Weekday'
                b='Weekday,Weekend,Holiday'
            elif d1>5:
                a='Weekend'
                b='Weekday,Weekend,Holiday'
            else:
                a='Holiday'
                b='Weekday,Weekend,Holiday'
            # print(t2.weekday())

            p_calc2 = Pricing_chart.objects.filter(timing=t).filter(day=a)
            p_calc3 = Pricing_chart.objects.filter(timing=t).filter(day=b)
            for k in p_calc3:
                price1=k.price

            for i in p_calc2:
                        # print(i.timing,i.price)
                    price1=i.price

            t3=datetime(year,month,day,int(s_time[0:2]),int(s_time[4:]),0)
            t4=datetime(year,month,day,int(e_time[0:2]),int(e_time[4:]),0)
            d=str(t4-t3)
            price1=int(price1[1:5])
            # print('total =',price1*int(d[0]))
            total = price1*int(d[0])
            if request.user.is_authenticated:
                B=Booking_slot3(user=request.user,t_name=t_name,date=d3,s_time=s_time,e_time=e_time,s_type=s_type,total=total)
                B.save()
                return render(request, 'booking2.html',{'total': total, 's_time': s_time, 'e_time': e_time, 't_name': t_name, 'date'
                              : d3})

    else:
        return redirect('http://127.0.0.1:8000/accounts/login')




        # return render(request,'booking2.html',{'total':total,'s_time':s_time,'e_time':e_time,'t_name':t_name,'date'
        #                                        :d3})
        # return HttpResponse('Done')

def turf_booking3(request):
    return HttpResponse('<p>TRANSACTION SUCCESSFULL</p> <a href=''http://127.0.0.1:8000''>click here</a>')



def bookings(request):

    b=Booking_slot3.objects.filter(user=request.user.id)

    return render(request,'bookings.html',{'b':b})

def Match_host(request):
    if request.method== 'POST' :

        h_match=request.POST ['h_match']



        return render(request,'Match_host.html',{'h':h_match})





    else:
     return redirect(Join_match)

def Match_host2(request):
    if request.method=='POST':
        team_name=request.POST['te_name']
        no_pl=request.POST['no_pl']
        place=request.POST['place']
        date=request.POST['b_date']
        s_time=request.POST['start_time']
        e_time=request.POST['end_time']
        m_number=request.POST['m_number']
        s_type=request.POST['s_type']
        id='m2'

        y=turf.objects.filter(place=place)




        return render(request,'Match_host.html',{'id':id,'y':y,'team_name':team_name,'no_pl':no_pl,'date':date,'s_time':s_time,'e_time':e_time,'m_number':m_number,'s_type':s_type})


def Match_host3(request):
    if request.method == 'POST':
        t_name=request.POST['t_name']
        d= request.POST['date']
        s_time = request.POST['s_time']
        e_time = request.POST['e_time']
        s_type =request.POST['s_type']
        no_pl=request.POST['no_pl']
        t1_name=request.POST['team_name']
        id2='m3'
        s = turf.objects.filter(turf_name=t_name,)
        for i in s:
            id = i.id
            break

        if Booking_slot3.objects.filter(t_name=t_name).filter(s_type=s_type).filter(date=d).filter(
                s_time=s_time).filter(e_time=e_time).exists():

            return HttpResponse(
                'Timing slot Already booked <a href=''http://127.0.0.1:8000/turf/Match_host''>click here</a>')



        else:

            h1 = M_Host(t1_name=t1_name,date=d,s_time=s_time,e_time=e_time,s_type=s_type,turf_name=t_name,no_pl=no_pl)
            h1.save()


            p_calc = Pricing_chart.objects.filter(turf_id=id)
            d3 = d
            t1 = [k.timing for k in p_calc]
            for l in p_calc:
                if s_type in l.s_type:
                    for i in t1:
                        if s_time[0:2] >= i[0:2] and s_time[0:2] < i[6:8]:
                            t = i

                            break
                    break

            # print(datetime.today())
            t1 = str(d)
            year = int(t1[0:4])
            month = int(t1[5:7])
            day = int(t1[8:10])

            t2 = datetime(year, month, day, 0, 0, 0)
            d1 = t2.weekday()

            if d1 < 5:
                a = 'Weekday'
                b = 'Weekday,Weekend,Holiday'
            elif d1 > 5:
                a = 'Weekend'
                b = 'Weekday,Weekend,Holiday'
            else:
                a = 'Holiday'
                b = 'Weekday,Weekend,Holiday'
            # print(t2.weekday())

            p_calc2 = Pricing_chart.objects.filter(timing=t).filter(day=a)
            p_calc3 = Pricing_chart.objects.filter(timing=t).filter(day=b)
            for k in p_calc3:
                price1 = k.price

            for i in p_calc2:
                price1 = i.price

            t3 = datetime(year, month, day, int(s_time[0:2]), int(s_time[4:]), 0)
            t4 = datetime(year, month, day, int(e_time[0:2]), int(e_time[4:]), 0)
            d = str(t4 - t3)
            price1 = int(price1[1:5])
            total = price1 * int(d[0])

            return render(request,'Match_host.html',{'id2':id2,'total':total})



def Join_match(request):
    M=M_Host.objects.all()
    return render(request,'Match_host.html',{'M':M})

