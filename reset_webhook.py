from bot import bot

WEBHOOK_HOST = 'uleychatgloria.eastus.cloudapp.azure.com'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
API_TOKEN = ''

if __name__ == '__main__':
    with file('api_token', 'r') as api_token_file:
        API_TOKEN = api_token_file.readline()
        api_token_file.close()

WEBHOOK_URL_PATH = "/%s/" % API_TOKEN

# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()
# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))