import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou!")
        print("Erro: {}".format(error))
        sys.exit()

    print("Socket criado com sucesso!")

    host_alvo = input("Digite o Host ou Ip a ser conectado: ")
    porta_alvo = input("Digite a Porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com sucesso no Host: " + host_alvo + " e na Porta: " + porta_alvo)
        s.shutdown(2)
    except socket.error as error:
        print("A conexão no {} falhou!".format(host_alvo))
        print("Erro: {}".format(error))
        sys.exit()


if __name__ == "__main__":
    main()

        

