def maxValue(n: str, x: int) -> str:
    out = "" 
    if(n[0] == "-"):
        # negative
        for i in n:
            if(i=="-" or int(i)<x):
                out+=i
            else:
                out+=str(x)
                out+=i
    else:
        # positive
        for i in n:
            if(int(i)>x):
                out+=i
            elif(int(i)==x):
                out+=i
            else:
                out+=str(x)
                out+=i
    return out
   


if __name__ == "__main__":
    n = "-13"
    x = 2
    print(maxValue(n, x))

