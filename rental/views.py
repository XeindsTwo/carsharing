from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from rental.forms import BookingForm


@login_required
def booking_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # делаем commit для того, чтобы мы могли указать своего пользователя и авто
            # иначе если не указать - есть риск, что данные не привяжутся
            booking = form.save(commit=False)

            # привязка текущего пользователя и авто
            booking.user = request.user
            booking.car = car
            booking.save()

            return redirect('profile')  # отправляем на страницу профиля после успеха

    else:
        form = BookingForm()

    return render(
        request,
        'rental/create_booking.html',
        {'form': form, 'car': car}
    )
