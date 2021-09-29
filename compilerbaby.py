
data = 0
lennumber = 0
letter = 0
START = ["section .text\n", "   global _start  (ld)\n", "\n", "_start:\n", "   mov edx,len\n", "   mov ecs,msg\n", "   mov ebx,1\n", "   mov eax,4\n", "   int	0x80", "/n", "   mov eax,1/n", "   int 0x80/n", "/n", "section	.data"]
PRINTA = ["msg db '", data,"', 0xa  ;string to be printed\n", "len equ $ - msg     ;length of the string\n"]

 
# Using readlines()
file1 = open('scr.d', 'r')
Lines = file1.readlines()

linearprint = 0
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    data = .format(count, line.strip())
    if linearprint == 1:
      PRINT = ["msg db '", data,"', 0xa  ;string to be printed/n", "len" + lennumber " equ $ - msg     ;length of the string\n"]
      file1 = open('compiled.asm', 'a')
      file1.writelines(PRINT)
      file1.close()
    if data == "START":
      file1 = open('compiled.asm', 'a')
      file1.writelines(START)
      file1.close()
    if data == "Print: ":
      linearprint = 1
    if data == "section .script":
       for letter in Lines:
          printa = 0
          printb = 0
          printc = 0
          vara = 0
          varb = 0
          varc = 0
          ifa = 0
          ifb = 0
          ifc = 0
          jea = 0
          jeb = 0
          jec = 0
          if jec == 1:
             if letter != ";":
                vamdata = vamdata + letter
             else:
                vamdata = 0
                printa = 0
                printb = 0
                printc = 0
                vara = 0
                varb = 0
                varc = 0
                ifa = 0
                ifb = 0
                ifc = 0
                jea = 0
                jeb = 0
                jec = 0   
                lennumber = lennumber + 1
                file1 = open('compiled.asm', 'a')
                file1.writelines(varc)
                file1.close()
          lennumber = 0
          if printc == 1:
             if letter != ";":
                if letter != "_":
               
                    putdata = putdata + letter
             
             else:
                putdata = 0
                lennumber = lennumber + 1
                printa = 0
                printb = 0
                printc = 0
                vara = 0
                varb = 0
                varc = 0
                ifa = 0
                ifb = 0
                ifc = 0
                jea = 0
                jeb = 0
                jec = 0
                printc = 0
                PRINTA = ["msg", lennumber, " db '", putdata,"', 0xa  ;string to be printed\n", "len " , lennubmer," equ $ - msg     ;length of the string\n"]
                file1 = open('compiled.asm', 'a')
                file1.writelines(PRINTA)
                file1.close()
          if ifc == 1:
             if letter != ";":
                if letter != ".":
                   
                   ifdata = ifdata + letter
             
             else:
                printa = 0
                printb = 0
                printc = 0
                vara = 0
                varb = 0
                varc = 0
                ifa = 0
                ifb = 0
                ifc = 0
                jea = 0
                jeb = 0
                jec = 0
                lennumber = lennumber + 1
                printc = 0
                IFDATAC = ["CMP", ifdata,"\n"]
                file1 = open('compiled.asm', 'a')
                file1.writelines(IFDATAC)
                file1.close()
          
          if varc == 1:
             if letter != ";":
                vardata = vardata + letter
             else:
                printa = 0
                printb = 0
                printc = 0
                vara = 0
                varb = 0
                varc = 0
                ifa = 0
                ifb = 0
                ifc = 0
                jea = 0
                jeb = 0
                jec = 0   
                lennumber = lennumber + 1
                file1 = open('compiled.asm', 'a')
                file1.writelines(varc)
                file1.close()
          if printc and varc and jec != 1:
             if letter == "p":
                printa = 1
             if printa == 1:
                if letter == "u":
                   printb = 1
             if printb == 1:
                if letter == "t":
                   printc = 1
             if letter == "a":
                vara = 1
             if vara == 1:
                if letter == "s":
                   varb = 1
             if varb == 1:
                if letter == "m":
                   varc = 1
             if letter == "i":
                vara = 1
             if ifa == 1:
                if letter == "f":
                   ifb = 1
             if varb == 1:
                if letter == "1":
                   ifc = 1
             if letter == "j":
                jea = 1
             if jea == 1:
                if letter == "i":
                   jeb = 1
             if jeb == 1:
                if letter == "f":
                   jec = 1
             
          
                
                      
