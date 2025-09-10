section .data
    a db 5
    b db 3

    newline db 10

    ascii_base db 48

section .bss
    res resb 2

section .text
    global _start

_start:

    mov rax, [a]
    mov rbx, [b]
    
    ; suma a con b
    add rax, rbx        ; rax = rax + rbx -> rax = 5 + 3
    ;mov rcx, [ascii_base]
    ;add rax, rcx

    mov rcx, res
    mov [rcx], rax
    add rcx, 1
    mov rdx, [newline]
    mov [rcx], rdx

    ;syswrite
    mov rax, 1
    mov rdi, 1
    mov rsi, res
    mov rdx, 2
    syscall

    ;sysexit
    mov rax, 60
    mov rdi, 0
    syscall    
