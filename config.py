import os
import ProxyCloud

BOT_TOKEN = '5900217375:AAHJPCehya6lZUfuaXM831-okA0Jms0povg' #Aqui va el token del bot
API_ID =  9902519 #Tu api id de telegram
API_HASH = '9d8097d05bbc90a6ed2a7a81abcd4e8a' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Abolanos3').split(';')

static_proxy = 'http://KJCKLHYGKEGDYDKDGKCIYEDHCFRHDELDDGLF'
PROXY = ProxyCloud.parse(static_proxy)
if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['Abolanos3'] = 0

#
#
