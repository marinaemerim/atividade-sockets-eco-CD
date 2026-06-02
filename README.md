# Atividade Prática: Sockets TCP — Cliente/Servidor Eco

### Pré-requisitos:
- Git instalado na máquina
- Docker com o plugin Docker Compose instalado (`docker compose version` deve funcionar)
  - Docker Desktop (Mac/Windows/Linux) já inclui o Compose automaticamente
  - Docker Engine (Linux) requer instalação separada do plugin: veja a [documentação oficial](https://docs.docker.com/compose/install/linux/)

---

## Objetivo

Ao final desta atividade você será capaz de:

1. Explicar o fluxo de uma conexão TCP: `socket → bind → listen → accept` (servidor) e `socket → connect → send/recv` (cliente).
2. Justificar por que dois processos em contêineres distintos precisam de endereço e porta para se comunicar, mesmo rodando no mesmo computador.
3. Modificar um servidor simples e reconstruir a imagem Docker para validar a mudança.

---

## Fase pré-atividade (faça antes da parte prática)

Estude **pelo menos dois** dos recursos abaixo (escolha os formatos que
funcionam melhor para você):

- **Vídeo (20 min):** [O que é um socket](https://www.youtube.com/watch?v=aV4p6f2MuJc)
- **Leitura:** [documentação oficial Python — Howto: Programação de Soquetes](https://docs.python.org/pt-br/3.14/howto/sockets.html)
- **Slides/texto curto:** [capítulo introdutório de sockets do material no Moodle.](https://presencial.moodle.ufsc.br/pluginfile.php/1900841/mod_resource/content/12/INE5418_05_sockets.pdf)

---

## Estrutura do projeto

```
atividade-sockets-eco/
├── README.md                  ← este arquivo
├── docker-compose.yml         ← orquestra servidor e cliente
├── servidor/
│   ├── Dockerfile
│   └── servidor.py            ← servidor TCP eco (leia e inspecione!)
├── cliente/
│   ├── Dockerfile
│   └── cliente.py             ← cliente TCP (leia e inspecione!)
└── relatorio-template.md      ← template do relatório a entregar
```

---

## Nível 0 — Rodar (não escreva código ainda)

```bash
# 1. Clone o repositório (ou copie a pasta)
# 2. Entre na pasta da atividade
cd atividade-sockets-eco

# 3. Suba os contêineres
docker compose up --build
```

Você deve ver uma saída parecida com:

```
servidor-1  | [SERVIDOR] Escutando em 0.0.0.0:5000 ...
servidor-1  | [SERVIDOR] Conexão estabelecida com ('172.x.x.x', XXXXX)
servidor-1  | [SERVIDOR] Mensagem #1 recebida: 'Olá, Sistemas Distribuídos!'
servidor-1  | [SERVIDOR] Eco enviado: 'Olá, Sistemas Distribuídos!'
cliente-1   | [CLIENTE] Conectando a servidor:5000 ...
cliente-1   | [CLIENTE] Conexão estabelecida.
cliente-1   | [CLIENTE] Mensagem enviada: 'Olá, Sistemas Distribuídos!'
cliente-1   | [CLIENTE] Eco recebido do servidor: 'Olá, Sistemas Distribuídos!'
```

Pressione `Ctrl+C` para parar. Depois limpe os contêineres:

```bash
docker compose down
```

**Ponto de atenção:** observe que o log do servidor e o log do cliente
podem aparecer intercalados. Os dois processos rodam em contêineres separados,
em paralelo, mas compartilham a mesma rede interna do Docker.

---

## Nível 1 — Inspecionar

Abra `servidor/servidor.py` e `cliente/cliente.py` lado a lado.

Usando o `relatorio-template.md` como guia, responda **por escrito** as
perguntas sobre cada chamada de socket. Não pule esta etapa — as respostas
são a parte conceitual central da atividade.

Dicas para discussão em dupla:

- O que acontece se o cliente tentar se conectar antes de o servidor
  estar escutando? Teste: altere o `depends_on` no `docker-compose.yml`
  para removê-lo e observe.
- Por que usamos `conn.sendall()` em vez de `conn.send()`? Veja a
  documentação de `send` no Python.

---

## Nível 2 — Modificar

Edite `servidor/servidor.py` para que o servidor:

1. **Devolva a mensagem em maiúsculas** (em vez de devolver exatamente o
   que recebeu).
2. **Exiba no log o contador acumulado** de mensagens (já existe a variável
   `total_mensagens` — use-a).

Após editar, reconstrua e suba os contêineres:

```bash
docker compose up --build
```

Verifique nos logs que o cliente recebe a mensagem em maiúsculas.

Para testar com mensagens diferentes, edite o campo `command` em
`docker-compose.yml` e suba novamente.

---

## Entregável

Faça um fork deste repositório (ou copie para um repositório Git próprio)
e submeta o link no Moodle com:

1. O código modificado (`servidor/servidor.py` com as alterações do Nível 2).
2. O arquivo `relatorio.md` preenchido a partir do `relatorio-template.md`.

**Prazo:** conforme combinado em aula.

(Obs: A forma de entrega do relatório pode variar, dependendo do combinado em aula)

---

## Dúvidas

Registre qualquer dúvida no `relatorio.md` (seção "Dúvida para a próxima
aula"). O professor usará essas dúvidas para planejar o próximo encontro.
