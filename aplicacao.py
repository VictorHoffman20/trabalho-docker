import sys

def main():
    nome = "Seu Nome"  
    matricula = "Sua Matricula" 

    if len(sys.argv) != 2:
        print("Por favor, forneça um único número como argumento.")
        return

    try:
        numero = int(sys.argv[1])
        
        for i in range(1, numero + 1):
            print(i)

        print(f"\nNome: {nome}, Matrícula: {matricula}")

    except ValueError:
        print("Por favor, insira um número inteiro válido como argumento.")

if __name__ == "__main__":
    main()
