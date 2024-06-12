import os, platform

caminhoDoArquivoDeSom = 'audio/eating-sound-effect-36186.mp3'  

def tocarSFXComendo():
    if platform.system() == 'Windows':
        os.system(f"start {caminhoDoArquivoDeSom} >NUL 2>&1")
    elif platform.system() == 'Darwin':  # macOS
        os.system(f"afplay {caminhoDoArquivoDeSom} >/dev/null 2>&1")
    elif platform.system() == 'Linux':
        os.system(f"ffplay -nodisp -autoexit {caminhoDoArquivoDeSom} >/dev/null 2>&1")

# Para que o ffplay não mostre nenhuma informação no terminal durante o jogo, 
# redirecionamos a saída padrão e a saída de erro para '/dev/null' ou para 'NUL'. 