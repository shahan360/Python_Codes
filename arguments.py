sk = ["Govi","Hari","Palak","Lauki","Kathal"]
normie = "This is a normie sabzi"
kwsabzi = {"TKS":"Tinda","BKS":"Bhindi","LKS":"Lauki","AKS":"Aloo"}

def sabziargs(nsabzi,*sksabzi,**kwasabzi):
    print(nsabzi)
    for i in sksabzi:
        print(i)
    for i,e in kwasabzi.items():
        print(f"{i} sabzi hai {e} ki")

sabziargs(normie,*sk,**kwsabzi)