"""
https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

"""
import os

class ApiClient:
    def __init__(self): 
        self.api_key = os.getenv("API_KEY",None) # <--- dependency
        self.timeout = os.getenv("TIMEOUT",None) # <--- dependency
        
class Service:
    
    def __init__(self):
        self.api_client = ApiClient()  # <--- dependency
def main() -> None:
    service = Service() # <--- dependency
    
if __name__=="__main__":
    main()