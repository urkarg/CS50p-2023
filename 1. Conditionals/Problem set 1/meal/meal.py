def main():
    t = input("What's the time? ")
    t = convert(t)
    if 7<= t <=8:
        print("breakfast time")
    elif 12<= t <=13:
        print("lunch time")
    elif 18<= t <=19:
        print("dinner time")

def convert(time):
    if time.endswith("p.m."):
        time=time.replace("p.m.","")
        t1, t2 = time.split(sep=":")
        if t1 == "12":
            t1=float(t1)
        else:
            t1 = float(t1)+12
    else:
        if time.endswith("a.m."):
            time=time.replace("a.m.","")
        t1, t2 = time.split(sep=":")
        t1 = float(t1)
    t2 = float(t2)/60
    return t1+t2

if __name__ == "__main__":
    main()