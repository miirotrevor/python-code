class Patient:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments


class Appointment:
    def __init__(self, date, time, doctor):
        self.date = date
        self.time = time
        self.doctor = doctor


class PatientPortal:
    def __init__(self):
        self.patients = []

    def register_patient(self, patient):
        self.patients.append(patient)

    def search_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None


def create_patient(name, age, gender, contact):
    return Patient(name, age, gender, contact)


def create_appointment(date, time, doctor):
    return Appointment(date, time, doctor)


def register_patient(portal, patient):
    portal.register_patient(patient)


def search_patient(portal, name):
    return portal.search_patient(name)


# Create patient objects
patient1 = create_patient("majok", 30, "Male", "majok@gmail.com")
patient2 = create_patient("Jane Akot", 25, "Female", "jane@gmail.com")

# Create appointment objects
appointment1 = create_appointment("2023-07-11", "10:00 AM", "Dr. Miiro")
appointment2 = create_appointment("2023-07-17", "02:30 PM", "Dr. yesu")

# Create patient portal
portal = PatientPortal()

# Register patients in the portal
register_patient(portal, patient1)
register_patient(portal, patient2)

# Add appointments for patients
patient1.add_appointment(appointment1)
patient2.add_appointment(appointment2)

# Search for a patient by name
search_name = "John Doe"
found_patient = search_patient(portal, search_name)

if found_patient:
    print("Patient found:")
    print("Name:", found_patient.name)
    print("Age:", found_patient.age)
    print("Gender:", found_patient.gender)
    print("Contact:", found_patient.contact)
    print("Appointments:")
    for appointment in found_patient.get_appointments():
        print("Date:", appointment.date)
        print("Time:", appointment.time)
        print("Doctor:", appointment.doctor)
else:
    print("Patient not found.")
