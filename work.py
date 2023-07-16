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


# Create patient objects
patient1 = Patient("John Doe", 30, "Male", "john@example.com")
patient2 = Patient("Jane Smith", 25, "Female", "jane@example.com")

# Create appointment objects
appointment1 = Appointment("2023-07-16", "10:00 AM", "Dr. Johnson")
appointment2 = Appointment("2023-07-17", "02:30 PM", "Dr. Anderson")

# Create patient portal
portal = PatientPortal()

# Register patients in the portal
portal.register_patient(patient1)
portal.register_patient(patient2)

# Add appointments for patients
patient1.add_appointment(appointment1)
patient2.add_appointment(appointment2)

# Search for a patient by name
search_name = "John Doe"
found_patient = portal.search_patient(search_name)

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
