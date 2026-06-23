step 1
Entities

Person      → Base class
Doctor      → Child class
Patient     → Child class
Hospital    → Manager class


             Person
            /      \
           /        \
      Doctor      Patient

                Hospital
                   │
         ┌─────────┴─────────┐
         │                   │
    List[Doctor]       List[Patient]


Day 6 — Assignment 4
Hospital Management System
Real-world App
Apollo / Practo / MediBuddy
Overview
Capstone OOP: Person (private name/age/contact) as base. Doctor adds __fee and specialisation. 
Patient adds __appointments. Hospital holds lists of both and provides find_doctor(), 
book_appointment(), and daily_summary(). Every attribute is accessed only through public methods 
-- the same architecture used by hospital ERP systems like SAP Healthcare.
Problem
Combine all OOP concepts: Person base, Doctor and Patient children with private data, 
Hospital manager class.
Classes Person, Doctor, Patient, Hospital
class Doctor:
Inheritance Doctor(Person), 
Patient(Person)
super().__init__(name,age,contact)
Encapsulation Private name, age, fee self.__fee @property fee
Methods book_appointment, daily_summary , hospital.find_doctor("Cardio")
Constraints
• Person attrs all private -- access via @property
• Doctor.__fee private
• Patient appointments via book_appointment() only
• Hospital never accesses private attrs directly
Bonus: Add billing_report(patient) to Hospital for a formatted invoice.
