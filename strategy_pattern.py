
import re
import string
import random
from typing import List, Callable
from abc import ABC,abstractmethod

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

# lets create a basic strategy for us
class TicketOrderingStrategy(ABC):
    
    @abstractmethod
    def create_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
        pass
    
def fifo_ordering(list: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()

def filo_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = (list.copy())
    list_copy.reverse()
    return list_copy

def blackhole_ordering(list: List[SupportTicket]) -> List[SupportTicket]:
    return []
    
    
def random_ordering(list: List[SupportTicket]) -> List[SupportTicket]:
    
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy
    
    
    


class CustomerSupport:
    

    tickets: List[SupportTicket] = []

    def __new__(cls):
        return super(CustomerSupport,cls).__new__(cls)
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
        
    def process_tickets(self, processing_strategy_fn : Callable[[List[SupportTicket]],List[SupportTicket]]):
        
        # create ordered list
        ticket_list = processing_strategy_fn(self.tickets)
        # if its empty , dont do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in ticket_list:
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

app.process_tickets(random_ordering)

# The problem with this code relay in the if statement. 
# # If you add more strategies need to extends conditions
# so process_tickets have low cohesion. Because is responsable not only
# tickers also for implement strategies

# NOW we are going to design a functional strategies. 