import csv
import datetime as dt
import math

#create a file name from current date and time
fileName=  dt.datetime.strftime(dt.datetime.now(), '%Y-%n-%d-%H-%M-%S.csv')

#open the file with the filename
with open(fileName, "w" , newline='') as f:
    #enables csv writing to the file
    writer = csv.writer(f)
    #write a header row
    writer.writerow("i", "j", "gcd")
    #write the gcd for all i and j pairs from 0 to 100
    for i in range(100):
        for j in range(100):
            writer.writerow(i, j, math.gcd(i, j))
