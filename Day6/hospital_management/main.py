from models import Doctor, Patient, Hospital

hospital = Hospital("Apollo")

doctor1 = Doctor(
    "Dr. Sharma",
    45,
    "9876543210",
    "Cardiology",
    1000
)

doctor2 = Doctor(
    "Dr. Priya",
    38,
    "9876501234",
    "Dermatology",
    800
)

patient1 = Patient(
    "Arun",
    28,
    "9999999999"
)
patient2 = Patient(
    "patient2",
    28,
    "9999999999"
)

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

hospital.add_patient(patient1)

hospital.book_appointment(patient1,"Cardiology")
hospital.book_appointment(patient1,"Dermatology")
hospital.book_appointment(patient1,"Dermatology")
hospital.book_appointment(patient2,"Dermatology")


print(hospital.daily_summary())

print()

print(hospital.billing_summary(patient1))