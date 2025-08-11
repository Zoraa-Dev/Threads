# Zoraa Dev/Dev Knowing

from Menu.Data.data import *
from Menu.Temporary.DataThreads import Penyimpanan

class edukasi:
    def ___init__(self) -> None:
        pass
        
    def logo(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        print('''
   ____   __     __            _ 
  / __/__/ /_ __/ /_____ ____ (_)
 / _// _  / // /  '_/ _ `(_-</ / 
/___/\_,_/\_,_/_/\_\\_,_/___/_/  
                            ''')
                            
class Login:
    def __init__(self) -> None:
        pass
        
    def cookies_threads(self):
        try:
            edukasi().logo()
            cookies = input("[•] cookies threads: ")
            self.fullname, self.username = Penyimpanan().data_profiles_threads(cookies)
            if len(cookies) >0:
                with open('.cookies_threads.json', mode='w') as r:
                    r.write(json.dumps({
                        'cookie': cookies
                     }))
                    r.close()
                exit(f'[•] success: {self.fullname}/{self.username}, run ulang perintahnya')
            else:
                exit('[•] cookies kosong, masukan cookie threads')
        except (KeyboardInterrupt, Exception) as e:
            exit(f'[•] Error: {str(e).title()}')
            
class Threads:
    def __init__(self) -> None:
        pass
        
    def chek_cookies(self):
        try:
           cookies = json.loads(open('.cookies_threads.json', mode='r').read())['cookie']
           self.chek_profiles(cookies) 
        except (FileNotFoundError) as e:
           print(f'[•] Error: {str(e).title()}')
           time.sleep(3)
           Login().cookies_threads()
        
    def chek_profiles(self, cookies):
        try:
            self.fullname, self.username = Penyimpanan().data_profiles_threads(cookies)
            self.bot_threads(self.fullname, self.username, cookies)
        except (Exception) as e:
            print(f'[•] Error: {str(e).title()}')
            time.sleep(3)
            os.system('rm -rf .cookies_threads.json')
        
    def bot_threads(self, fullname, username, cookies):
        try:
            edukasi().logo()
            print('[•] Threads Fullname: {}'.format(self.fullname))
            print('[•] Threads Username: {}'.format(self.username))
            print('\n\
[01] Edit Bio Profile Threads\n\
[02] Posting Utas Threads\n\
[E] Deleted Cookie\n\
            ')
            query = input('[•] input: ')
            if len(query) >0:
                if query =='01' or query =='1':
                    try:
                        biography = input('[•] Masukan Teks: ')
                        if len(biography) >0:
                            Penyimpanan().edit_bio_profile_threads(cookies, biography)
                        else: exit('[•] Teks Kosong!')
                    except (Exception) as e:
                        exit(f'[•] Error: {str(e).title()}')
                        
                elif query =='02' or query =='2':
                    try:
                        text = input('[•] Masukan Teks: ')
                        if len(text) >0:
                            Penyimpanan().posting_utas_threads(cookies, text)
                        else: exit('[•] Teks Kosong!')
                    except (Exception) as e:
                        exit(f'[•] Error: {str(e).title()}')
                elif query =='E' or query =='e': os.system('rm -rf .cookies_threads.json')
                else: exit('[•] Input Kosong!')    
            else: exit('[•] Input Kosong!')            
                    
        except (Exception) as e:
            exit(f'[•] Error: {str(e).title()}')
        
        
    