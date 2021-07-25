#!/usr/bin/python3
import whois
import socket
import ssl
import nmap
from pyfiglet import Figlet

def primeiro():
    dominio = input("[*] Alvo:")
    consulta = whois.whois(dominio)
    return print (consulta.text)


def segundo():
    dominio = input("[*] Alvo:")
    brute = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

    for nome in brute:
        DNS = nome + "." + dominio
        try:
            teste = print (DNS + ": " + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass

def sub():
    dominio = input("[*] Alvo:")
    brute = ["www", "ftp", "intranet"]
    brute2 = ["login/", "admin", "adm",]

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
def nm():

    choice = input("[1] Apenas uma porta\n[2] Mais de uma porta\n>>")

    if choice == "2":
        target = input("[*] Alvo (IP):")

        begin = input("[I] Porta inicial: ")
        end = input("[F] Porta final:")

        bg = int(begin)
        en = int(end)

        scanner = nmap.PortScanner()

        for i in range(bg,en+1):
            res = scanner.scan(target,str(i))
            res = res['scan'][target]['tcp'][i]['state']
            print(f'[*] Port:  {i} | State: {res}.')
    elif choice == "1":
        target = input("[*] Alvo (IP):")

        porta = input("[P] Porta:")
        p = int(porta)

        scanner = nmap.PortScanner()

        
        res = scanner.scan(target,str(p))
        res = res['scan'][target]['tcp'][p]['state']
        print(f'[*] Port: {p} | State: {res}.')

def inicio():
    print("[*] O programa está em execução")
    print("[*] Digite <Ctrl + C> para sair")
    fig = Figlet(font='standard')
    print("[*] Made By:")
    print(fig.renderText('@ Intellhytus'))
    
    
inicio()


pedido = input("\n\n\n[1] Whois\n[2] Paginas e DNS\n[3] Sub-Dominios e DNS\n[4] PortScan\n[-] Escolha:")

def opc():
    if pedido == "1":
        primeiro()
        
    elif pedido == "2":
        segundo()

    elif pedido == "3":
        sub()
    elif pedido == "4":
        nm()
    else:
        print("[x] Nao valido")

opc()
