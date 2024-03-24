# Python-PulseTech-RPI-Comp
This code allows you to take your heartrate from a Heartrate sensor (MAX 30101) and display it on a LCD Display. The heartrate data is constantly being sent to a txt file. Then on a press of a button the txt file is sent to a website. In my case it is the Gauntlet website. This can be found in my profile.

For this to work you need to add this code to the bottom of your flask website:
@app.route("/processfile")


def process_file():
    file = open("static/uploads/hr.txt","r")
    # this is where your txt file is #
    data = file.read().splitlines() #data will be an array of lines from text file
    #print(data)
    total = 0
    count = 0
    for i in range(5, len(data)-1):#loop through all lines execept last
        print(data[i])
        total = total + float(data[i])
        count = count + 1
    average = total / count
    return("Average heart rate is " + str(average) )

Any Questions let me know
