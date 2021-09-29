
data = 0
START = ["section .text\n", "   global _start  (ld)\n", "\n", "_start:\n", "   mov edx,len\n", "   mov ecs,msg\n", "   mov ebx,1\n", "   mov eax,4\n", "   int	0x80", "/n", "   mov eax,1/n", "   int 0x80/n", "/n", "section	.data"]
PRINT = ["msg db '", data,"', 0xa  ;string to be printed/n", "len equ $ - msg     ;length of the string"]

 
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
      file1 = open('compiled.asm', 'a')
      file1.writelines(PRINT)
      file1.close()
    if data == "START":
      file1 = open('compiled.asm', 'a')
      file1.writelines(START)
      file1.close()
    if data == "Print: ":
      linearprint = 1
