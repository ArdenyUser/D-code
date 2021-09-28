section	.text
   global _start     ;must be declared for linker (ld)
	
_start:	            ;tells linker entry point
   mov	edx,len     ;message length
   mov	ecx,msg     ;message to write
   mov	ebx,1       ;file descriptor (stdout)
   mov	eax,4       ;system call number (sys_write)
   int	0x80        ;call kernel
	
   mov	eax,1       ;system call number (sys_exit)
   int	0x80        ;call kernel
# Python code to
# demonstrate readlines()
 
START = ["section .text\n", "   global _start  (ld)\n", "Geeks\n"]
 
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
