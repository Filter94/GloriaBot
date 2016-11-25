API_TOKEN = '111111111:AAAAAAAAAAAAAAAAAAA'

try:
    with file('api_token', 'r') as api_token_file:
        API_TOKEN = api_token_file.readline()
        api_token_file.close()
except IOError as e:
    # test mode
    pass
