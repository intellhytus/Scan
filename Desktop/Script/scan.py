#!/usr/bin/python3
import whois
import socket

def primeiro():
    dominio = input("Alvo:")
    consulta = whois.whois(dominio)
    return print (consulta.text)


def segundo():
    dominio = input("Alvo:")
    brute = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

    for nome in brute:
        DNS = nome + "." + dominio
        try:
            teste = print (DNS + ": " + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass

def sub():
    dominio = input("Alvo:")
    brute = ["www", "ftp", "intranet"]
    brute2 = ["login/", "admin", "adm", "gestao", "privado"]

    for name in brute:
        pag = name + "." + dominio
        pag2 = "" + name + dominio
        for nome in brute2:
            pag1 = pag + "/" + nome
            pag3 = pag2 + "/" + nome
            try:
                teste = print (pag1 + ": " + socket.gethostbyname(pag))
                teste1 = print (pag3 +": " + socket.gethostbyname(pag2)) 
            except socket.gaierror:
                pass

def inicio():
    print("Made By: @intellhytus")
    
    
inicio()          

pedido = input("\n\n\n\n\nWhois: Digite 1\nPaginas e DNS: Digite 2\nSub-Dominios e DNS: Digite 3\nEscolha: ")

def opc():
    if pedido == "1":
        primeiro()

    elif pedido == "2":
        segundo()

    elif pedido == "3":
        sub()

    else:
        print("Nao valido")

opc()
