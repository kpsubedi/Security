import my_debugger

debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to:")
debugger.attach(int(pid))
all_list = debugger.enumerate_threads()
#debugger.run()
#print all_list
# for each thread in list display registers

for thread in all_list:
	thread_context = debugger.get_thread_context(thread)
	# Now output the register
	print "[*] Dumping registers for thread ID: 0x%08x" % thread
	print "[*] EIP: 0x%08x" % thread_context.Eip
	print "[*] ESP: 0x%08x" % thread_context.Esp
	print "[*] EBP: 0x%08x" % thread_context.Ebp
	print "[*] EAX: 0x%08x" % thread_context.Eax
	print "[*] EBX: 0x%08x" % thread_context.Ebx
	print "[*] ECX: 0x%08x" % thread_context.Ecx
	print "[*] EDX: 0x%08x" % thread_context.Edx
debugger.detach()
#debugger.load("C:\\WINDOWS\\system32\\calc.exe")