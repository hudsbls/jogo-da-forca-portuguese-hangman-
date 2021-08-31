import random
import time


# Apresentação do jogo:
print("\nOlá, vamos para um jogo clássico, quase sempre jogado só com papel e caneta.\n")
name = input("Coloque seu nome: ")
print("Oi " + name + "! Boa sorte!")
time.sleep(1)
print("O jogo já vai começar\nVamos lá!")
time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global wrong_guess

    words_to_guess = ["janeiro", "mar", "praia", "oceano", "ferias"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    wrong_guess = []
    play_game = ""

    

# Loop para reiniciar o jogo quando a partida acabar:
def play_loop():
    global play_game
    play_game = input("Quer jogar novamente? s = sim, n = não \n")
    if play_game == "s":
        main()
    elif play_game == "n":
        print("Obrigada por jogar! Volte sempre")
        exit()
    else:
        play_game

# Função com as condições e caracteristicas do jogo:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global length

    # Dicas para ajudar o usuário a chutar a letra certa:
    if word == "janeiro":
        print("a dica é: cidade maravilhosa")
    elif word == "mar":
        print("a dica é: habitat dos peixes")
    elif word == "praia":
        print("a dica é: onde crianças fazem castelos de areia")
    elif word == "oceano":
        print("a dica é: O planeta terra tem continentes e ______")
    elif word == "ferias":
        print("a dica é: período de descanso escolar ou do trabalho")
    

    limit = 5
    length = len(word)

    guess = input("Esta é a palavra da forca: " + display + " Ela tem " + str(length) + " letras. Chute uma letra: \n")
    guess = guess.strip()



    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Entrada errada, tente uma letra\n")
        hangman()  
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print("Parabéns, você acertou! " + display + "\n")
    elif guess in already_guessed:
        print("Você já colocou essa letra. Tente outra letra.\n")
 
    else:
        wrong_guess.extend([guess])
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Resposta errada. 😥 " + str(limit - count) + " chances restantes. Letras que não estão na palavra:" + str(wrong_guess) + "\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Resposta errada. 😥 Chances restantes: " + str(limit - count) + ". Letras que não estão na palavra:" + str(wrong_guess) + "\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("A letra escolhida não está na palabra. 😥 " + str(limit - count) + ". Letras que não estão na palavra:" + str(wrong_guess) + "\n")
        elif  count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Resposta errada. 😥 " + str(limit - count) + " chance restante. É agora ou agora!!! Letras que não estão na palavra:" + str(wrong_guess) + "\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Poxa, resposta errada. Você está enforcado!!!\n")
            print("A palavra é:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print("Parabéns! Você acertou a palavra!")
        play_loop()
    elif count != limit:
        hangman()

main()
hangman()