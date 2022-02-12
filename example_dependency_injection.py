"""
https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

"""
### before

import os


class ApiClient:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")  # <-- dependency
        self.timeout = os.getenv("TIMEOUT")  # <-- dependency


class Service:

    def __init__(self):
        self.api_client = ApiClient()  # <-- dependency


def main() -> None:
    service = Service()  # <-- dependency
    ...


if __name__ == "__main__":
    main()
    
    
### after


import os

class ApiClient:
    def __init__(self, api_key:str, timeout: int): 
        self.api_key = api_key # <-- dependency injected
        self.timeout = timeout # <-- dependency injected
        
class Service:
    
    def __init__(self , api_client: ApiClient): # <-- dependency injected
        self.api_client = api_client # <-- dependency injected
def main(service: Service) -> None: # <-- dependency injected
    pass
    
if __name__=="__main__":
    main(Service(ApiClient(
        api_key=os.getenv("API_KEY"),
        timeout=os.getenv("TIMEOUT")
    )))