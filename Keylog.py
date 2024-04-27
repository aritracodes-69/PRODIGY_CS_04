
log = ""

def write_to_file(log):
    with open("keylog.txt", "a") as f:
        f.write(log + "\n")

def on_press(key):
    global log
    try:
        # Convert the pressed key to a string and append it to the log
        log += str(key)
    except:
        log += " " + str(key) + " "

while True:
    key = input("Press a key (Press 'q' to quit): ")
    
    if key.lower() == 'q':
        break
    
    on_press(key)
write_to_file(log)

