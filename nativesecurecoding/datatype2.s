	.file	"datatype2.c"
	.text
.globl copy
	.type	copy, @function
copy:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	cmpq	$0, -24(%rbp)
	jne	.L2
	movl	$0, %eax
	jmp	.L3
.L2:
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	malloc
	movq	%rax, -16(%rbp)
	cmpq	$0, -16(%rbp)
	jne	.L4
	movl	$0, %eax
	jmp	.L3
.L4:
	movl	$0, -4(%rbp)
	jmp	.L5
.L6:
	movl	-4(%rbp), %eax
	cltq
	addq	-16(%rbp), %rax
	movq	-32(%rbp), %rdx
	movzbl	(%rdx), %edx
	movb	%dl, (%rax)
	addq	$1, -32(%rbp)
	addl	$1, -4(%rbp)
.L5:
	movl	-4(%rbp), %eax
	cltq
	cmpq	-24(%rbp), %rax
	jb	.L6
	movq	-16(%rbp), %rax
.L3:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	copy, .-copy
	.section	.rodata
.LC0:
	.string	"Hello, World!"
	.text
.globl main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movl	%edi, -36(%rbp)
	movq	%rsi, -48(%rbp)
	movl	$-2147483549, -24(%rbp)
	movl	$0, -20(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, %rsi
	movl	$1, %edi
	call	calloc
	movq	%rax, -8(%rbp)
	cmpq	$0, -8(%rbp)
	jne	.L9
	movl	$1, %eax
	jmp	.L10
.L9:
	movq	-8(%rbp), %rax
	movl	$14, %edx
	movl	$.LC0, %esi
	movq	%rax, %rdi
	call	memcpy
	movq	-8(%rbp), %rdx
	movq	-24(%rbp), %rax
	movq	%rdx, %rsi
	movq	%rax, %rdi
	call	copy
	movq	%rax, -16(%rbp)
	cmpq	$0, -16(%rbp)
	jne	.L11
	movl	$1, %eax
	jmp	.L10
.L11:
	jmp	.L8
.L10:
.L8:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (GNU) 4.4.7 20120313 (Red Hat 4.4.7-11)"
	.section	.note.GNU-stack,"",@progbits
