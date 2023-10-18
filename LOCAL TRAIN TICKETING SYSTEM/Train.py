class Train:
    def __init__(self, train_id, name, source, destination, fare, capacity):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.fare = fare
        self.capacity = capacity
        self.available_seats = capacity

    def book_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def check_availability(self):
        return self.available_seats

class TicketingSystem:
    def __init__(self):
        self.trains = {}

    def add_train(self, train):
        self.trains[train.train_id] = train

    def get_train(self, train_id):
        return self.trains.get(train_id)

    def book_ticket(self, train_id, num_tickets):
        train = self.get_train(train_id)
        if train is not None:
            return train.book_ticket(num_tickets)
        else:
            return False

    def check_train_availability(self, train_id):
        train = self.get_train(train_id)
        if train is not None:
            return train.check_availability()
        else:
            return None

def main():
    ticketing_system = TicketingSystem()

    # Adding some sample trains
    train1 = Train(1, "Express 1", "City A", "City B", 100, 50)
    train2 = Train(2, "Local 1", "City A", "City C", 50, 30)

    ticketing_system.add_train(train1)
    ticketing_system.add_train(train2)

    while True:
        print("1. Book Ticket")
        print("2. Check Train Availability")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            train_id = int(input("Enter Train ID: "))
            num_tickets = int(input("Enter the number of tickets: "))
            if ticketing_system.book_ticket(train_id, num_tickets):
                print(f"Tickets booked successfully for Train {train_id}.")
            else:
                print("Booking failed. Insufficient seats or invalid Train ID.")

        elif choice == '2':
            train_id = int(input("Enter Train ID: "))
            availability = ticketing_system.check_train_availability(train_id)
            if availability is not None:
                print(f"Train {train_id} has {availability} seats available.")
            else:
                print("Train not found.")

        elif choice == '3':
            break

if __name__ == "__main__":
    main()
