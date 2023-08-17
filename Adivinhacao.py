import random
print("**********************************");
print("Bem vindo ao jogo de Adivinhação!!");
print("**********************************");

#Variaveis principais
numero_secreto = random.randrange(1,101);#o numero secreto varias de 1 a 100
total_tentativas = 0;
pontos = 1000;

print("Qual o nivel de dificuldade?")
print("(1) Facil  (2)Medio  (3)Dificil")

nivel = int(input("Define o nivel: "))

if(nivel == 1):
    total_tentativas = 20;
elif(nivel == 2):
    total_tentativas = 10;
else:
    total_tentativas = 5;

#rodada = 5
#Ferramenta de repetição do jogo
#while(total_tentativas >= rodada):
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite um numero entre 1 e 100: ");
    chute = int(chute_str);
    print("Você digitou: ", chute);

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        print("   ")
        continue

    #variaveis que demonstram quando o chute foi certo,  maior  que o numero_aleatorio e quando ele é menor que o numero_aleatorio
    acertou = numero_secreto == chute;
    erro_maior = chute > numero_secreto;
    erro_menor = chute < numero_secreto;

    if (acertou):
        print("Você acertou!");
        print("  ")
        print("SUA PONTUAÇÃO É: {}".format(pontos))
        break;
    else:
        if(erro_maior):
            print("O seu chute foi maior que o número secreto.");
        elif(erro_menor):
            print("O seu chute foi menor que o número secreto.");
        pontos_perdidos = abs(numero_secreto - chute)# calculos de pontos perdidos o qual é a diferença entre o numero secreto e o chute. abs é para que o resultado do calculo senja o valor absoluto
        pontos = pontos - pontos_perdidos
    print("  ")


print("FIM DE JOGO!")