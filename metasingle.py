from abc import ABCMeta, abstractmethod

class Company(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        """Implement in child class"""
        pass

class CoSingleton(Company):
    __instance = None
    
    @staticmethod
    def get_instance(Company_name=None, Year_established=None):
        if CoSingleton.__instance is None:
            if Company_name is None or Year_established is None:
                raise ValueError("Initialization parameters are required for the first instance.")
            CoSingleton(Company_name, Year_established)
        return CoSingleton.__instance
    
    def __init__(self, Company_name, Year_established):
        if CoSingleton.__instance is not None:
            raise Exception("Singleton instance already exists!")
        self.Company_name = Company_name
        self.Year_established = Year_established
        CoSingleton.__instance = self
    
    def get_data(self):
        return {"Company_name": self.Company_name, "Year_established": self.Year_established}

    def Data(self):
       
        print(f"Company_name: {self.Company_name}, Year_established: {self.Year_established}")
c = CoSingleton.get_instance("Rubiscape", 2020)        
m = CoSingleton.get_instance()  
z = CoSingleton.get_instance()  

print(m)  
print(z)  
print(c)  
c.Data()  


