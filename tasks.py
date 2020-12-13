from random import randint
import time, random, os, threading, csv, sys
from time import sleep
from playsound import playsound
os.system('cls')
csv_path = 'Thread.csv'
proxy_path = 'Proxies.txt'
proxy_file = open(proxy_path)

info_file = open(csv_path)
file_data = csv.DictReader(info_file)
log = open('Task-Log.txt', 'a')

random_number = ['4','4.5','5','5.5','6','6.5','7','7.5','8','8.5','9','9.5','10','10.5','11','11.5','12','12.5']

def get_len():
    file = open("Thread.csv")
    reader = csv.reader(file)
    lines = len(list(reader))
    return lines




def RandomDelay():
    random_number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    random_delay = random_number[random.randint(0, 15)]
    random_delay_int = int(random_delay)
    time.sleep(random_delay_int)


def tasks(task_number,email,name,sname,size,doorno,street1,street2,city,postcode,paymethod,proxy):
    task = ('\x1b[1;37m[TASK {}] [{}] [SIZE {}] [{}]'.format(task_number,email,size,proxy))
    completed_task = ('\x1b[1;36m[TASK {}] [COMPLETED] [{}] [SIZE {}] [{}]                                  '.format(task_number,email,size,proxy))
    task_log = ('[TASK {}] [{}] [SIZE {}] [{}]\n'.format(task_number,email,size,proxy))
    completed_task_log = ('[TASK {}] [COMPLETED] [{}] [SIZE {}] [{}]\n'.format(task_number,email,size,proxy))  
    print(task,end='\r')
    log.write(task_log)
    print(completed_task,end='\r',)
    #playsound('C:\\Users\\Khush Chauhan\\Desktop\\SNS SCRIPT\\.md\\ding.wav') 
    log.write(completed_task_log)

def init_tasks():
    for i,lines in enumerate(file_data, start=0):
        proxies = proxy_file.readline()[:-1]
        ip = (proxies.split(':')[0])
        port = (proxies.split(':')[1])
        user = (proxies.split(':')[2])
        ippw = (proxies.split(':')[3])
        email = lines['Email']
        fname = lines['F-Name']
        sname = lines['S-Name']
        size = lines['Size']
        Doorno = lines['Door-No']
        Street1 = lines['Street-1']
        Street2 = lines['Street-2']
        City = lines['City']
        Postcode = lines['Post-Code']
        paymethod = lines['Payment-Method']
        delay = 1000 
        time_between_task = int(i) * delay      
        i = i + 1
        if size == 'r': 
            rsize = random_number[random.randint(0, 17)]
            thread = threading.Thread(target=(tasks), args=(i,email,fname,sname,rsize,Doorno,Street1,Street2,City,Postcode,paymethod,ip,))
            thread.start()


        elif size == 'rb':
            rbsize = random_number[random.randint(0, 5)]
            thread = threading.Thread(target=tasks, args=(i,email,fname,sname,rbsize,Doorno,Street1,Street2,City,Postcode,paymethod,proxies,))
            thread.start()

        else:  
            thread = threading.Thread(target=tasks, args=(i,email,fname,sname,size,Doorno,Street1,Street2,City,Postcode,paymethod,proxies,))
            thread.start()


    input()

    

def main():
    
    print('\x1b[1;37m{} Tasks in {}'.format(get_len() - 1,csv_path))
    input()
    time.sleep(0.1)
    #I1 = input("\x1b[1;36mCLICK \x1b[1;37m'\x1b[1;36mENTER\x1b[1;37m' \x1b[1;36mTO START\x1b[1;37m: ")
    init_tasks()
    time.sleep(1)
    log.close()

def main2():
    for i in range(40):
        print("FAILED...") 
    time.sleep(1)
    for i in range(39):
        sys.stdout.write("\033[F") #back to previous line 
    sys.stdout.write("\033[K") #clear line 
    print("SUCCESS!") 
main()





