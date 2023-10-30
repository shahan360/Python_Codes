import time

initial = time.time()
k = 0
while(k<12):
    print(f"This is {k}th iteration of while loop.")
    k+=1
print("This while loop ran in ",time.time()-initial," Seconds")

init2 = time.time()
for i in range(12):
    print(f"This is {i}th iteration of for loop.")
print("This for loop ran in ",time.time()-init2," Seconds")

loctime = time.asctime(time.localtime(time.time()))
print(loctime)