# Relatório — Atividade Prática: Sockets TCP

**Disciplina:** Sistemas Distribuídos
**Dupla:** Marina rosa dos santos emerim (20200417)
**Data:** 01/06/2026

---

## Nível 1 — Inspecionar o código

### 1.1 Servidor (`servidor.py`)

Descreva com suas palavras o que cada chamada abaixo faz e por que ela
é necessária:

| Chamada | O que ela faz? |
|---------|---------------|
| `socket.socket(AF_INET, SOCK_STREAM)` | | ->  cria um socket da familia Internet (AF_INET) e do tipo stream, que utiliza conexoes TCP/IP. é necessaria para permitir a comunicacao em rede entre cliente e servidor.
| `servidor_socket.bind((HOST, PORTA))` | | -> associa esse socket do servidor a uma porta e a um IP, é necessaria para definir o endereco que o servidor ficara disponivel para receber conexoes.
| `servidor_socket.listen(5)` | | -> declara que o servidor esta pronto para receber conexoes e define que o tamanho maximo da fila de conexoes de cliente é 5.
| `servidor_socket.accept()` | | -> bloqueia ate que haja um pedido de conexao, quando isso acontece aceita a nova conexao e retorna um novo socket para conversar com esse cliente.
| `conn.recv(TAMANHO_BUFFER)` | | -> recebe dados enviados pelo cliente. o tamanho do buffer define a quantidade max de bytes que sera lida de uma vez.
| `conn.sendall(resposta.encode("utf-8"))` | | -> envia resposta para o cliente. essa msg precisa ser codificada em bytes usando utf-8 antes de ser enviada.
| `conn.close()` | | -> encerra a conexao com cliente quando a comunicacao termina e fecha socket.

### 1.2 Cliente (`cliente.py`)

| Chamada | O que ela faz? |
|---------|---------------|
| `socket.socket(AF_INET, SOCK_STREAM)` | | -> cria socket TCP, que sera usado pelo cliente para se comunicar com o servidor.
| `cliente_socket.connect((HOST_SERVIDOR, PORTA_SERVIDOR))` | | -> pede uma conexao ao servidor, utlizando IP e porta definidos. se aceita, estabelece conexao, se nao, fica bloqueado ou retorna erro, 
| `cliente_socket.sendall(mensagem.encode("utf-8"))` | | -> envia msg ao servidor, antes de enviar codifica essa msg para bytes em utf-8.
| `cliente_socket.recv(TAMANHO_BUFFER)` | | -> aguarda e recebe a resposta enviada pelo servidor.

### 1.3 Rede e contêineres

Por que o cliente usa o hostname `"servidor"` em vez de `"localhost"`
para se conectar? O que aconteceria se usasse `"localhost"`?

> _Resposta:_
 
 O cliente usa hostname `"servidor"` porque no arquivo docker-compose.yml, esse é o nome do conteiner do servidor dentro da rede interna criada pelo Docker.
 Se o cliente usasse `"localhost"` ele tentaria se conectar ao proprio conteiner do cliente, e nao o do servidor. Como nao existe servidor rodando dentro do conteiner do cliente, a conexao provavelmente falharia.

---

## Nível 2 — Modificar o servidor

Descreva as mudanças que você fez no `servidor.py` para:

1. Devolver a mensagem **em maiúsculas**:

   > _O que foi alterado e por quê:_
   Alterei a linha `resposta = mensagem.upper()`, aplicando o metodo upper() na mensagem que sera enviada pelo servidor, para devolve-la com letras maiusculas.

2. Exibir no log o **contador de mensagens recebidas** acumulado:

   > _O que foi alterado e por quê:_
     Foram adicionadas essas duas linhas de codigo:
         total_mensagens += 1
         log(f"[SERVIDOR] Total de mensagens recebidas: {total_mensagens}")
     Incrementando a variavel glabal total_mensagens, que ja existia, a cada vez que uma nova msg eh recebida e imprimindo esse resultado no terminal.

Após a modificação, você precisou rodar `docker compose up --build`.
Por que o `--build` é necessário aqui?

> _Resposta:_
      Porque o codigo do servidor.py foi alterado. Como o servidor roda dentro de um conteiner Docker, é necessário reconstruir essa imagem para que a nova versao de servidor.py seja copiada para dentro do conteiner.
---

## Observações livres

Anote aqui qualquer comportamento inesperado que observaram, erros que
apareceram e como resolveram, ou dúvidas que ainda têm:

> 
       A principio tudo tranquilo.
---

## Dúvida para a próxima aula

Escreva **uma pergunta** que surgiu durante a atividade e que vocês
gostariam de ver respondida na aula seguinte:

> Porque usar sendall() ao inves de send() nesse exemplo? Ja que o metodo que vimos em aula foi send().
