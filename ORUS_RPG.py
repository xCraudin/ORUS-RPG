import random
import time

print("╔══════════════════════════════════════════════════════════════════╗")
print("║                 SEJA BEM-VINDO AO MUNDO DE ORUS!                 ║")
print("║ Aqui você encontrará uma aventura muito imersante e desafiadora! ║")
print("╚══════════════════════════════════════════════════════════════════╝\n\n")

score = 0
genero = input("Digite o seu gênero ->(m ou f) : ")

if genero == 'm' or genero == 'M' or genero == 'f' or genero == 'F' :
    nome = input("Digite o nome do seu personagem: ")
    time.sleep(0.8)
    print("\nÓtimo, continuaremos com a criação da ficha de", nome,"\n\n" "Neste mundo você tera 3 opções de guardiões, eles definirão a dificulade do jogo, então escolha com sabedoria!")
    time.sleep(1.6)
    divindade = input(('''
╔══════════════════════════════════════════╗
║[1] - Deus da Ordem (Dificuldade: Fácil)  ║
║[2] - Deus da Justiça (Dificuldade: Média)║
║[3] - Deus do Caos (Dificuldade: Difícil) ║
╚══════════════════════════════════════════╝
  \nDigite sua escolha: '''))
    print("")
    time.sleep(0.8)
    print("Muito bem, agora vamos para a classe!\n")
    time.sleep(1)
    classe = input("[1] - Paladino\nDigite sua escolha: ")
    time.sleep(0.8)
    print("\nAgora estamos prontos! Vamos para a história! Que a sorte esteja com você!\n")
    print(nome,"se encontra na Catedral da Capital do Reino humano, na sua frente está o Sumo Sacerdote\n")
    time.sleep(0.8)
    print("Ele vira em sua direção e diz...")
    print("\n(Sumo Sarcedote) -Bravo servo de nossa Igreja!, tenho uma missão a vós, Preciso que faças uma peregrinação para vossa graça.\n")
    mapa = input("[1] - País dos demônios\nEscolha o país destino: ")
    if mapa == '1' and classe == '1':
        print("\n(Sumo Sarcedote) -Fez uma escolha perigosa nobre paladino..\n Receberas tua missão quando chegar na fronteira do País dos Demônios.\n Tenha discrição e se mantenha em sigilo!")
        time.sleep(3)
        print("\nEssas foram as últimas palavras do Sumo Sacerdote para",nome,", então começaremos sua Aventura!\n",nome,"sai da catedral e segue seu destino depois de terminar os preparativos para as Estradas.\n")
        print(nome,"avista dois caminhos na estrada e escolhe a ...")
        time.sleep(1)
        estrada = input("[1] - estrada do rei (estrada mais movimentada e segura)\n[2] - estrada rural (menos popular e mais perigosa)\nEstrada da sua escolha: ")
        if estrada == '1':
            time.sleep(0.8)
            print("\nEstrada segura e movimentada, com isso vamos para o seu dilema:\nAlguns minutos depois..\nUma carroça se encontra na encosta da estrada com a roda quebrada, O que você faz?")
            time.sleep(2)
            escolha=input("\n[1] - ajudar no conserto (+Fama)\n[2] - Ignorar (neutro)\nSeu escolha: ")
            if escolha == '1':
                score = score -2
                dado = int(random.randrange(1,21))
                print("Seu dado foi:", dado, "")
                if dado == 20:
                    time.sleep(0.8)
                    print("\nSeu conserto foi perfeito, os comerciantes ficaram muito agredecidos\ne vão propagar o teu nome por todos os 4 cantos do mundo por sua gentileza")
                    score = score + 5
                elif dado <=19 and dado >= 16:
                    time.sleep(0.8)
                    print("\nSeu conserto foi muito bom, porém houve pequenas falhas.\nOs comerciantes ficaram sastifeitos e vão lembrar do teu nome por um bom tempo")
                    score = score + 3
                elif dado >= 8 and dado <= 15:
                    time.sleep(0.8)
                    print("\nSeu conserto foi mediocre e os comerciantes fizeram o trabalho junto com você,\neles te agradecem mas não vão se lembrar do Paladino nos proximos 3 dias")
                    score = score + 1
                elif dado >= 2 and dado <= 7:
                    time.sleep(0.8)
                    print("\nVocê tentou ajudar mas só atrasou os comerciantes,\neles ficaram bravos com",nome,"e o mandam embora!")
                    score = score -1
                else :
                    time.sleep(0.8)
                    print("\nEm vez de você ajudar, acabou quebrando mais a carroça.\nOs comerciantes fizeram o Paladino picar a mula com as espadas empunhadas pela raiva!")
                    score = score -4
       
            if  escolha == '2'  :
                score = score -2
                print(nome,"ignorou os comerciantes e seguiu seu caminho até os reinos dos Demônios")
        elif estrada =='2' :
            print("\nEstrada perigosa e com pouca movimentação")
            score = score +2
            time.sleep(1.6)
            print("\nAo chegar na metade do caminho do Reino dos Demônios",nome,"se depara com uma situação normal numa estrada não vigiada\n")
            print("Uma Família Aldeã está sendo assaltada por um Bandido!, o que",nome,"vai fazer?\n[1] - Combater o bandido\n[2] - Fugir em uma disparada para o portão do Reino dos Demônios")
            time.sleep(1.6)
            assalto = input("\nQual é sua escolha: ")
            if assalto == '1':
                dado = int(random.randrange(1,21))
                print("Seu dado foi:", dado, "\n")
                if divindade == '1':
                    dado = dado +3
                elif divindade == '2':
                    dado = dado +1
                elif divindade == '3':
                    dado= dado -1
                else:
                    print("Erro de digitação, preste atenção na proxima!")
                    exit()
                print("Seu dado depois do bonificador: ", dado)
                if dado >= 20:
                    time.sleep(0.8)
                    print("\nVocê faz uma luta épica contra o bandido! fixando essa imagem na memória da familía,\nque depois falarão para todos sobre o seu feito pelo resto de suas vidas")
                    score = score + 9
                elif dado <=19 and dado >= 16:
                    time.sleep(0.8)
                    print("\nVocê vence, sem ferimentos, foi uma luta longa..., você sai cansado da batalha fazendo impacto na mente da família, com eles ficando muito agradecidos\ne irão comentar por esse feito por um bom tempo")
                    score = score + 5
                elif dado >= 8 and dado <= 15:
                    time.sleep(0.8)
                    print("\nVocê ganha o combate incapacitando o bandido mas você sai levemente ferido")
                    score = score + 3
                elif dado >= 2 and dado <= 7:
                    time.sleep(0.8)
                    print("\n",nome,"sai gravemente ferido mas mata o bandido e em agradecimento a humilde familía o leva para casa deles e o curam.\nO paladino espera estar 100% para voltar a estrada")
                    score = score +1
                else :
                    time.sleep(0.8)
                    print("\nVocê Morreu")
                    score = score -100
                    print("Seu resultado ao final da história foi:",score)
                    exit()
        print(nome,"chegou ao Reino dos Demônios e lhe é oferecido dois caminhos de entrada")
        time.sleep(2)
        portao = input("[1] - Portão principal do Reino\n[2] - Portão auxiliar\nSua escolha: ")
        if portao == '1':
            score = score -2
            print("Os guardas te revistam e lhe perguntam qual é seu objetivo entrando no reino dos Demônios\n")
            fala = input("[1] - Estou a Turismo nas férias de serviço da igreja\n[2] - Apenas Por peregrinação\n[3] - Para investigar uma história do ducado atual\nSua escolha: ")
            if fala =='1':
                score = score -1
                print("O guarda desconfia de você mas te deixa entrar e coloca um olheiro atrás de você\n",nome,"se dirige para a praça principal da cidade fronteriça")
                time.sleep(2)
            elif fala == '2':
                score = score +1
                print("O guarda recebe bem a sua fala e abre o portão do reino para você lhe desejando boa sorte na peregrinação\n",nome,"se dirige para a praça principal da cidade fronteriça")
                time.sleep(2)          
            elif fala == '3':
                score = score -3
                print("O guarda abre com receio o portão do reino e coloca 2 guardas para segui-lo escondidos durante sua permanencia no local\n",nome,"se dirige para a praça principal da cidade fronteriça")
                time.sleep(2)
            else :
                print("Escolha inválida, preste atenção na próxima")
                exit()
        elif portao == '2':
            score = score + 2
            print("O paladino se depera com um guarda roncando depois do almoço\ne entra no reino sem que ninguém saiba de sua presença\n",nome,"se dirige para a praça principal da cidade fronteriça")
        else:
            print("Escolha inválida, preste atenção na próxima")
            exit()
        print("Ao chegar na praça o paladino senta-se próximo da fonte e um homem com uma capa com capuz lhe entraga um bilhete\n")
        time.sleep(1)
        print(nome,'abre o bilhete e lá estava a mensagem... "RESGATE A PRINCESA DAS GARRAS DO REI DEMÕNIO"\n')
        time.sleep(1)
        print('O homem encapuzado sussura ao seu lado "Boa sorte" e lhe dá as costas e desaparece entre a multidão')
        time.sleep(1)
        print("O paladino se levanta e vai em direção à Capital do Reino,\n",nome,"vai em uma marcha rápida....................\n")
        time.sleep(1)
        print("Adentrando a capital qual caminho ",nome,"escolheu até o castelo?\n")
        time.sleep(1)
        caminho = input("[1] - Avenida principal\n[2] - Vielas da periferia\nSua escolha: ")
        if caminho == '1':
            print("")
            print(nome,"escolheu a Avenida Principal e todos ali reconheceram você como estrangeiro e\nse perguntavam o porquê de um Servo da Igreja estar vagando por ali.\nChegando nas portas do castelo...")
            score = score -3
            time.sleep(2)
            invasao = input("O paladino, ao ver que foi descoberto por ter chamado atenção demais naquela avenida,\npartiu em frente ao portão principal do lorde demônio e lhe vem na mente uma ideia\n\n[1] - Lutar com os guardas do portão e entrar a força no Castelo\n[2] - Fugir do local e tentar uma nova empreitada no dia seguinte pelas vielas\nQual sua escolha: ")
            if invasao == '1':
                score = score - 1
                dado = int(random.randrange(1,21))
                print("")
                print("Seu dado foi:", dado)
                if divindade == '1':
                    dado = dado +3
                elif divindade == '2':
                    dado = dado +1
                elif divindade == '3':
                    dado= dado -1
                else:
                    dado = dado
                print("Seu dado após o bonificador:", dado)
                if dado >= 20:
                    time.sleep(0.8)
                    print("\nVocê mata os guardas com eximia destreza antes que qualquer alarme fosse disparado")
                    score = score + 15
                    print("O Paladino anda com glória em direção ao castelo e segue indo para o Hall de entrada do castelo que dava passagem para a sala do trono\ne quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa! e espero que não tenha derramamento de sangue desnecessário aqui Demônio!\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa...\n O Rei Demônio Respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria-a pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro!, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente em sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\n[3] - Você puxa a garrafa de rum e chama o Rei demônio pro x1 de shots\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Sua confiança te ajuda nesse momento e a luta será definida em um golpe,\no seu dado será bonificado por sua luta anterior")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +5
                            elif divindade == '2':
                                    paladino = paladino +3
                            elif divindade == '3':
                                    paladino = paladino +1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -4
                            elif divindade == '2':
                                    demonio = demonio - 2
                            elif divindade == '3':
                                    demonio = demonio
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói!,\nmesmo ferido você mostrou do que é feito e fez o Rei Demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente,\ndando um final dramático para nossa história\nR.i.p bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, o nome do Herói não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                        if postura == '3':
                            print("Você chamou o Rei demônio pra um x1 de shots de Rum")
                            paladino = int(random.randrange(1,11))
                            demonio = int(random.randrange(1,11))
                            print("O Rei demônio deu: ",demonio," shots")
                            print("O Paladino deu: ",paladino," shots")
                            if paladino > demonio:
                                print("Mostra a sua soberania humana em cachaças perante o demônio e o humilha deixando o mesmo vivo.\nLevando a princesa com a qual se casa para o Reino Humano")
                                score = score + 80
                            elif paladino == demonio:
                                    print("O duelo lendário termina em empate o Rei demônio se sente humilhado por ter empatado com um mero humano ele se torna um vassalo do Reino Humano,\nvocê retorna com a princesa a qual você protegerá para sempre como seu guarda pessoal")
                                    score = score + 120
                            else :
                                print("Você perde para o Rei Demônio na batalha de shots e o mesmo o toma como escravo. A princesa é forçada a casar com o Rei Demônio e os reinos entram em guerra pela eternidade")
                                score = score - 15
                elif dado <=19 and dado >= 16:
                    time.sleep(0.8)
                    print("\nVocê mata os guardas com destreza mas o alarme foi tocado")
                    score = score + 7
                    print("Após o alarme ser disparado o Paladino corre em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa.\nO Demônio Respira fundo e olha nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\n[3] - Você puxa a garrafa de rum e chama o Rei demônio pro x1 de shots\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Seu status não te atrapalham nem te ajudam nesse momento e a luta será definida em um golpe definido pelo dado")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +3
                            elif divindade == '2':
                                    paladino = paladino +1
                            elif divindade == '3':
                                    paladino = paladino -1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -2
                            elif divindade == '2':
                                    demonio = demonio
                            elif divindade == '3':
                                    demonio = demonio +2
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                        if postura == '3':
                            print("Você chamou o Rei demônio pra um x1 de shots de Rum")
                            paladino = int(random.randrange(1,11))
                            demonio = int(random.randrange(1,11))
                            print("O Rei demônio deu: ",demonio," shots")
                            print("O Paladino deu: ",paladino," shots")
                            if paladino > demonio:
                                print("Mostra a sua soberania humana em cachaças perante o demônio e o humilha deixando o mesmo vivo.\nLevando a princesa com a qual se casa para o Reino Humano")
                                score = score + 80
                            elif paladino == demonio:
                                    print("O duelo lendário termina em empate o Rei demônio se sente humilhado por ter empatado com um mero humano ele se torna um vassalo do Reino Humano, você retorna com a princesa a qual você protegerá para sempre como seu guarda pessoal")
                                    score = score + 120
                            else :
                                print("Você perde para o Rei Demônio na batalha de shots e o mesmo o toma como escravo. A princesa é forçada a casar com o Rei Demônio e os reinos entram em guerra pela eternidade")
                                score = score - 15
                elif dado >= 8 and dado <= 15:
                    time.sleep(0.8)
                    print("\nMata os guardas mas foi ferido na batalha e com isso sua aventura terá uma maior dificultade daqui pra frente")
                    score = score -1
                    print("Após o alarme ser disparado o Paladino corre em direção ao castelo indo para o Hall de entrada do castelo que\ndava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa! Espero que não tenha derramamento de sangue desnecessário Demônio!\n(Rei Demônio) -MUITA AUDÁCIA SUA SEU PROJETO DE CAVALEIRO!, mas me responda uma coisa...\nO Demônio respira fundo e olha nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captura-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\n[3] - Você puxa a garrafa de rum e chama o Rei demônio pro x1 de shots\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +1
                            elif divindade == '2':
                                    paladino = paladino -1
                            elif divindade == '3':
                                    paladino = paladino -3
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -2
                            elif divindade == '2':
                                    demonio = demonio
                            elif divindade == '3':
                                    demonio = demonio +2
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                        if postura == '3':
                            print("")
                            print("Você chamou o Rei demônio pra um x1 de shots de Rum")
                            paladino = int(random.randrange(1,11))
                            demonio = int(random.randrange(1,11))
                            print("\nO Rei demônio deu: ",demonio," shots")
                            print("\nO Paladino deu: ",paladino," shots")
                            if paladino > demonio:
                                print("Mostra a sua soberania Humana em cachaças perante ao Demônio e o humilha deixando o mesmo vivo.\nLevando a princesa para o Reino Humano e casando-se!")
                                score = score + 80
                            elif paladino == demonio:
                                    print("O duelo lendário termina em empate e o Rei Demônio se sente humilhado por ter empatado com um mero humano, ele se torna um vassalo do Reino Humano,\nja você retorna com a princesa a qual você protegerá para sempre como seu guarda pessoal")
                                    score = score + 120
                            else :
                                print("Você perde para o Rei Demônio na batalha de shots e o mesmo o toma como escravo. A princesa é forçada a casar com o Rei Demônio e os reinos entram em guerra pela eternidade")
                                score = score - 15
                else :         
                    time.sleep(0.8)
                    print("\nVocê Morreu")
                    score = score -100
                    print("Seu resultado ao final da história foi:",score)
                    exit()
            elif invasao =='2':
                score = score + 3
                print("\nEscolheu as vielas e chegou a porta dos fundos do castelo e começa a observar o muro e os arredores")
                dado = int(random.randrange(1,21))
                print("Seu dado de percepção foi: ",dado)
                if dado >= 15:
                    score = score +5
                    print("Você encontrou a passagem secreta nos fundos do castelo! Tu és um sortudo!\n")
                    print("O Paladino anda com glória pelo Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa.\nO Demônio Respira fundo e olha nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                            print("Você pega um caminho subterrâneo e vai direto para a sala do trono assustando o Rei Demônio que estava bajulando a princesa\n")
                            print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                            postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                            if postura == '1' or postura == '2':
                                print("Sua chegada assusta o Rei Demônio que não consegue se concentrar na batalha e será penalizado em seus dados")
                                paladino = int(random.randrange(1,21))
                                if divindade == '1':
                                        paladino = paladino +3
                                elif divindade == '2':
                                        paladino = paladino +1
                                elif divindade == '3':
                                        paladino = paladino -1
                                else:
                                        print("Escolha inválida")
                                demonio = int(random.randrange(1,21))
                                if divindade == '1':
                                        demonio = demonio -4
                                elif divindade == '2':
                                        demonio = demonio -2
                                elif divindade == '3':
                                        demonio = demonio +1
                                else:
                                    print("Escolha inválida")
                                print("Dado do Rei Demônio: ", demonio)
                                print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                    else:
                        print("Você começa a escalar e conforme sobe fica mais confiante, e quando estava quase alcançando o topo escorrega no pé de apoio e acaba caindo de cabeça no chão acabando ali a nobre aventura do Paladino \n:(   RIP...")
                        score = score - 100
                        print("Seu resultado ao final da história foi: ",score)
                        exit()
                                    
                else:
                    print("Você se depara com um muro alto do castelo e tenta a escalada nas pedras com anuancias, vamos ver como foi tua proeficiencia *_*")
                    if dado == 14:
                        print("Subiu como se tivesse nascido para aquele momento\n")
                        print("O Paladino anda com glória em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e\nquando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                        print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa...\nO Rei Demônio respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                        resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                        if resposta == '1' or resposta == '3' or resposta == '2':
                            print("(Rei Demônio) -Então vamos lutar projeto de guerreiro!, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                            postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                            if postura == '1' or postura == '2':
                                print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior")
                                paladino = int(random.randrange(1,21))
                                if divindade == '1':
                                        paladino = paladino +3
                                elif divindade == '2':
                                        paladino = paladino +1
                                elif divindade == '3':
                                        paladino = paladino -1
                                else:
                                        print("Escolha inválida")
                                demonio = int(random.randrange(1,21))
                                if divindade == '1':
                                        demonio = demonio -2
                                elif divindade == '2':
                                        demonio = demonio
                                elif divindade == '3':
                                        demonio = demonio +2
                                else:
                                    print("Escolha inválida")
                                print("Dado do Rei Demônio: ", demonio)
                                print("\nDado do Paladino: ", paladino)
                                if paladino > demonio:
                                    print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                    score = score + 80
                                elif paladino == demonio:
                                        print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                        score = score + 40 
                                else :
                                    print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                    score = score + 10
                    elif dado >=8 and dado <= 13:
                        print("Subiu com dificuldade e para um pouco no topo muralha para respirar fundo e recuperar o folêgo\n")
                        print("O Paladino anda em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                        print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa \nO Rei Demônio respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                        resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\nQual a sua resposta: ")

                        if resposta == '1' or resposta == '3' or resposta == '2':
                            print("(Rei Demônio) - Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                            postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n1 - Fica em posição de batalha com a espada em mãos\n2 - Corre em direção ao rei demônio\n3 - Você puxa a garrafa de rum e chama o Rei demônio pro x1 de shots\nQual sua escolha? ")
                            if postura == '1' or postura == '2':
                                print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior")
                                paladino = int(random.randrange(1,21))
                                if divindade == '1':
                                        paladino = paladino +3
                                elif divindade == '2':
                                        paladino = paladino +1
                                elif divindade == '3':
                                        paladino = paladino -1
                                else:
                                        print("Escolha inválida")
                                demonio = int(random.randrange(1,21))
                                if divindade == '1':
                                        demonio = demonio -2
                                elif divindade == '2':
                                        demonio = demonio
                                elif divindade == '3':
                                        demonio = demonio +2
                                else:
                                    print("Escolha inválida")
                                print("Dado do Rei Demônio: ", demonio)
                                print("\nDado do Paladino: ", paladino)
                                if paladino > demonio:
                                    print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                    score = score + 80
                                elif paladino == demonio:
                                        print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                        score = score + 40 
                                else :
                                    print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                    score = score + 10
                        if postura == '3':
                            print("Você chamou o Rei demônio pra um x1 de shots de Rum")
                            paladino = int(random.randrange(1,11))
                            demonio = int(random.randrange(1,11))
                            print("O Rei demônio deu: ",demonio," shots")
                            print("O Paladino deu: ",paladino," shots")
                            if paladino > demonio:
                                print("Mostra a sua soberania humana em cachaças perante o demônio e o humilha deixando o mesmo vivo.\nLevando a princesa com a qual se casa para o Reino Humano")
                                score = score + 80
                            elif paladino == demonio:
                                    print("O duelo lendário termina em empate o Rei demônio se sente humilhado por ter empatado com um mero humano ele se torna um vassalo do Reino Humano, você retorna com a princesa a qual você protegerá para sempre como seu guarda pessoal")
                                    score = score + 120
                            else :
                                print("Você perde para o Rei Demônio na batalha de shots e o mesmo o toma como escravo. A princesa é forçada a casar com o Rei Demônio e os reinos entram em guerra pela eternidade")
                                score = score - 15
                    elif dado >= 5 and dado <=7:
                        print("Depois de ter subido 2 metros no muro você escorregou e caiu de bunda no chão e depois de passar vergonha o Paladino se levanta e escala o muro nervoso e com êxito dessa vez\n")
                        print("O Paladino anda com vergonha em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                        print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa...\nO Rei Demônio Respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                        resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                        if resposta == '1' or resposta == '3' or resposta == '2':
                            print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                            postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                            if postura == '1' or postura == '2':
                                print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior\n")
                                paladino = int(random.randrange(1,21))
                                if divindade == '1':
                                        paladino = paladino +3
                                elif divindade == '2':
                                        paladino = paladino +1
                                elif divindade == '3':
                                        paladino = paladino -1
                                else:
                                        print("Escolha inválida")
                                demonio = int(random.randrange(1,21))
                                if divindade == '1':
                                        demonio = demonio -2
                                elif divindade == '2':
                                        demonio = demonio
                                elif divindade == '3':
                                        demonio = demonio +2
                                else:
                                    print("Escolha inválida")
                                print("Dado do Rei Demônio: ", demonio)
                                print("\nDado do Paladino: ", paladino)
                                if paladino > demonio:
                                    print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                    score = score + 80
                                elif paladino == demonio:
                                        print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                        score = score + 40 
                                else :
                                    print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                    score = score + 10
                    else:
                        print("Você começa a escalar e conforme sobe fica mais confiante, e quando estava quase alcançando o topo escorrega no pé de apoio e acaba caindo de cabeça no chão acabando ali a nobre aventura do Paladino \n:(   RIP...")
                        score = score - 100
                        print("Seu resultado ao final da história foi: ",score)
                        exit()
        elif caminho == '2':
            score = score + 3
            print("\nEscolheu as vielas e chegou a porta dos fundos do castelo e começa a observar o muro e os arredores")
            dado = int(random.randrange(1,21))
            print("Seu dado de percepção foi: ",dado)
            if dado >= 15:
                score = score +5
                print("Você encontrou a passagem secreta nos fundos do castelo! Tu és um sortudo!\n")
                print("O Paladino anda com glória pelo Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa.\nO Demônio Respira fundo e olha nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                if resposta == '1' or resposta == '3' or resposta == '2':
                        print("Você pega um caminho subterrâneo e vai direto para a sala do trono assustando o Rei Demônio que estava bajulando a princesa\n")
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Sua chegada assusta o Rei Demônio que não consegue se concentrar na batalha e será penalizado em seus dados")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +3
                            elif divindade == '2':
                                    paladino = paladino +1
                            elif divindade == '3':
                                    paladino = paladino -1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -4
                            elif divindade == '2':
                                    demonio = demonio -2
                            elif divindade == '3':
                                    demonio = demonio +1
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                else:
                    print("Você começa a escalar e conforme sobe fica mais confiante, e quando estava quase alcançando o topo escorrega no pé de apoio e acaba caindo de cabeça no chão acabando ali a nobre aventura do Paladino \n:(   RIP...")
                    score = score - 100
                    print("Seu resultado ao final da história foi: ",score)
                    exit()
                                
            else:
                print("Você se depara com um muro alto do castelo e tenta a escalada nas pedras com anuancias, vamos ver como foi tua proeficiencia *_*")
                if dado == 14:
                    print("Subiu como se tivesse nascido para aquele momento\n")
                    print("O Paladino anda com glória em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e\nquando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa...\nO Rei Demônio respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro!, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +3
                            elif divindade == '2':
                                    paladino = paladino +1
                            elif divindade == '3':
                                    paladino = paladino -1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -2
                            elif divindade == '2':
                                    demonio = demonio
                            elif divindade == '3':
                                    demonio = demonio +2
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                elif dado >=8 and dado <= 13:
                    print("Subiu com dificuldade e para um pouco no topo muralha para respirar fundo e recuperar o folêgo\n")
                    print("O Paladino anda em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa.\nO Rei Demônio respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\nQual a sua resposta: ")

                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) - Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n1 - Fica em posição de batalha com a espada em mãos\n2 - Corre em direção ao rei demônio\n3 - Você puxa a garrafa de rum e chama o Rei demônio pro x1 de shots\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +3
                            elif divindade == '2':
                                    paladino = paladino +1
                            elif divindade == '3':
                                    paladino = paladino -1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -2
                            elif divindade == '2':
                                    demonio = demonio
                            elif divindade == '3':
                                    demonio = demonio +2
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                elif dado >= 5 and dado <=7:
                    print("Depois de ter subido 2 metros no muro você escorregou e caiu de bunda no chão e depois de passar vergonha o Paladino se levanta e escala o muro nervoso e com êxito dessa vez\n")
                    print("O Paladino anda com vergonha em direção ao castelo indo para o Hall de entrada do castelo que dava passagem para a sala do trono e quando abre essa porta lá estava a princesa ao lado do Rei Demônio\n\n")
                    print("(Rei Demônio) -Olá nobre paladino, o que o traz nessa tarde de Domingo?\n(Paladino) -Me devolva a princesa espero que não tenha derramamento de sangue desnecessário Demônio\n(Rei Demônio) -Muita audácia sua projeto de cavaleiro, me responda uma coisa...\n O Rei Demônio Respira fundo e olho nos olhos do paladino com desprezo\n(Rei Demônio) -Depois de todo o esforço que tive para captua-la. Por que a devolveria pra você de mão beijada?")
                    resposta = input("[1] - Porque você é sábio e gosta de viver\n[2] - Porque isso vai causar uma guerra entre os reinos\n[3] - Porque isso é o certo a se fazer\nQual a sua resposta: ")
                    if resposta == '1' or resposta == '3' or resposta == '2':
                        print("(Rei Demônio) -Então vamos lutar projeto de guerreiro, me cansei de VOCÊ!\n\nO Rei se levanta do seu trono e pega sua espada e caminha lentamente na sua direção")
                        postura=input("\nRESPOSTA RÁPIDA O QUE VOCÊ FAZ?\n[1] - Fica em posição de batalha com a espada em mãos\n[2] - Corre em direção ao rei demônio\nQual sua escolha? ")
                        if postura == '1' or postura == '2':
                            print("Seus ferimentos te atrapalham nesse momento e a luta será definida em um golpe seu dado será penalizado por sua luta anterior\n")
                            paladino = int(random.randrange(1,21))
                            if divindade == '1':
                                    paladino = paladino +3
                            elif divindade == '2':
                                    paladino = paladino +1
                            elif divindade == '3':
                                    paladino = paladino -1
                            else:
                                    print("Escolha inválida")
                            demonio = int(random.randrange(1,21))
                            if divindade == '1':
                                    demonio = demonio -2
                            elif divindade == '2':
                                    demonio = demonio
                            elif divindade == '3':
                                    demonio = demonio +2
                            else:
                                print("Escolha inválida")
                            print("Dado do Rei Demônio: ", demonio)
                            print("\nDado do Paladino: ", paladino)
                            if paladino > demonio:
                                print("O paladino mata o Rei demônio numa batalha épica e longa de apenas um golpe. Parabéns bravo herói, mesmo ferido você mostrou do que é feito e fez o rei demônio ser chacota pelo resto dos séculos.\n",nome,"se casa com a princesa e após a morte de seu sogro vira Rei do reino humano e será lembrado para sempre")
                                score = score + 80
                            elif paladino == demonio:
                                    print("Ocorreu um empate na batalha épica do paladino contra o rei demônio, cada um crava sua espada no coração do oponente, dando um final dramático para nossa história\nRip bravo herói que será lembrado para sempre nos séculos que virão")
                                    score = score + 40 
                            else :
                                print("No fim da batalha épica o rei demônio prevaleceu, seu nome não será lembrado, a princesa é forçada a casar-se com o rei demônio e os dois reinos travarão uma guerra sangrenta que nunca terá desfexo claro")
                                score = score + 10
                else:
                    print("Você começa a escalar e conforme sobe fica mais confiante, e quando estava quase alcançando o topo escorrega no pé de apoio e acaba caindo de cabeça no chão acabando ali a nobre aventura do Paladino \n:(   RIP...")
                    score = score - 100
                    print("Seu resultado ao final da história foi: ",score)
                    exit()
    else:
        print("Escolha inválida, mais atenção na próxima!")
        exit()
else:
    print("Gênero Inválido")
    exit()


 
print("O resultado final foi: ",score)
#Deusa da Ordem (Facil)
if score <= 0 and divindade == '1':
    print("Você fracassou em sua Missão, a Deusa da Ordem esta decepcionada com você, seu fracassado!")
if score > 0 and score < 50 and divindade== '1':
    print("Você pelo menos tentou, mas faça melhor na proxima reencarnação, a Deusa da Ordem confia em ti!")
if score >= 50 and score < 100 and divindade== '1':
    print("Você lutou bravamente meu grande Paladino, Não desistas na proxima reencarnação, a Deusa da Ordem ficou contente com seus resultados. ")
if score >= 100 and divindade== '1':
    print("Oh!, meu grande paladino...Por tamanha coragem, astusia e grandiosidade...\nVocê herdara este reino ao lado da sua princesa resgatada\nSua Deusa da Ordem agradece por tamanha lealdade, que a paz estejas entre vós para sempre! ")

#Deusa da Justiça (Média)
if score <= 0 and divindade== '2':
    print("Você fracassou em sua Missão, a Deusa da Justiça esta decepcionada com você, seu fracassado!")
if score > 0 and score < 50 and divindade== '2':
    print("Você pelo menos tentou, mas faça melhor na proxima reencarnação, a Deusa da Justiça confia em ti!")
if score >= 50 and score < 100 and divindade== '2':
    print("Você lutou bravamente meu grande Paladino, Não desistas na proxima reencarnação, a Deusa da Justiça ficou contente com seus resultados. ")
if score >= 100 and divindade== '2':
    print("Oh!, meu grande paladino...Por tamanha coragem, astusia e grandiosidade...\nVocê herdara este reino ao lado da sua princesa resgatada\nSua Deusa da Justiça agradece por tamanha lealdade, que a paz estejas entre vós para sempre! ")

#Deusa do Caos (Dificil)
if score <= 0 and divindade== '3':
    print("Você fracassou em sua Missão, a Deusa do Caos esta decepcionada com você, seu fracassado!")
if score > 0 and score < 50 and divindade== '3':
    print("Você pelo menos tentou, mas faça melhor na proxima reencarnação, a Deusa do Caos confia em ti!")
if score >= 50 and score < 100 and divindade== '3':
    print("Você lutou bravamente meu grande Paladino, Não desistas na proxima reencarnação, a Deusa do Caos ficou contente com seus resultados. ")
if score >= 100 and divindade== '3':
    print("Oh!, meu grande paladino...Por tamanha coragem, astusia e grandiosidade...\nVocê herdara este reino ao lado da sua princesa resgatada\nSua Deusa do Caos agradece por tamanha lealdade, que a paz estejas entre vós para sempre! ")
    

