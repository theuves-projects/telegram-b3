import os
import requests

def send_message(message, token, chat_id):
  res = requests.post(
    "https://api.telegram.org/bot%s/sendMessage" % token,
    headers={
      "Content-Type": "application/json"
    },
    json={
      "text": message,
      "chat_id": chat_id,
      "parse_mode": "markdown"
    }
  )

def get_shares_value(code):
    params = {
        'region'        : 'BR',
        'lang'          : 'pt-BR',
        'includePrePost': 'false',
        'interval'      : '2m',
        'range'         : '1d',
        'corsDomain'    : 'br.financas.yahoo.com',
        '.tsrc'         : 'finance'
    }

    data = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/%s.SA' % code, params=params)
    data_json = data.json()

    return data_json['chart']['result'][0]['meta']['regularMarketPrice']

def get_message(codes):
    values = map(lambda code: '`%s` = R$ %s' % (code + '.SA', get_shares_value(code)), codes)
    message = '\n'.join(values)

    return message

def alert(event, context):
    codes = os.environ.get('CODES').split(',')

    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

    message = get_message(codes)

    send_message(message, telegram_token, telegram_chat_id)

    return {
        "statusCode": 200
    }
