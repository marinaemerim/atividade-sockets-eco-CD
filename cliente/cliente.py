"""
Cliente de Eco — Atividade Prática de Sistemas Distribuídos
UFSC — Proposta de Abordagem para o Ensino de Computação Distribuída

Um cliente TCP que se conecta ao servidor, envia uma mensagem e exibe
a resposta recebida (eco).
"""

import socket
import sys
from datetime import datetime


def log(msg):
    ts = datetime.now().isoformat(timespec='microseconds')
    print(f"[{ts}] {msg}")

# Nome do host (ou IP) do servidor.
# "servidor" é o hostname definido no docker-compose.yml — o Docker
# resolve automaticamente esse nome para o IP interno do contêiner.
HOST_SERVIDOR = "servidor"
PORTA_SERVIDOR = 5000

TAMANHO_BUFFER = 1024


def enviar_mensagem(mensagem: str):
    # 1. Criar o socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Conectar ao servidor pelo hostname e porta
    log(f"[CLIENTE] Conectando a {HOST_SERVIDOR}:{PORTA_SERVIDOR} ...")
    cliente_socket.connect((HOST_SERVIDOR, PORTA_SERVIDOR))
    log("[CLIENTE] Conexão estabelecida.")

    # 3. Enviar a mensagem codificada em bytes (UTF-8)
    cliente_socket.sendall(mensagem.encode("utf-8"))
    log(f"[CLIENTE] Mensagem enviada: '{mensagem}'")

    # 4. Aguardar e receber o eco do servidor
    resposta = cliente_socket.recv(TAMANHO_BUFFER).decode("utf-8")
    log(f"[CLIENTE] Eco recebido do servidor: '{resposta}'")

    # 5. Encerrar a conexão
    cliente_socket.close()
    log("[CLIENTE] Conexão encerrada.")


if __name__ == "__main__":
    # A mensagem pode ser passada como argumento ou usa um valor padrão
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = "Olá, Sistemas Distribuídos!"

    enviar_mensagem(msg)
