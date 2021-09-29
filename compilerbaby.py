
# Python code to
# demonstrate readlines()
 
START = ["section .text\n", "   global _start  (ld)\n", "\n", "_start:\n", "   mov edx,len\n", "   mov ecs,msg\n", "   mov ebx,1\n", "   mov eax,4\n", "   int	0x80", "/n", "   mov eax,1", "   int 0x80"]
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
 
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    data = .format(count, line.strip())
    if data == "START":
      file1 = open('scr.d', 'w')
      file1.writelines(START)
      file1.close()
