from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient

# Create your views here.
def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospi/list_doctors.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialty']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        try:
            doctor = Doctor.objects.create(name=name, specialization=specialization, contact_number=contact_number, email=email)
            return redirect('list_doctors')
        except IntegrityError:
            return render(request, 'hospi/add_doctor.html', {
                'error': 'Doctor with this email already exists',
                'name': name,
                'email': email,
                'specialization': specialization,
            })
    return render(request, 'hospi/add_doctor.html')

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    patients = doctor.patients.all()
    return render(request, 'hospi/doctor_detail.html', {'doctor': doctor, 'patients': patients})

def add_patient(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        contact_number = request.POST['contact_number']
        Patient.objects.create(name=name, age=age, contact_number=contact_number, doctor=doctor)
        return redirect('doctor_detail', doctor_id=doctor_id)
    return render(request, 'hospi/add_patient.html', {'doctor': doctor})