# Zoraa Dev/Dev Knowing
from Menu.menu import Threads

class DancokKontolMemek:
    def __init__(self) -> None:
        pass
    
    def HidupPenuhCobaanCok(self):
        try: Threads().chek_cookies()
        except (Exception) as e:
            exit(f'[•] Error: {str(e).title()}')
        
if __name__ == '__main__':
        DancokKontolMemek().HidupPenuhCobaanCok()
        
        
            

        