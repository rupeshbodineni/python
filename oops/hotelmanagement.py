from abc import ABC, abstractmethod
from datetime import datetime
import json

# ====================== MIXIN ======================
class JsonSerializableMixin:
    """Mixin to add JSON functionality to any class"""
    def to_json(self):
        return json.dumps(self.__dict__, indent=2, default=str)
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)


# ====================== BASE CLASSES ======================
class Person(ABC):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.created_at = datetime.now()

    @abstractmethod
    def get_details(self):
        pass


class Room(ABC):
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_occupied = False
        self.current_guest = None

    @abstractmethod
    def get_room_type(self):
        pass

    def book_room(self, guest):
        if not self.is_occupied:
            self.is_occupied = True
            self.current_guest = guest
            return True
        return False

    def checkout(self):
        if self.is_occupied:
            self.is_occupied = False
            self.current_guest = None
            return True
        return False

    def calculate_cost(self, nights):
        return self.price_per_night * nights


# ====================== CHILD CLASSES ======================

class Guest(Person, JsonSerializableMixin):
    def __init__(self, name, contact, id_proof):
        super().__init__(name, contact)
        self.id_proof = id_proof
        self.booking_history = []

    def get_details(self):
        return f"Guest: {self.name} | Contact: {self.contact} | ID: {self.id_proof}"

    def add_booking(self, room_number):
        self.booking_history.append(room_number)


class Employee(Person):
    def __init__(self, name, contact, employee_id, department, salary):
        super().__init__(name, contact)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name} | Dept: {self.department} | ID: {self.employee_id}"


class StandardRoom(Room, JsonSerializableMixin):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)
        self.max_occupancy = 2
        self.has_ac = True

    def get_room_type(self):
        return "Standard Room"


class DeluxeRoom(Room, JsonSerializableMixin):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)
        self.max_occupancy = 4
        self.has_ac = True
        self.has_balcony = True

    def get_room_type(self):
        return "Deluxe Room"


class Suite(Room, JsonSerializableMixin):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)
        self.max_occupancy = 6
        self.has_ac = True
        self.has_living_room = True
        self.has_jacuzzi = True

    def get_room_type(self):
        return "Suite"


# ====================== MAIN HOTEL CLASS ======================
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}
        self.guests = {}
        self.employees = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def add_guest(self, guest):
        self.guests[guest.contact] = guest

    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee

    def book_room(self, room_number, guest_contact, nights):
        if room_number not in self.rooms:
            return "Room not found!"
        
        room = self.rooms[room_number]
        guest = self.guests.get(guest_contact)
        
        if not guest:
            return "Guest not found!"
        
        if room.book_room(guest):
            cost = room.calculate_cost(nights)
            guest.add_booking(room_number)
            return f"Room {room_number} booked successfully!\nTotal Cost: ₹{cost}"
        else:
            return "Room is already occupied!"

    def checkout_room(self, room_number):
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if room.checkout():
                return f"Room {room_number} checked out successfully!"
            return "Room was not occupied."
        return "Room not found!"

    def show_available_rooms(self):
        print(f"\nAvailable Rooms in {self.name}:")
        for room in self.rooms.values():
            if not room.is_occupied:
                print(f"Room {room.room_number} - {room.get_room_type()} - ₹{room.price_per_night}/night")


# ====================== USAGE EXAMPLE ======================

if __name__ == "__main__":
    # Create Hotel
    taj = Hotel("Taj Palace")

    # Add Rooms
    taj.add_room(StandardRoom(101, 3000))
    taj.add_room(DeluxeRoom(201, 6000))
    taj.add_room(Suite(301, 15000))

    # Add Guests
    g1 = Guest("Rahul Sharma", "9876543210", "Aadhar-9876")
    g2 = Guest("Priya Patel", "8765432109", "Passport-X1234")
    taj.add_guest(g1)
    taj.add_guest(g2)

    # Add Employee
    manager = Employee("Amit Kumar", "9123456789", "EMP001", "Management", 85000)
    taj.add_employee(manager)

    # Book Rooms
    print(taj.book_room(101, "9876543210", 3))
    print(taj.book_room(201, "8765432109", 2))

    # Show Available Rooms
    taj.show_available_rooms()

    # Checkout
    print(taj.checkout_room(101))

    # Show Guest Details
    print("\nGuest Details:")
    print(g1.get_details())
    print(g2.get_details())

    # JSON Example
    print("\nGuest JSON:")
    print(g1.to_json())