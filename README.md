# tgb3

> Telegram bot para notificar preço de ações da B3 (powered by Serverless Framework and AWS Lambda).

## Schedule

A Lambda será executada de hora em hora entre 10h e 18h (UTC-3).

Obs.: horário de funcionamento da B3 (exceto 18h).

## Setup

```
$ virtualenv env --python=python3
$ source env/bin/activate
$ python3 -m pip install -r requirements.txt
```

Configurar arquivo `serverless.env.yml` como no modelo abaixo:

```yaml
CODES: ACAO1,ACAO2,ACAO3
TELEGRAM_TOKEN: 0000000000:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TELEGRAM_CHAT_ID: 1111111111
```

- `CODES` - Códigos da ação separpados por vírgula
- `TELEGRAM_TOKEN` - Token do bot do Telegram (gerado pelo BotFather)
- `TELEGRAM_CHAT_ID` - Chat ID do usuário

## Deploy

```
serverless deploy
```

## Remove

```
serverless remove
```
