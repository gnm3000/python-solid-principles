
"""
Advanced employee Managament systems
Two main problems:
1) There are a lot of code duplication
2) the classes has a lot responsabilities


"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Employee(ABC):
    """ basic representation of employee """
    name: str
    id: int
    
    @abstractmethod
    def compute_pay(self) -> float:
        """ compute how much should be paid"""

@dataclass
class HourlyEmployee(Employee):
    """ Employee that's paid based on number of worked hours"""
    
    comission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000
    
    def compute_pay(self) -> float:
        """ compute how much should be paid"""
        return (
            self.pay_rate * self.hours_worked + self.employer_cost 
            + self.comission*self.contracts_landed
        )




@dataclass
class SalariedEmployee(Employee):
    """ employee that's paid based on a fixed monthly salary"""
    
    monthly_salary: float = 0
    percentage: float = 1
    def compute_pay(self) -> float:
        """ compute how much should be paid"""
        return (
            self.monthly_salary* self.percentage
            
        )
@dataclass
class SalariedEmployeeWithComission(SalariedEmployee):
    """ employee that's paid based on a fixed monthly salary and get a comission"""
    
    comission: float = 100
    contracts_landed: float = 0
    def compute_pay(self) -> float:
        """ compute how much should be paid"""
        return (
            super().compute_pay()+
            
            + self.comission * self.contracts_landed
        )
@dataclass
class Freelancer(Employee):
    """ freelancer basid on number of worked hours"""
    
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""
    
    def compute_pay(self):
        """ """
        return (
            self.pay_rate * self.hours_worked 
        )
 @dataclass
class FreelancerWithComission(Freelancer):
    """ freelancer basid on number of worked hours with comission """
    
    comission: float = 100
    contracts_landed: float = 0
    
    
    def compute_pay(self):
        """ """
        return (
           super().compute_pay() + self.comission*self.contracts_landed
        )       
def main() -> None:
    """Main function."""

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithComission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()