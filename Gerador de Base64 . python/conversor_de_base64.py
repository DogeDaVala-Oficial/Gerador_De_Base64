'''
    criador : DogeDaVala .
    
    projeto : criador de base64 simples .
    
    compatibilidade : por enquanto apenas .mp3 .
'''
# chama a biblioteca base64
import base64

# Caminho para o seu arquivo de áudio MP3
file_path = r' coloque aqui seu path , entre as aspas '  # Substitua a marcação pelo path do seu arquivo MP3

# Abre o arquivo de áudio no modo binário
with open(file_path, 'rb') as audio_file:
    audio_data = audio_file.read()

# Codifica os dados em base64
encoded_audio = base64.b64encode(audio_data).decode('utf-8')

# Salva o base64 em um arquivo de texto
with open('audio_base64.txt', 'w') as base64_file:
    base64_file.write(encoded_audio)

# imprime a string base64 para facilitar o uso , mas e recomendado usar o text do .txt gerado .
print(encoded_audio) # printa no terminal