class Client:
    def __init__(self, name, plate_number):
        self.__name = name
        self.__plate_number = plate_number
        self.__verification_ticket = None
        
    
    @property
    def name(self):
        return self.__name
    
    
    @property
    def plate_number(self):
        return self.__plate_number
    
    
    @property
    def verification_ticket(self):
        return self.__verification_ticket
    
    
    @verification_ticket.setter
    def verification_ticket(self, value):
        self.__verification_ticket = value
    
    
    def get_verification_ticket(self, ticket):
        self.verification_ticket = ticket
    