def main():
    nome = "Victor Augusto Malaquias Hoffman"  
    matricula = "198462"  

    numero = int(input("Digite um número até o qual você deseja contar: "))

    for i in range(1, numero + 1):
        print(i)

    print(f"\nNome: {nome}, Matrícula: {matricula}")

if __name__ == "__main__":
    main()

