
import sys
import pyfiglet

def main():
    if len(sys.argv) == 1:
        font = None
        
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
        
    else:
        print("Uso: figlet.py [-f FONT] [TEXTO]")
        sys.exit(1)

    if font:
        try:
            figlet_font = pyfiglet.Figlet(font=font)
        except pyfiglet.FontNotFound:
            print(f"Fonte '{font}' não encontrada. Use uma fonte válida.")
            sys.exit(1)
            
    else:
        figlet_font = pyfiglet.Figlet()
    texto = input("Digite o texto que deseja exibir: ")

    texto_em_fonte = figlet_font.renderText(texto)
    print(texto_em_fonte)

if __name__ == "__main__":
    main()





