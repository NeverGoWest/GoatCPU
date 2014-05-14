# libraries and stuff
import random # for later usage
import winsound # BLEEP!

# initialization
# memdimensions = int(input("Memory size(best if a number divisible by 2 "))
# mem = [0]*2048 # initialize memory for the CPU
mem = [0 for i in range(2048)] # initialize memory for the CPU
# print('Set mem to ', memdimensions)
debug = 1
console = ""
comhalt = 1
com = ""
comerror = 0
win = 1

# instruction set as a list, for debugging
islist = ["HALT", "MOC", "MOV", "LDA", "STA", "ADD", "ADC", "ACA", "SUB", "SDC", "SCA", "MUL", "MDC", "MCA", "DIV", "DDC", "DCA", "JMP", "JIE", "JIL", "JIG", "JAE", "JAL", "JAG", "SCJ", "MCR", "MCC", "CALL", "RET", "SSP", "MSP", "MSC", "AND", "ANC", "FRT", "ANA", "OR", "ORC", "ORA", "XOR", "XOC", "XOA", "NOR", "NOC", "NOA", "PUSH", "POP", "IN", "OUT"]

mem[0] = 10



# function def's

# memory management stuff
def peekmem(a):
    print(mem[a])

def dumpmem(x, y):

    while x <= y:
        print(mem[x], "", end='')
        x = x + 1
    print()
def ip():
    global mem
    return mem[0]

def instr():
    global mem
    return mem[ip()]

# the programmer
def assemble(adress):
    asmin = ""
    count = adress
    
    while asmin != "q":
        asmin = input(": ")
        args = asmin.split()

        if asmin != "q":
            mem[count] = islist.index(args[0])
            mem[count + 1] = int(args[1])
            mem[count + 2] = int(args[2])

            count += 3
            
        

# misc stuff
def ConsoleOutput():
    pass

def Bleep():
    if win == 0:
        print('\a', end='')
    else:
        winsound.Beep(2500, 500)


# test program
def LoadTest():
    mem[10] = 2; mem[11] = 300; mem[12] = 2 # MOV 300,2; var A
    mem[13] = 2; mem[14] = 301; mem[15] = 4 # MOV 301,2; var B
    mem[16] = 3; mem[17] = 301; mem[18] = 0 # LDA 301  ; load var A into ac
    mem[19] = 7; mem[20] = 300; mem[21] = 0 # ACA 300  ; add ac to value A
    mem[22] = 4; mem[23] = 300; mem[24] = 0 # STA 300  ; store ac in var A
    

# Step()
def Step():
    global mem
    if debug == 1:
        print("Stepping!")
        print(mem[mem[mem[0]]])
        print(mem[0])
        print(islist[instr()])
    if mem[8] == 1:
        print("HALTED, SIGNAL 1")
        comhalt = 1
        return mem[8]
    if mem[mem[0]] == 0: # HALT
        mem[8] = 1
        # print("HALT")
    if mem[mem[0]] == 1: # MOC #A
        argA = mem[mem[0] + 1]
        argB = mem[mem[0] + 2]

        mem[argA] = mem[argB]
    if mem[mem[0]] == 2: # MOV #C,V
        #mem[mem[0] + 1] = mem[mem[0] + 2]
        #mem[mem[mem[1] + 1]] = mem[mem[1] + 2]
        #mem[mem[mem[0]+1]] = mem[mem[0]+2]
        mem[mem[ip()+1]] = mem[ip()+2]
    if mem[mem[0]] == 3: # LDA #D
        mem[3] = mem[mem[ip()+1]] # mem[mem[0] + 1]
    if mem[mem[0]] == 4: # STA #C
        mem[mem[ip()+1]] = mem[3]
    if mem[mem[0]] == 5: # ADD #C
        mem[mem[0] + 1] = mem[mem[0] + 1] + mem[3]
    if mem[mem[0]] == 6: # ADC #A,#B
        # print("ADC not implemented yet lol")
        # mem[mem[0] + 1] = mem[mem[0] + 1] + mem[mem[0] + 2]
        # mem[mem[0]+1] = mem[mem[mem[ip()+1]]] + mem[mem[0]+2]
        mem[mem[ip()+1]] = mem[mem[ip()+1]] + mem[mem[ip()+2]]
        
    if mem[mem[0]] == 7: # ACA #C
        mem[3] = mem[mem[ip()+1]] + mem[3]
    if mem[mem[0]] == 8: # SUB #C
        mem[mem[ip()+1]] = mem[mem[ip()+1]] - mem[3]
    
    mem[0] = mem[0] + 3

    return mem[8]
        

# memory testing functions
# dumpmem(0, 10)
# peekmem(0)

# program loop
while com != "quit":
    global mem
    
    ConsoleOutput()

    com = input("> ") #     Input string
    comargs = com.split() # split up the string to take arguments

    if com == "":
        comerror = 1
    
    if comerror == 0:
        
        if com == "halt":
            comhalt = 1
        if com == "unhalt":
            comhalt = 0
        if com == "run":
            print("Running!")
            comhalt = 0
            while comhalt == 0:
                Step()
                if mem[8] == 1:
                    comhalt = 1
        if comargs[0] == "peek":
            # print("Contents: ")
            if len(comargs) != 2:
                print("Insufficient arguments.")
            else:
                print(comargs[1], ":", mem[int(comargs[1])])
                print()
        if comargs[0] == "dump":
            dumpmem(int(comargs[1]), int(comargs[2]))
        if comargs[0] == "poke":
            mem[int(comargs[1])] = int(comargs[2])
            print("Wrote", comargs[2], "on cell", comargs[1])
        if comargs[0] == "asm":
            assemble(int(comargs[1]))
        if com == "debugon":
            debug = 1
        if com == "debugoff":
            debug = 0
        if com == "loadtest":
            LoadTest()
        if com == "testbleep":
            Bleep()
        if com == "linux":
            win = 0
        if com == "windows":
            win = 1

    comerror = 0
    #else:
    #    print(com, "is not a command.")
    
    

    if comhalt != 1:
        Step()
    
    


# end of program
print('Program has ended.')
string = print('Press any key to continue')
while 1:
    pass
