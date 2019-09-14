from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from movieapp.models import *
from django.db.models import Q
from django.template import RequestContext, Context, Template
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
import json


# Create your views here.
def index(request):
    return render_to_response('home.html',context_instance=RequestContext(request))


@login_required
def homeapi(request):
    return render_to_response('welcome.html',context_instance=RequestContext(request))


def usrlog(request):
    #for user login
        
    response = {'status': "error"}
    user = str(request.POST.get('username'))
    pswd = str(request.POST.get('password'))
    uname = User.objects.filter(username = user)
    if uname.count()>0:
        user_valid = authenticate(username = user, password = pswd)
        if user_valid is not None:
            login(request,user_valid)
            response['message'] = 'welcome'
            response['status'] = 'success'
            return render_to_response('welcome.html',context_instance=RequestContext(request))  
        else:
            response['message'] = 'username or password incorrect'
            response['status'] = 'error'
            return render_to_response('home.html',{'data': response},context_instance=RequestContext(request))

    else:
        response['message'] = 'please register'
        response['status'] = 'error'
        return render_to_response('home.html',{'data': response},context_instance=RequestContext(request))


def registration(request):
    #for user register
    
    if request.method == 'GET':
        return render_to_response('register.html',context_instance=RequestContext(request))
    response = {'status': "error"}
    user = request.POST.get('username')
    pswd = request.POST.get('password')
    email = request.POST.get('email')
    print(email)
    uname = User.objects.filter(username = user)
    if uname.count()>0:
        response['message'] = 'user already exist'
        return  render_to_response('register.html', {'data': response},context_instance=RequestContext(request))
    
    else:
        user_reg = User.objects.create_user(username = user )
        user_reg.set_password(pswd)
        user_reg.save()
        response['status'] = 'success'
        return  render_to_response('register.html', {'data': response},context_instance=RequestContext(request))


@login_required
def userlogout(request):
    #for logout user
    
    response = {'status': "error"}
    logout(request)
    response['status'] = 'YOUR ARE LOGGED OUT'
    return render_to_response('home.html', {'log': response}, context_instance=RequestContext(request))


@login_required
def userdetails(request):
    #for user profile
    
    if request.method == 'GET':
        return render_to_response('edit.html',context_instance=RequestContext(request))

    response = {'status': "error"}

    name = request.POST.get('name')
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    address = request.POST.get('address')
    mobile_num = request.POST.get('mobile')
    email = request.POST.get('email')
    user_update = UserDetail.objects.create( name = name, first_name = first_name, last_name = last_name, mail= email,
                                        address = address, mobile = mobile_num)
    user_update.save()
    response['status'] = "succes"

    return render_to_response('edit.html', {'res': response}, context_instance=RequestContext(request))

@login_required
def allmovie(request):
    movie_data = MovieDetail.objects.all()
    return render_to_response('movie.html', {'data': movie_data}, context_instance=RequestContext(request))


@login_required
def movies(request):
    #geting movie
    obj = Movie.objects.all()
    return render_to_response('welcome.html', {'data': obj}, context_instance=RequestContext(request))


@login_required
def searchmovie(request):
    #searching movies
    response = {'status': "error"}
    #uname = request.user for geting username
    if request.method == 'GET':
        return render_to_response('welcome.html',context_instance=RequestContext(request))
    movie = request.POST.get('movie')
    if movie in [None,'']:
        movie = None
    if not movie:
        response['status'] = 'please enter name'
        return render_to_response('welcome.html', {'respo': response}, context_instance=RequestContext(request))
    data = Movie.objects.filter(movie_name__contains=movie)
    if data.count()>0:
        return render_to_response('welcome.html', {'data': data}, context_instance=RequestContext(request))
    else:
        response['status'] = 'NOT IN OUR LIST'
        return render_to_response('welcome.html', {'respo': response}, context_instance=RequestContext(request))


@login_required
def movie_details(request):
    #getting movie details
    resp = {'status': "error"}
    m_id = request.GET.get('id')
    obj = request.POST.get('search')
    movie_data = MovieDetail.objects.filter(Q(movie_id = m_id) | Q(movie__movie_name = obj) | Q(hero = obj) | Q(heroine = obj))
    songs = Songs.objects.filter(id = m_id)
    resp['movie'] = m_id
    return render_to_response('moviedata.html', {'data': movie_data, 'songs': songs, 'dat': resp}, context_instance=RequestContext(request))

@login_required
def book(request):
    movie_id = request.GET.get('id')
    print(movie_id)
    details = Booking_info.objects.all()
    return render_to_response('book.html', {'data': details}, context_instance=RequestContext(request))


@login_required
def booking(request):
    movie_id = request.GET.get('id')
    print(movie_id)
    #details = Booking_info.objects.all()
    details = Booking_info.objects.filter(movie_id=movie_id)
    return render_to_response('book.html', {'data': details}, context_instance=RequestContext(request))


@login_required
def seats(request):
    res = {'status': "error"}
    cs={}
    show = request.GET.get('id')
    print(show)
    #import pdb;pdb.set_trace()
    seats = Booking_info.objects.get(id = show)
    if  request.method == 'POST':    
        seat_req = request.POST.get('no')
        print(seat_req)
        if seats.seat_available >= int(seat_req):
            obj = User_sel.objects.create(seats = seat_req, booking = seats, user = request.user)
            obj.save()
            seats.seat_available = seats.seat_available - int(seat_req)
            seats.save()

            l=seats.total_seats
            l1 = l.split(',')
            #print()l1
            
            for n in l1:
                ts = {'A':l1[0:10],'B':l1[10 : 20],'C':l1[20:30],'D':l1[30:40],'E':l1[40:50],'F':l1[50:60],'G':l1[60:70],'H':l1[70:80],'I':l1[80:90],'J':l1[90:100] }
                cs['t'] = ts
            #import pdb;pdb.set_trace()
            res['seats_list'] = seats.seat_num
            res['seats_list'] = res['seats_list'].split(',')
            res['status'] = 'success' 
            res['bookingid'] = show
            res['seat'] = seat_req
            return render_to_response('select.html', {'data': res , 's' : cs, 'req': seat_req},context_instance=RequestContext(request)) 
        else:
            res['status'] = 'error'
            return HttpResponse(json.dumps(res), content_type ='application/json')
        
    res['status'] = 'ok'
    res['msg'] = 'select no of seat'
    res['bookingid'] = show
    return render_to_response('seat.html', {'data': res, 'seat' : seats},context_instance=RequestContext(request)) 


@login_required
def selection(request):
    res = {'status': "error"}
    request.method == 'POST'
    sel = request.GET.get('id')
    print(sel)
    #lh  = len(sel)
    seats = Booking_info.objects.get(id = sel)
    booking = Seats.objects.get(show=seats)
    #st = User_sel.objects.all
    #print()st
    select = request.POST.getlist("seat")
    print(select)
    a = ",".join(select)
    print(a)
    obj = User_sel.objects.create(selected_seats = a, booking = seats, user = request.user)
    obj.save()
    #import pdb;pdb.set_trace()
    s= seats.seat_num
    spt = s.split(",")
    l= [seat for seat in spt if seat not in select]
    avail_seats = ",".join(l)
    #print()avail_seats
    
    seats.seat_num = avail_seats
    seats.save()

    
    """status = booking.seat_status
    if status == True:
        res['status'] = 'available'
    else:
        res['status'] = 'not available'""



    if a not in avail_seats:
        select = a.replace(',',' ')
        sel = list(map(str, a))
        info = Seats.objects.create(show = seats, seats= select, seat_status= 'S')
        info.save()
    else:
        res['msg'] = 'seat not selected' """

    res['status'] = 'success'
    res['msg'] = 'your seat is  booked'
    return HttpResponse(json.dumps(res), content_type ='application/json')

    #return render_to_response('sel.html', {'sel': s },context_instance=RequestContext(request))


@login_required
def trans(request):
    user = request.user
    obj = Transaction.objects.values('user__username').annotate(Sum('amount'))
    print(obj)
    return render_to_response('trans.html', {'data': obj },context_instance=RequestContext(request))


@login_required
def book_seat(request):
    res = {'status': "error"}
    cs={}
    show = request.GET.get('id')
    print(show)
    #import pdb;pdb.set_trace()
    booking = Seats.objects.filter(show_id=show)
    print(booking)
    if booking.count()> 0:
        seat_list = []
        status = []
        if  request.method == 'POST': 
            seat_req = request.POST.get('no')
            for obj in booking:
                seat_list.append(obj.seat)
                if obj.seat_status==True:
                    status.append(obj.seat)
                #seat_list.append({'seat':obj.seat, 'status': obj.seat_status})

            for n in seat_list:
                ts = {'A':seat_list[0:5],'B':seat_list[5 : 10] }
            cs['r'] = ts
            print(ts)
            print(len(status))
            if len(status)>=int(seat_req):
                res['t'] = status
                #cs['t'] = booking
                res['bookingid'] = show
                res['seat'] = seat_list
                return render_to_response('sel.html', {'data': res, 's' : cs, 'req': seat_req},context_instance=RequestContext(request))
            else:
                res['status'] = 'sorry no of seats not available'
                return HttpResponse(json.dumps(res), content_type ='application/json')

       
    else:
        res['status'] = 'Error'
        res['msg'] = 'sorry we are screening no shows now'
        return HttpResponse(json.dumps(res), content_type ='application/json')

    res['status'] = 'ok'
    res['msg'] = 'select no of seat'
    res['bookingid'] = show
    return render_to_response('seatbook.html', {'data': res},context_instance=RequestContext(request))


@login_required
def selected(request):
    user = request.user
    res = {'status': "error"}
    sel = request.GET.get('id')
    print(sel)
    if request.method == 'POST':
        user = request.user
        select = request.POST.getlist("seat")
        user_selected = ",".join(select)
        seat = Seats.objects.filter(show_id=sel,seat__in=select)
        cost=[]
        for t in seat:
            cost.append(t.cost_of_ticket)
        booked_amount=sum(cost)
        obj = Transaction.objects.filter(user = user)
        user_amount=[]
        for n in obj:
            user_amount.append(n.amount)
        if sum(user_amount)>= sum(cost):
            trans= obj.create(amount = -booked_amount, user= user)
            booked= BookingTransactions.objects.create(seat_id=sel, seat_selected=user_selected, user=user,amount=booked_amount)
            booked.save()
            seat.update(seat_status=False, user = request.user)
            res['status'] = 'success'
            res['msg'] = user_selected,'Seat_Number Is Booked For you'
            return HttpResponse(json.dumps(res), content_type ='application/json')
        else:
            res['status'] = 'error'
            res['msg'] = "Sorry No Amount In Your Account"
            return HttpResponse(json.dumps(res), content_type ='application/json')
    else:
        res['status'] = 'error'
        return HttpResponse(json.dumps(res), content_type ='application/json')


@login_required
def details(request):
    res = {'status': "error"}
    user = request.user
    detail = UserDetail.objects.filter(user=user)
    trans = Transaction.objects.filter(user = user).aggregate(Sum('amount'))
    res['status'] = "success"
    return render_to_response('myprofile.html', {'data': trans, 'info':detail },context_instance=RequestContext(request))






#def booking_details(request):
#    obj = Booking_info.objects.all()

    
    # used group by
    #Annotate calculates summary values for each item in the query set
    # aggregate calculates values for the entire query set
    # obj = Transaction.objects.aggregate(Sum('amount')).values()
    # obj = Transaction.objects.filter(user = user).aggregate(Sum('amount'))
    
"""def trans(request):
    res = {'status': "error"}
    user = request.user
    rst = request.GET.get('id')
    print()rst
    bj =Transaction.objects.all()
    #print()bj
    #for i in bj:
        #print()i.amount
    #obj = Transaction.objects.filter(user = user).aggregate(Sum('amount'))
    #obj = Transaction.objects.aggregate(Sum('amount')).values()[0]
    #Player.objects.annotate(total_amount=Sum('amount'))
    #obj = Transaction.objects.annotate(total_amount=Sum('amount'))
    #print()obj
    #obj = Transaction.objects.filter(id=rst)
    obj = Transaction.objects.filter(user=rst).aggregate(Sum('amount'))
    print()obj
    res['status'] = 'success'
    #return HttpResponse(json.dumps(res), content_type ='application/json')
    return render_to_response('trans.html', {'data': obj, 's': bj},context_instance=RequestContext(request))"""