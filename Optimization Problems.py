import ipaddress
import re
import timeit
fib = {"data":[]}

def houston ():
    houstonIP =[]
    f1 = open("houston.txt",'r')
    trigger = False
    # worse case runtime o(n) (houston is at the bottom and has no ips)
    for line in f1:
        
        if trigger == True:
            if line[0].isdigit():
                parts = []
                parts = line.split(" ")
                houstonIP.append(parts[0])

            else:
            ## comments can be present in the file
            ## so I need to make sure this isnt a comment before proceeding
            ## note: this is assuming comments cannot start with "["
                if line[0] == "[":
                    break
        if line[:9] == "[Houston]" or line[:9] == "[houston]":
            trigger = True

    return houstonIP

## runtime is O(1.618^n)
def recFib (n):
    if n < 2:
        return n
    return recFib(n-2) + recFib(n-1)

# Runtime is O(n)
def dynamicFib(n):
    n1 = 1
    n2 = 1
    if n < 0 or n > 26:
        print("incorrect input")
        return 0
    elif n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        for i in range (2,n+1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2


## runtime is linear to build data structure
def createFibDictionary():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,26):
        fibVal={}
        answer= ""
        letter = alphabet[i]
        fibVal["element"]=i+1
        fibVal["fibonacci"] = dynamicFib(i)
        for i in range(fibVal["fibonacci"]):
            answer += letter
        fibVal["answer"] = answer
        addToGlobal(fibVal)
       

        
def addToGlobal(Dict):
    fib["data"].append(Dict)
        
## First runthrough is O(n) to build data structure
## after that runtime is O(1) 
def fibFunction(fibIndex):
    if fibIndex > 0 and fibIndex <=26:
        if fib == {"data":[]}:
            createFibDictionary()

        return fib["data"][fibIndex-1]['answer']
    else:
        return ""

def fibFunctionTimed(fibIndex):
    start = timeit.default_timer()
    if fibIndex > 0 and fibIndex <=26:
        if fib == {"data":[]}:
            createFibDictionary()
        stop = timeit.default_timer()
        print("Time : ", stop-start)
        return fib["data"][fibIndex-1]['answer']
    else:
        return ""

## runtime is O(n) where n is the number of lines in the file
def zones():
    validIP = []
    f2 = open("zone.txt",'r')
    answer = ""
    for line in f2:
        #Strip newlines to ensure isValidIPv4 works correctly
        line = line.rstrip('\n\r')
        if line[0].isdigit():
            if isValidIPv4(line):
                answer += line
                answer += ","
    answer = answer[:len(answer)-1]
    return answer
## runtime is o(1) each ip has 4 parts and is checked in constant time.
def isValidIPv4(ip):
    sec = ip.split(".")
    if len(sec) != 4:
        #print("False len")
        return False
    for i in sec:
        #print(len(i))
        if not 0 <= int(i) <= 255:
            #print("False num")
            return False
        if len(i) > 3 or len(i) == 0:
            #print("False count")
            return False

    return True
