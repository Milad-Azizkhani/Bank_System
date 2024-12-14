import serial
from playsound import playsound
import time
from IPython.display import clear_output

serialport=serial.Serial('COM3',baudrate=9600,timeout=2)
time.sleep(4)
i=0
j=1
while True :
  arduinodata=serialport.readline()
  str_rn = arduinodata.decode()
  s=str_rn.rstrip()
  serial_output=s.split('.')
 # print(serial_output[1])
  if serial_output[0]=='0' :
      print('Please Waiting')
  if serial_output[0]=='1' :
      if serial_output[1]=='1' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\1.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\1.mp3')
          
      if serial_output[1]=='2' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\1.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\2.mp3')
          
      if serial_output[1]=='3' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\1.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\3.mp3')
          
      if serial_output[1]=='4' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\1.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\4.mp3')
          

  if serial_output[0]=='2' :
      if serial_output[1]=='1' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\2.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\1.mp3')
         
      if serial_output[1]=='2' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\2.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\2.mp3')
          
      if serial_output[1]=='3' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\2.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\3.mp3')
          
      if serial_output[1]=='4' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\2.mp3')
       
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\4.mp3')
          
  if serial_output[0]=='3' :
      if serial_output[1]=='1' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\3.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\1.mp3')
          
      if serial_output[1]=='2' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\3.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\2.mp3')
          
      if serial_output[1]=='3' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\3.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\3.mp3')
          
      if serial_output[1]=='4' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\3.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\4.mp3')
          
  if serial_output[0]=='4' :
      if serial_output[1]=='1' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\4.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\1.mp3')
          
      if serial_output[1]=='2' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\4.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\2.mp3')
          
      if serial_output[1]=='3' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\4.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\3.mp3')
          
      if serial_output[1]=='4' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\4.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\4.mp3')
         
  if serial_output[0]=='5' :
      if serial_output[1]=='1' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\5.mp3')
         
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\1.mp3')
          
      if serial_output[1]=='2' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\5.mp3')
        
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\2.mp3')
          
      if serial_output[1]=='3' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\5.mp3')
      
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\3.mp3')
          
      if serial_output[1]=='4' :
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\number\\new\\5.mp3')
        
         playsound('D:\\my classes in university\\term 7\\Mechanics measuerment\\project\\project\\to\\new\\4.mp3')
      break
serial.close()
clear_output(wait=True)