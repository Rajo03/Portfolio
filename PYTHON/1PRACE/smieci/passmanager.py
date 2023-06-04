from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    def create_key(self,path):
        self.key = Fernet.generate_key()
        with open(path, 'rb)') as f:    
             f.write(self.key)
         
         
    def load_key(self, path):
        with open(path, 'rb)') as f:    
             self.key = f.read()
             
    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        
        if initial_values is not None:
           for key, value in initial_values.items():
               self.add_password(key, value)
           
    def load_passwords_file(self, path):
        self.password_file = path
        
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    def add_password(self, site, password):
        self.password_dict[site] = password
        
        
        if self.password_file is  not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")     
                        
    def get_password(self, site):
        return self.password_dict[site]
    
    
def main():
    password = {
        "email":  "password",
        "facebook": "",
        "youtube":  "",   
    }   
             
             
             
             
             
             
             
             
             
pm = PasswordManager()

print("""Do czego haslo?
 (1) stworz nowe haslo    
 (2) pokaz haslo
 (3) stworz nowy plik z haslami
 (4) pokaz plik z haslami
 (5) dodaj nowe haslo 
 (6) podaj haslo
 (w) wyjscie
 """)



done = False


while not done:
    
    choice = input("wybierz")
    if choice == "1":
        path = input("enter path")
        pm.create_key(path)
    elif choice == "2":
        path = input("Enter path")
        pm.load_key(path)
    elif choice == "3":
        path = input("Enter path")
        pm.create_password_file(path, password)
    elif choice == "4":
        path = input("Enter path")
        pm.load_passwords_file(path)
    elif choice == "5": 
        site = input("Enter path")
        password = input("podaj haslo")
        pm.add_password(site. password)
    elif choice == "6":
        site = input("haslo do jakiej strony")
        print(f"password for {site} is {pm.get_password(site)}")
    elif choice == "w":
        done = True
        print ("Nara")
    else:
        print("zly wybor")
        
        
if __name__ == "__main__":
    main()
        

