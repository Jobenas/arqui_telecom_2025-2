section .data
    mensaje db "Hola mundo!", 10 ; Cadena de caracteres a imprimir
    ;len equ $ - mensaje

section .text
    global _start

_start:

print:
    ; syscall write
    mov rax, 1          ; rax = 1 -> syscall write
    mov rdi, 1          ; rdi = 1
    mov rsi, mensaje    ; (buffer) rsi = &mensaje
    mov rdx, 11         ; rdx = len
    syscall

exit:
    ;exit(0)
    mov rax, 60         ; rax = 60 -> syscall exit
    mov rdi, 0          ; rdi = 0
    syscall

