
import string
import random
from typing import List


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: str = "fifo"):
        # if its empty , dont do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        if(processing_strategy == "fifo"):
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif(processing_strategy == "filo"):
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif(processing_strategy == "random"):
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("======================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer} ")
        print(f"Issue {ticket.issue}")
        print("======================================")


app = CustomerSupport()

# register a few tickets

app.create_ticket("John", "My computer make strange sounds!")
app.create_ticket("Arjan", "VSCode dont save my work")
app.create_ticket("Linus", "I cant upload videos")

app.process_tickets("filo")

# The problem with this code relay in the if statement. 
# # If you add more strategies need to extends conditions
# so process_tickets have low cohesion. Because is responsable not only
# tickers also for implement strategies