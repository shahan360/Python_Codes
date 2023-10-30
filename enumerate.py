l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

i=0
for item in l1:
    if i%2 is 0:
        print(f"Jarvis please buy {item}")
    i+=1

for idx,item in enumerate(l1):
    if idx%2==0:
        print(f"Jarvis please buy {item}")