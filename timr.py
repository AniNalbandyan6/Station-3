import time

def timer(time_list):
    sec = int(time_list[0])*3600+int(time_list[1])*60+int(time_list[2])
    while(sec>0):
        time.sleep(1)
        sec -= 1
        hours = int(sec/3600)
        minutes = int((sec - hours*3600)/60)
        seconds = sec - hours*3600-minutes*60
        print(f"{hours}:{minutes}:{seconds}\n")


time_arr=[" "]
j = 0
while True:
    if time_arr[j].isdigit() != True:
        j=0
        print("Please insert time in the given format with positive numbers only h:m:s\n")
        time_ = input("Insert time (h:m:s) ")
        time_arr = time_.split(":")
    else:
        j+=1
    if j==3:
        break

timer(time_arr)


