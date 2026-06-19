from models.patient import Patient
from models.doctor import Doctor

class Hospital:
    def __init__ (self,name:str):
        self._name = name
        self._doctors = []
        self._patients = []

    def add_patient (self, patient: Patient)-> None:
        self._patients.append(patient)

    def add_doctor (self, doctor: Doctor)-> None:
        self._doctors.append(doctor)

    def find_doctor (self,specialisation:str) -> Doctor | None:
        for doctor in self._doctors:
            if doctor.specialisation.lower() == specialisation.lower():
                return doctor
            
        return None
            
    def book_appointment (self,patient:Patient, specialisation:str) -> dict:
        doctor = self.find_doctor(specialisation)

        if doctor is None:
            raise ValueError("The specified doctor is not available ")
        
        appointment = {
            "doctor":doctor.name,
            "specialisation":doctor.specialisation,
            "fee" : doctor.fee
        }
        print(appointment)
        patient.add_appointments(appointment)

        return appointment 
        
    
    def daily_summary(self)-> str:

        total_appointments = sum(
            len(patient.appointments)
            for patient in self._patients
        )

        return (
            f"Doctors: {len(self._doctors)}\n"
            f"Patients: {len(self._patients)}\n"
            f"Appointments: {total_appointments}"
        )
    
    def billing_summary(self,patient:Patient)-> str:

        # for appointment in patient.appointments:
        #     total = sum(appointment["fee"])
        total = sum(
            appointment["fee"]
            for appointment in patient.appointments
        )

        doctor_details = "\n".join(
            f"{appointment['doctor']}"
            f"({appointment['specialisation']}):"
            f"₹{appointment['fee']:.2f}"
            for appointment in patient.appointments
        )

        return (
            f"Patient Name:{patient.name}"
            f"Total :₹{total:.2f}"
            f"Appointment:{doctor_details}"
        )




        


        
    