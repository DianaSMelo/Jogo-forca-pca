#-*-coding utf-8 -*-

#-- Escopo de importações --
import random
import time
import turtle

#-- Escopo de variáveis globais --
score = 0 #variavel de controle dos pontos conquistados
palavra ='' #variavel que controla a palavra escolhida
jogando = True #variavel de controle do loop do jogo
x=0 #variavel que encontra o meio da janela para posicionar elementos
janela = None # variavel que permite o reset da janela atravez da função cria_janela
erro = 0# variavel de controle de erros
escolhas = []#variavel que guarda as escolhas pra conferir se não se repetem
posLetra = -350 # variável que controla o posicionamento em que as letras digitadas são mostradas
#-- Dicionário que serve de banco de dados com todas as palavras e frases do jogo
bd = {
"Dinheiro": "Precisamos trabalhar para tê-lo.",
"Empréstimo":"O banco empresta um valor  \nse formos bons pagadores.",
"crédito": " Cartão de crédito É uma forma de \nempréstimo que temos que pagar em alguns dias.",
"Parcela":"Usamos quando precisamos comprar  \nalgo que não temos todo o dimdim.",
"Juros": "Temos que pagar quando não cumprimos  \ncom o pagamento no dia certo.",
"Carência":' Quando temos que pagar a primeira parcela.',
"Mesada": 'É o dinheiro que o papai e a mamãe  \nnos dão todos os meses.',
"débito":'Cartão de débito É uma forma de   \nusarmos o dimdim sem ser em papel.',
"Economizar": 'é Não gastar o dimdim com coisas  \nque não precisamos.',
"Dívidas": 'Acontecem quando gastamos mais  \ndo que temos pra gastar.',
"Despesas": 'são os Gastos necessários.',
"Investimento": "É colocar o dimdim que guardamos  \nem algo que vai nos dar um dimdim a mais.",
"vista": "à vista é  Quando pagamos no momento da compra.",
"Boleto": "Documento que pagamos de alguma compra feita.",
"Financiamento":" É um crédito que conseguimos para  \ncomprar por exemplo, uma casa." ,
"Azul": "quando gastamos nosso dimdim menos do que  \nganhamos nosso crédito fica no azul",
}

#----Registro de imagens---#
turtle.register_shape('./imgs/forca.gif')
turtle.register_shape('./imgs/corda.gif')
turtle.register_shape('./imgs/cabeça.gif')
turtle.register_shape('./imgs/bDir.gif')
turtle.register_shape('./imgs/bEsq.gif')
turtle.register_shape('./imgs/pDir.gif')
turtle.register_shape('./imgs/pEsq.gif')
turtle.register_shape('./imgs/peito.gif')
turtle.register_shape('./imgs/barriga.gif')
#-- Escopo de objetos do jogo

'''todos os objetos do jogo serão criados
através de chamadas de funções'''

#-- Escopo de funções --
def cria_janela():
	global janela, x
 
	#desenhando janela
	janela = turtle.Screen()
	janela.setup(width = 1.0, height = 1.0, startx=None, starty=None)
	janela.title('Jogo da Forca')
	janela.bgcolor('green')
 
	x=janela.window_width()/4*(-1)-50 #inicializando a variavel x
  
	#desenhando a forca
	forca = turtle.Turtle()
	forca.shape('./imgs/forca.gif')
	forca.speed(0)
	forca.pu()
	forca.setpos(-200,75)
	
	# desenhando o score
	score_pen = turtle.Turtle()
	score_pen.speed(0)
	score_pen.ht()
	score_pen.color('white')
	score_pen.setpos(0,250)
	score_pen.clear()#sempre que a janela é redesenhada, reseta o score_pen
	score_pen.write(f'Score: {score}', font = ('Arial', 32,'normal'))
	
#---------------
'''funções que desenharão as partes do corpo e a corda
se o usuario errar a(s) letra(s)'''

def criaCabeca():
	cabeca = turtle.Turtle()
	cabeca.speed(0)
	cabeca.pu()
	cabeca.ht()
	cabeca.shape('./imgs/cabeça.gif')
	cabeca.setpos(-90,155)
	cabeca.st()
	
def criaCorda():
	corda = turtle.Turtle()
	corda.speed(0)
	corda.pu()
	corda.ht()
	corda.shape('./imgs/corda.gif')
	corda.setpos(-90,155)
	corda.st()

def cria_pEsq():
	pEsq = turtle.Turtle()
	pEsq.speed(0)
	pEsq.pu()
	pEsq.ht()
	pEsq.shape('./imgs/pEsq.gif')
	pEsq.setpos(-80,-85)
	pEsq.st()	

def cria_pDir():
	pDir = turtle.Turtle()
	pDir.speed(0)
	pDir.pu()
	pDir.ht()
	pDir.shape('./imgs/pDir.gif')
	pDir.setpos(-15,-85)
	pDir.st()

def cria_bDir():
	bDir = turtle.Turtle()
	bDir.speed(0)
	bDir.pu()
	bDir.ht()
	bDir.shape('./imgs/bDir.gif')
	bDir.setpos(-25,32)
	bDir.st()

def cria_bEsq():
	bEsq = turtle.Turtle()
	bEsq.speed(0)
	bEsq.pu()
	bEsq.ht()
	bEsq.shape('./imgs/bEsq.gif')
	bEsq.setpos(-122,40)
	bEsq.st()

def criaBarriga():
	barriga = turtle.Turtle()
	barriga.speed(0)
	barriga.pu()
	barriga.ht()
	barriga.shape('./imgs/barriga.gif')
	barriga.setpos(-65,0)
	barriga.st()

def criaPeito():
	peito = turtle.Turtle()
	peito.speed(0)
	peito.pu()
	peito.ht()
	peito.shape('./imgs/peito.gif')
	peito.setpos(-75,60)
	peito.st()

#---------
'''Funções de controle do jogo'''

def escolhePalavra():
    '''função que escolhe aleatoriamente uma palavra e uma
    frase no bd e manda para o jogo'''
    escolhido = palavra, frase = random.choice(list(bd.items())) 
    return escolhido # retorna a palavra e a frase escolhida

def trata_char_especial(p):
	'''função que trata caracteres especiais nas palavras escolhidas'''
	#especiais = ÀÂÄÁÅ Ç ÈÊÉË ÏÌÎÍ ÒÖÓÕÔ ÙÜÚÛ
	nova = '' #palavra temporaria
	
	#percorrendo a palavra escolhida e substituindo
	#os caracteres especiais por caracteres normais  
	for letra in p:
		if letra in 'ÀÂÄÁÅÃ': 
			nova+='A'
		elif letra in 'ÈÊÉË':
			nova+='E'
		elif letra in 'ÏÌÎÍ':
			nova +='I'
		elif letra in 'ÒÖÓÕÔ':
			nova+='O'
		elif letra in 'ÙÜÚÛ':
			nova+= 'U'
		elif letra == 'Ç':
			nova += 'C'
		else: 
			nova+=letra
	#retornando a palavra escolhida já tratada, sem cc especiais
	return nova
	
def trata_erro(erros):
	'''função que desenha as partes do corpo 
	segundo os erros do usuário'''
	if erros == 1:
		criaCabeca()
	elif erros == 2:
		criaPeito()
	elif erros == 3:
		criaBarriga()
	elif erros == 4:
		cria_bDir()
	elif erros == 5:
		cria_bEsq()
	elif erros == 6:
		cria_pDir()
	elif erros == 7:
		cria_pEsq()
	elif erros == 8:
		criaCorda()

#loop do jogo (main_loop)
while jogando:
	cria_janela()#inicia a janela
		
	#escolhe o par de palavra e frase
	escolhido = escolhePalavra()
	#coloca tudo em maiusculas
	palavra = escolhido[0].upper()
	frase = escolhido[1].upper()
	print(palavra , '\n', frase)
	#trata a palavra escolhida e reserva numa palavra temporaria
	palavra_t = trata_char_especial(palavra)
	
	#variavel que representa as letras. 
	palavra_escondida = '' 
	
	#desenhando a palavra escondida
	for i in range(len(palavra)):
		palavra_escondida += '-'	
	turtle.ht()
	turtle.speed(0)
	turtle.pu()
	turtle.setpos(-350,-320)
	turtle.write(palavra_escondida,font = ('Arial',100,'bold'))
	
	#loop de tentativas do jogo
	while True: 
		#obtendo a resposta do usuario 
		resposta = str(turtle.textinput('Escolha uma Letra:',''))[0].upper()
		#mostrando as letras digitadas
		if resposta: # esse if vê se foi digitado alguma coisa na caixa de entrada
			#conferindo que só uma letra foi digitada
			resposta = resposta[0]
			digitado = turtle.Turtle()
			digitado.speed(0)
			digitado.ht()
			digitado.pu()
			digitado.setpos(posLetra,-175)
			digitado.color('gray')
			digitado.write(f' {resposta}',font = ('Arial',15,'bold'))
			posLetra+=20 # incrementando a variavel para a próxima letra se deslocar

  		#se a errou:
		if resposta not in palavra_t:
			erro+=1 #aumenta a variavel de erros
			trata_erro(erro)
			#mostra a mensagem de erro
			msg_erro = turtle.Turtle()
			msg_erro.speed(0)
			msg_erro.ht()
			msg_erro.pu()
			msg_erro.setpos(200,150)
			msg_erro.color('red')
			msg_erro.write('letra errada',font = ('Arial',40,'bold') )
			time.sleep(0.5)
			msg_erro.clear()
			#se errar oito vezes perde
			if erro == 8:
				#mostra a mensagem de fim
				time.sleep(1)
				janela.clear()
				turtle.clear()
				turtle.ht()
				turtle.pu()    
				turtle.setpos(x,-250)
				turtle.write(f'Que pena!Você foi enforcado!\nA palavra era {palavra},lembrando que: \n{frase}',font = ('Arial',25,'bold'))
				time.sleep(4)
				#para o loop de tentativas
				break
		# se a letra for repetida
		if resposta in escolhas:
			erro+=1
			trata_erro(erro)
			#mostra a mensagem de erro por repetição
			msg_erro = turtle.Turtle()
			msg_erro.ht()
			msg_erro.pu()
			msg_erro.setpos(200,150)
			msg_erro.color('blue')
			msg_erro.write('Letra Repetida',font = ('Arial',40,'bold') )
			msg_erro.speed(0)
			time.sleep(0.5)
			msg_erro.clear()
			
			if erro == 8:
				#mostra a mensagem de fim
				time.sleep(1)
				janela.clear()
				turtle.clear()
				turtle.ht()
				turtle.pu()    
				turtle.setpos(x,-250)
				turtle.write(f'Que pena!Você foi enforcado!\nA palavra era {palavra},lembrando que: \n{frase}',font = ('Arial',25,'bold'))
				time.sleep(5)
				#para o loop de tentativas
				break
		# se acertou a letra
		if resposta in palavra_t:
			contador =0# variavel que controla a posição da letra certa dentro da palavra
			#percorrendo a palavra tratada
			for letra in palavra_t:
				# transformando a palavra escondida em lista
				#para facilitar a substituição
				palavra_escondida = list(palavra_escondida)
				#verificando se a resposta é a letra atual
				if letra == resposta:
					#fazendo a substituição na tela  to traço pela letra
					del(palavra_escondida[contador])
					palavra_escondida.insert(contador,palavra[contador])
					palavra_escondida = str().join(palavra_escondida)
					turtle.clear()
					turtle.write(palavra_escondida,font = ('Arial',100,'bold'))
				contador +=1 #aumentando o contador
	
		#inserindo a letra escolhida na lista de escolhas
		#para verificar se foi repetida	
		escolhas.append(resposta)
		#verificando se completou a palavra
		if '-' in palavra_escondida:
			# se não completou
			continue
		else:
			# se completou   
   			#limpa a tela
			time.sleep(1)
			janela.clear()
			score+=1# aumenta score
			
			#mostra mensagem de vitoria   
			msg_venceu = turtle.Turtle()
			msg_venceu.ht()
			msg_venceu.pu()
			msg_venceu.color('green')
			msg_venceu.speed(0)
			msg_venceu.setpos(x,-200)
			msg_venceu.write(f'Parabéns voce venceu!\nE por falar em {palavra}\nÉ bom lembrar que \n{frase}',font = ('Arial',25,'bold'))
			
			time.sleep(5)
			msg_venceu.clear()
			#para o loop de tentativas
			break

	#pergunta se quer jogar novamente
	novo_jogo = str(turtle.textinput('Jogar novamente:',' [S/N]'))
	#loop de verificação de escolha jogar novamente
	while True:
		
		if novo_jogo in 'Ss':
			#se jogar de novo
			turtle.clear()#limpa a palavra da tela
			erro=0 # zera os erros
			escolhas=[] #zera as escolhas
			janela.clear() #limpa a tela
			break # para o loop de verificação
		if novo_jogo in "Nn":
			#se não jogar de novo
			time.sleep(0.5)#pequena pausa
			janela.clear()#limpa janela
			#mostra mensagem final
			msg_final = turtle.Turtle()
			msg_final.ht()
			msg_final.pu()
			msg_final.color('gray')
			msg_final.speed(0)
			msg_final.setpos(x,-150)
			msg_final.write('Obrigado\n     por\n   jogar!',font = ('Arial',70,'bold') )
			
			time.sleep(1)#pequena pausa
			janela.bye()# fecha janela e encerra programa
		else:
			#se a opção não for nem 's' nem 'n', tenta outra vez
			novo_jogo = turtle.textinput('Jogar novamente:',' [S/N]')
				
#loop da janela		
janela.mainloop()
