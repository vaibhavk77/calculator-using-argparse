import argparse
 

def add(a,b):
    val = a+b
    return val
 

def sub(a,b):
    val = a-b
    return val
 

def div(a,b):
    val = a/b
    return val
 
def multi(a,b):
    val = a*b
    return val
 

parser = argparse.ArgumentParser()
 
x = parser.add_mutually_exclusive_group()
x.add_argument("-fa",action="store_true")
x.add_argument("-fs",action="store_true")
x.add_argument("-fd",action="store_true")
x.add_argument("-fm",action="store_true")
 
parser.add_argument("num1",type=float)
parser.add_argument("num2",type=float)
 
args = parser.parse_args()
     
 
if args.fa:
    print((add(args.num1,args.num2)))
elif args.fs:
    print((sub(args.num1,args.num2)))
elif args.fd:
    print((div(args.num1,args.num2)))
elif args.fm:
    print((multi(args.num1,args.num2)))
else:
    print("Error:Requires an argument to perform an action")
 
