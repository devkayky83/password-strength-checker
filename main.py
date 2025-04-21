import re

class PasswordChecker:
    def __init__(self):
        self.common_passwords = set(self.load_common_passwords())
        
    
    def load_common_passwords(self):
        try:
            with open('common_passwords.txt', 'r') as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            return []
        
    def check_strength(self, password):
        if password in self.common_passwords:
            return "Fraca (senha comum)"
        
        length = len(password)
        has_upper = re.search(r'[A-Z]', password)
        has_lower = re.search(r'[a-z]', password)
        has_digit = re.search(r'\d', password)
        has_symbol = re.search(r'\W', password)
        
        score = sum([bool(has_upper), bool(has_lower), bool(has_digit), bool(has_symbol)])
        
        if length < 6 or score < 2:
            return "Fraca"
        elif length < 10:
            return "Media"
        else:
            return "Forte"
        

if __name__ == "__main__":
    checker = PasswordChecker()
    while True:
        senha = input("Digite uma senha para verificar (Digite 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            break
        print("Classificação:", checker.check_strength(senha))