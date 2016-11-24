from api_token import API_TOKEN
from singletons import bot

WEBHOOK_HOST = 'uleychatgloria.eastus.cloudapp.azure.com'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate

WEBHOOK_URL_PATH = "/%s/" % API_TOKEN


def reset_webhook():
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    # Set webhook
    bot.set_webhook(webhook_url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

if __name__ == '__main__':
    reset_webhook()
