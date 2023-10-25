from tkinter import N


def check_value(s):
    try:
        s=float(s)
        return True
    except:
        return False
print("------C2F conversion system")

while True:
    a=input("Please insert your temp()like 34F, 12C): ")
    if a[-1] in ['F','f'] and check_value(a[:-1]):
        C = (eval(a[0:-1])-32)/1.8
        print("\nDetected {}F;\n The Celsius is {:.1f}C".format(a[:-1],C))
        break
    elif a[-1] in ['C','c'] and check_value(a[:-1]):
        F=1.8*eval(a[0:-1])+32
        print("\nDetected {}C;\n The corresponding {:.1f}F".format(a[:-1],F))
        break
    else:
        print("Wrong format.Please use value +F/C as the input")