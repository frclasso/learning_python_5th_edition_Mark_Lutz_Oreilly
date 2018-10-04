#!/usr/bin/env python3

def entradaNum():
    try:
        num = int(input("Entre com um numero:"))
        print(f'O número é: {num}')

    except:
        raise TypeError("Isso nao é um numero!")

entradaNum()