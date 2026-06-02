"""
Servidor de Eco — Atividade Prática de Sistemas Distribuídos
UFSC — Proposta de Abordagem para o Ensino de Computação Distribuída

Um servidor TCP simples que recebe uma mensagem de um cliente e a devolve
(eco). Cada conexão é atendida sequencialmente (servidor single-threaded).
"""

import socket
from datetime import datetime


def log(msg):
    ts = datetime.now().isoformat(timespec='microseconds')
    print(f"[{ts}] {msg}")

# Endereço e porta onde o servidor vai escutar.
# "0.0.0.0" significa: aceitar conexões de qualquer interface de rede.
HOST = "0.0.0.0"
PORTA = 5000

# Tamanho máximo (em bytes) de cada mensagem recebida.
TAMANHO_BUFFER = 1024

# Contador de mensagens recebidas 
total_mensagens = 0


def iniciar_servidor():
    global total_mensagens

    # 1. Criar o socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reusar a porta imediatamente após reiniciar o servidor
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. Associar o socket ao endereço e porta (bind)
    servidor_socket.bind((HOST, PORTA))

    # 3. Colocar o socket em modo de escuta; aceita até 5 conexões na fila
    servidor_socket.listen(5)

    log(f"[SERVIDOR] Escutando em {HOST}:{PORTA} ...")

    while True:
        # 4. Aguardar e aceitar uma nova conexão de cliente
        conn, endereco_cliente = servidor_socket.accept()
        log(f"[SERVIDOR] Conexão estabelecida com {endereco_cliente}")

        # 5. Receber dados do cliente
        dados = conn.recv(TAMANHO_BUFFER)

        if dados:
            mensagem = dados.decode("utf-8")
            log(f"[SERVIDOR] Mensagem recebida: '{mensagem}'")
            total_mensagens += 1
            log(f"[SERVIDOR] Total de mensagens recebidas: {total_mensagens}")

            # 6. Devolver a mensagem ao cliente (eco)
            resposta = mensagem.upper()  # Exemplo de processamento: converter para maiúsculas
            conn.sendall(resposta.encode("utf-8"))
            log(f"[SERVIDOR] Eco enviado: '{resposta}'")

        # 7. Encerrar a conexão com este cliente
        conn.close()
        log(f"[SERVIDOR] Conexão com {endereco_cliente} encerrada.")


if __name__ == "__main__":
    iniciar_servidor()
