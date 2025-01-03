from flask import Flask, request, jsonify, render_template, url_for, redirect, flash, session
from controller.login_service import *
from controller.search_room_service import *
from controller.time_service import *
from controller.waiting_service import *
from controller.book_service import *
from controller.reservation_service import *
from model.user import *
from model.account import *
from model.waitingList import *
from model.room import *
from model.time import *
from model.waiting_list import *
from model.reservation import *
from model.deny_list import *
from model.reservationDetail import *
from model.reservationRejectDetail import *
import datetime

app = Flask(__name__, template_folder='template')
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return redirect(url_for('intro'))

@app.route('/intro', methods=['GET', 'POST'])
def intro():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'log in':
            return redirect(url_for('login'))
        elif choice == 'admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('sign_up'))
    return render_template('intro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        choice = request.form.get('choice')
        username = request.form.get('username')
        password = request.form.get('password')
        account = Account(username, password)
        if choice == 'log in':
            login_service = LoginService()
            if login_service.validate_login(account):
                session['username'] = account.get_name()
                user_info = login_service.show_user_detail(account)
                session['user_id'] = user_info[0]
                # print('Info ', user_info)
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error_text='Invalid username or password')
        else:
            return redirect(url_for('sign_up'))
    return render_template('login.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        mail = request.form.get('mail')
        password = request.form.get('password')
        phone = request.form.get('phone')
        user = User(username, mail, password, phone)
        login_service = LoginService()
        choice = request.form.get('choice')
        if choice == 'sign up':
            if login_service.validate_sign_up(user):
                return redirect(url_for('successful_sign_up'))
            else:
                return render_template('signup.html', error_text='Email or Phone Number already exists')
        else:
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/successful_sign_up', methods=['GET', 'POST'])
def successful_sign_up():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('successful_signup.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    username = session.get('username')
    search_room_service = SearchRoomService()
    rooms = search_room_service.search_all_rooms()
    user_id = session.get('user_id')
   
    room_list = []
    for i in rooms:
        room_list.append(Room(i[0], i[1], i[2]))
    click = request.form.get('click')
    if request.method == 'GET':
        return render_template('home.html', welcome=username, rooms=room_list)
    if request.method == 'POST':
        if click == 'search room':
            room_id = request.form.get('room')
            session['room_id'] = room_id
            session['user_id'] = user_id
            return redirect(url_for('room_info'))
        elif click == 'login page':
            return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/room_info', methods=['GET', 'POST'])
def room_info():
    click = request.form.get('click')
    date = request.form.get('date')
    room_id = session.get('room_id')
    search_room_service = SearchRoomService()
    room_detail = search_room_service.search_room_detail(room_id)
   
    name = room_detail[1]
    capacity = room_detail[0]
    room = Room(room_id, capacity, name)
    user_id = session.get('user_id')
    if request.method == 'GET':
        return render_template('room_info.html', day=date, name=room.get_name(), capacity=room.get_capacity())
    if request.method == 'POST':
        if click.startswith("book-"):
            available_times = search_room_service.show_available_times(room_id, date)
            _, start_time, end_time = click.split('-')
            time_service = TimeService()
            response = time_service.show_time_detail(date, start_time, end_time)
            session['time_id'] = response[0]
            
            
            time = Time(response[0], start_time, end_time, date)
            # Add new waiting list
            room_id = session.get('room_id')
            time_id = session.get('time_id')
            booking = WaitingList(user_id, room.get_id(), time_id, 'waiting')
            waiting_service = WaitingService()
            waiting_service.delete_waiting_list_reject('reject')
            if waiting_service.check_exist_waiting_list(booking):
                waiting_service.add_to_waiting_list(booking)
                return render_template('room_info.html', day=time.get_day(), name=room.get_name(), capacity=room.get_capacity(), available_times=available_times, response='Booked successful!')
            
            return render_template('room_info.html', day=time.get_day(), name=room.get_name(), capacity=room.get_capacity(), available_times=available_times, response='Already booked!')
        elif click == 'return':
            session['user_id'] = user_id
            return redirect(url_for('home'))
        elif click == 'date':
            available_times = search_room_service.show_available_times(room_id, date)
            session['user_id'] = user_id
            return render_template('room_info.html', day=date, name=room.get_name(), capacity=room.get_capacity(), available_times=available_times)
        elif click == 'waiting list':
            session['user_id'] = user_id
            return redirect(url_for('successful_book'))
    return render_template('room_info.html')

@app.route('/successful_book', methods=['GET', 'POST'])
def successful_book():
    user_id = session.get('user_id')
    waiting_service = WaitingService()
    waiting_list = waiting_service.show_all_waiting_list(user_id)
  
    click = request.form.get('click')
    reservation_service = ReservationService()
    booking_accept = reservation_service.get_user_reservations(user_id)
    booking_deny = waiting_service.show_booking_deny_list(user_id)

    list_waiting = []
    for i in waiting_list:
        list_waiting.append(ListWaiting(i[0], i[1], i[2], i[3], i[4], i[5]))
    list_book = []
    for i in booking_accept:
        list_book.append(Reservation(i[0], i[1], i[2], i[3], i[4], i[5]))
    list_deny = []
    for i in booking_deny:
        list_deny.append(ListDeny(i[0], i[1], i[2], i[3], i[4], i[5]))
    
    if request.method == 'GET':
        return render_template('successful_book.html', messages='Waiting list to be accepted', waiting_list=list_waiting,
                               booking_accept=list_book,booking_deny=list_deny)
    if request.method == 'POST':
        if click.startswith("cancel-"):
            session['user_id'] = user_id
            _, waiting_id = click.split('-')
            waiting_service.delete_from_waiting_list(waiting_id)
            return redirect(url_for('successful_book'))
        elif click.startswith("delete-"):
            session['user_id'] = user_id
            _, reservation_id = click.split('-')
            reservation_service.deleteReservation(reservation_id)
            return redirect(url_for('successful_book'))
        elif click == 'back':
            session['user_id'] = user_id
            print('ID user ', user_id)
            return redirect(url_for('room_info'))
    return render_template('successful_book.html')

@app.route('/manageReservation', methods=['GET', 'POST'])
def manageReservation():
    click = request.form.get('click')
    waiting_service = WaitingService()
    waiting_list = waiting_service.show_all_waiting_list_total()
    reservation_service = ReservationService()
    reservations = reservation_service.get_all_reservations()
    rejectReservation = waiting_service.get_all_deny_list()
    reservation_wait = []
    reservation_accept = []
    reservation_reject = []
    for i in waiting_list:
        reservation_wait.append(ReservationDetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        
    for i in reservations:
        reservation_accept.append(ReservationDetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        
    for i in rejectReservation:
        reservation_reject.append(ReservationRejectDetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    
    if request.method == 'GET':
        return render_template('manageReservation.html', list=reservation_wait, bookings=reservation_accept, rejectReservation=reservation_reject)
    if request.method == 'POST':
        if click.startswith("accept-"):
            _, waiting_id, user_id, room_id, time_id = click.split('-')
            booking = WaitingList(user_id, room_id, time_id, 'waiting')
            book_service = BookService()
            book_service.add_new_reservation(booking)  
            waiting_service.delete_from_waiting_list(waiting_id) 
            
            waiting_service.update_reject_status(room_id, time_id, 'reject')
            # waiting_service.delete_same_from_waiting_list(room_id, time_id)
            
            return redirect(url_for('manageReservation'))
        elif click.startswith("reject-"):
            # delete from waiting list
            _, waiting_id = click.split('-')
            waiting_service.reject_waiting_list(waiting_id)
            return redirect(url_for('manageReservation'))
        elif click.startswith("delete-"):
            _, reservation_id = click.split('-')
            reservation_service.deleteReservation(reservation_id)
            return redirect(url_for('manageReservation'))
        elif click == 'deleteLateBookings':
            reservation_service.deleteLateReservations()
            return redirect(url_for('manageReservation'))
        elif click.startswith("deny-"):
            _, deny_id = click.split('-')
            waiting_service.delete_from_waiting_list(deny_id)
            return redirect(url_for('manageReservation'))
        elif click == 'adminPage':
            return redirect(url_for('admin'))
    return render_template('manageReservation.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'manageRoom':
            return redirect(url_for('manageRoom'))
        elif choice == 'manageTime':
            return redirect(url_for('manageTime'))
        else:
            return redirect(url_for('manageReservation'))
    return render_template('admin.html')

@app.route('/manageRoom', methods=['GET', 'POST'])
def manageRoom():
    search_room_service = SearchRoomService()
    rooms = search_room_service.search_all_rooms()

    if request.method == 'GET':
        return render_template('manageRoom.html', rooms=rooms)
    if request.method == 'POST':
        room_id = request.form.get('delete')
        search_room_service.delete_room(room_id)
        create = request.form.get('create')
        adminPage = request.form.get('adminPage')
        if create == 'onclick':
            capacity = request.form.get('capacity')
            roomName = request.form.get('roomName')
            room = Room(room_id, capacity, roomName)
            checkRoom = search_room_service.search_room_by_name(roomName)
            if len(checkRoom) > 0:
                return render_template('manageRoom.html', rooms=rooms, error_text='This room has been created')
            search_room_service.create_room(room)
            return redirect(url_for('manageRoom'))
        if adminPage == 'onclick':
            return redirect(url_for('admin'))
        return redirect(url_for('manageRoom'))
    return render_template('manageRoom.html')


@app.route('/manageTime', methods=['GET', 'POST'])
def manageTime():
    time_service = TimeService()
    times = time_service.show_all_times()
    if request.method == 'GET':
        return render_template('manageTime.html', times=times)
    if request.method == 'POST':
        time_id = request.form.get('delete')
        time_service.delete_time(time_id)
        create = request.form.get('create')
        adminPage = request.form.get('adminPage')
        if create == 'onclick':
            timeRoom = request.form.get('timeRoom')
            if timeRoom == 'slot1':
                start = '08:00:00'
                end = '09:59:00'
            elif timeRoom == 'slot2':
                start = '10:00:00'
                end = '11:59:00'
            elif timeRoom == 'slot3':
                start = '13:00:00'
                end = '14:59:00'
            elif timeRoom == 'slot4':
                start = '15:00:00'
                end = '16:59:00'
            day = request.form.get('day')
            time = Time(time_id, start, end, day)
            check_time = time_service.show_time_detail(time.get_day(), time.get_start_time(), time.get_end_time())
            if check_time:
                return render_template('manageTime.html', times=times, error_text='This time has been created')
            else:
                time_service.add_time(time)
                return redirect(url_for('manageTime'))
        if adminPage == 'onclick':
            return redirect(url_for('admin'))
        return redirect(url_for('manageTime'))
    return render_template('manageTime.html')

if __name__ == '__main__':
    app.run(debug=True)
 

