import platform
import subprocess

import factorio

#use Popen.communicate to start a new factorio process and keep it
#monitored by Python

#send info to stdin from the neural net
#recieve screen output as information and send it to the neural net
#keep fitness updated and fed to the neural net

fitness = 0 #maxmize this

#open factorio
#result = subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/factorio.app"])

os = platform.system()
print(os)

MOD_DIR = ''
FACTORIO_DIR = ''

if(os == 'Darwin'):
    #result = subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "../factorio/factorio.app"])
    factorio.load_factorio()
    #copy the mod to the factorio mods folder
    MOD_DIR = '~/Library/Application Support/factorio'
    FACTORIO_DIR = '/Users/benflanders/Documents/github/FactorioAI/factorio'

elif(os == 'Linux'):
    result = subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "../factorio/factorio.app"])

factorio.load_factorio(path=FACTORIO_DIR, mod_path=MOD_DIR)