import random

def main():
    nome = "Victor Augusto Malaquias Hoffman"  
    matricula = "198462"  

    numero = random.randint(1, 20)

    for i in range(1, numero + 1):
        print(i)

    print(f"\nNome: {nome}, Matrícula: {matricula}")

if __name__ == "__main__":
    main()
