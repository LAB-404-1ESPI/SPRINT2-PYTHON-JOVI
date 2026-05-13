cont_hist = ["Revolução Francesa", "Segunda Guerra Mundial", "Descobrimento do Brasil"]
cont_mat = ["Álgebra", "Geometria", "Porcentagem"]
cont_geo = ["Climatologia", "Globalização", "Hidrografia"]
def conteudos():

    def galeria():
        print("\n🖼️ GALERIA JOVIX")
        print("⚙️ EXEMPLO DE PASTA DE IMAGENS FEITO PELA JOVIX ⚙️")
        print("━━━━━━━━━━━━━━━━━━━━━━")

        if cont_escolhido == "Álgebra":
            print("📸 exemplo.jpg")
            print("📝 Foto da lousa com equações do 2° grau\n")
            print("")
            print("📸 exemplo.jpg")
            print("📝 Resolução de Bhaskara\n")
            print("")
            print("📸 exemplo.jpg")
            print("📝 Exercícios de álgebra")

        elif cont_escolhido == "Geometria":
            print("📸 exemplo.jpg")
            print("📝 Formas geométricas\n")
            print("📸 exemplo.jpg")
            print("📝 Área e perímetro\n")
            print("📸 exemplo.jpg")
            print("📝 Explicação sobre polígonos")

        elif cont_escolhido == "Porcentagem":
            print("📸 exemplo.jpg")
            print("📝 Conta de porcentagem\n")
            print("📸 exemplo.jpg")
            print("📝 Exercícios de desconto\n")
            print("📸 exemplo.jpg")
            print("📝 Regra de três")

        elif cont_escolhido == "Revolução Francesa":
            print("📸 exemplo.jpg")
            print("📝 Queda da Bastilha\n")
            print("📸 exemplo.jpg")
            print("📝 Revolução Francesa resumo\n")
            print("📸 exemplo.jpg")
            print("📝 Linha do tempo histórica")

        elif cont_escolhido == "Segunda Guerra Mundial":
            print("📸 exemplo.jpg")
            print("📝 Países do eixo e aliados\n")
            print("📸 exemplo.jpg")
            print("📝 Resumo Segunda Guerra\n")
            print("📸 exemplo.jpg")
            print("📝 Mapa da guerra")

        elif cont_escolhido == "Descobrimento do Brasil":
            print("📸 exemplo.jpg")
            print("📝 Chegada dos portugueses\n")
            print("📸 exemplo.jpg")
            print("📝 Pedro Álvares Cabral\n")
            print("📸 exemplo.jpg")
            print("📝 História do Brasil colonial")

        elif cont_escolhido == "Climatologia":
            print("📸 exemplo.jpg")
            print("📝 Tipos de clima\n")
            print("📸 exemplo.jpg")
            print("📝 Clima equatorial\n")
            print("📸 exemplo.jpg")
            print("📝 Fatores climáticos")

        elif cont_escolhido == "Globalização":
            print("📸 exemplo.jpg")
            print("📝 Comércio mundial\n")
            print("📸 exemplo.jpg")
            print("📝 Integração econômica\n")
            print("📸 exemplo.jpg")
            print("📝 Globalização resumo")

        elif cont_escolhido == "Hidrografia":
            print("📸 exemplo.jpg")
            print("📝 Bacias hidrográficas\n")
            print("📸 exemplo.jpg")
            print("📝 Ciclo da água\n")
            print("📸 exemplo.jpg")
            print("📝 Rios brasileiros")

        print("\n🤖 JOVIX: Imagens sincronizadas com sucesso")
        # para chamar a ia jovix tem um botão no canto superior com a imagem dela,
        # foi feito no figma tambem essa parte de design
        voltar = input("Digite 1 para voltar: ")


    while True:

        materias = ["Matemática", "História", "Geografia"]
        print(f"\n📚 Escolha uma matéria")
        print("1 - Matemática")
        print("2 - História")
        print("3 - Geografia")
        print("4 - Voltar")

        op = int(input("Escolha: "))

        if op == 1:
            materia_atual = "Matemática"
            cont = cont_mat
        elif op == 2:
            materia_atual = "História"
            cont = cont_hist
        elif op == 3:
            materia_atual = "Geografia"
            cont = cont_geo
        elif op == 4:
            break

        # conteúdos

        print(f"\n Conteúdos de {materia_atual}")
        print(f"1 - {cont[0]} ")
        print(f"2 - {cont[1]} ")
        print(f"3 - {cont[2]} ")

        op = int(input("Escolha: "))

        if op == 1:
            cont_escolhido = cont[0]
        elif op == 2:
            cont_escolhido = cont[1]
        elif op == 3:
            cont_escolhido = cont[2]
    # menu conteudos

        while True:
            print(f"\n📘 {cont_escolhido}")
            print("1 - Banco de Questões")
            print("2 - Imagens da Galeria")
            print("3 - Voltar")

            op2 = int(input("Escolha: "))
            if op2 == 2:
                # galeria de fotos

                galeria()

            elif op2 == 1:

                # matematica
                if cont_escolhido == "Álgebra":
                    print("\nQual o valor de x na equação x² = 25?")
                    print("A - 5")
                    print("B - 10")
                    print("C - 15")

                    r = input("Resposta: ").lower()

                    if r == "a" or r == "5":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é 5 ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Geometria":
                    print("\nQuantos lados possui um hexágono?")
                    print("A - 5")
                    print("B - 6")
                    print("C - 8")

                    r = input("Resposta: ").lower()

                    if r == "b" or r == "6":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é 6 ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Porcentagem":
                    print("\n25% de 200 é?")
                    print("A - 25")
                    print("B - 40")
                    print("C - 50")

                    r = input("Resposta: ").lower()

                    if r == "c" or r == "50":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é 50 ")

                    voltar = input("Digite 1 para voltar: ")

                # historia
                elif cont_escolhido == "Revolução Francesa":
                    print("\nQual era o lema da Revolução Francesa?")
                    print("A - Ordem e progresso")
                    print("B - Liberdade, igualdade e fraternidade")
                    print("C - Paz e justiça")

                    r = input("Resposta: ").lower()

                    if r == "b" or r == "liberdade igualdade e fraternidade":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é liberdade, igualdade e fraternidade ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Segunda Guerra Mundial":
                    print("\nQual país iniciou a Segunda Guerra Mundial?")
                    print("A - Alemanha")
                    print("B - França")
                    print("C - Estados Unidos")

                    r = input("Resposta: ").lower()

                    if r == "a" or r == "alemanha":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é Alemanha ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Descobrimento do Brasil":
                    print("\nEm que ano o Brasil foi descoberto?")
                    print("A - 1500")
                    print("B - 1822")
                    print("C - 1889")

                    r = input("Resposta: ").lower()

                    if r == "a" or r == "1500":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é 1500 ")

                    voltar = input("Digite 1 para voltar: ")

                # geografia
                elif cont_escolhido == "Climatologia":
                    print("\nQual fator climático influencia diretamente a temperatura de uma região?")
                    print("A - Latitude")
                    print("B - Internet")
                    print("C - Satélite de TV")

                    r = input("Resposta: ").lower()

                    if r == "a" or r == "latitude":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é latitude ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Globalização":
                    print("\nO que a globalização aumenta entre os países?")
                    print("A - O isolamento")
                    print("B - A integração econômica e cultural")
                    print("C - A distância geográfica")

                    r = input("Resposta: ").lower()

                    if r == "b" or r == "integração econômica e cultural" or r == "integracao economica e cultural":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é integração econômica e cultural ")

                    voltar = input("Digite 1 para voltar: ")

                elif cont_escolhido == "Hidrografia":
                    print("\nO que é uma bacia hidrográfica?")
                    print("A - Conjunto de rios interligados")
                    print("B - Uma montanha")
                    print("C - Um tipo de clima")

                    r = input("Resposta: ").lower()

                    if r == "a" or r == "conjunto de rios interligados":
                        print("✅ Correto")
                    else:
                        print("❌ Errado")
                        print("⚙️ JOVIX ESTÁ PENSANDO ⚙️")
                        print("🤖 JOVIX: A resposta correta é conjunto de rios interligados ")

                    voltar = input("Digite 1 para voltar: ")

            elif op2 == 3:
                break

def modo_jovix():
    print("\n📸 IA analisando imagem...")
    print("✅ Matéria identificada: Matemática")
    print("🤖Imagem adicionada na pasta Matématica")
    voltar = int(input("Digite 1 para voltar: "))
    print("\n")

while True:
    voltar = 0
    titulo = "JOVIX"
    print(f"{titulo:^20}")
    print("1 - Modo JOVIX")
    print("2 - Pasta Matérias")
    print("3 - Sair")

    menu = int(input("Escolha: "))

    # modo jovix
    if menu == 1:
        modo_jovix()
    elif voltar == 1:
        print("👋 Saindo do JOVIX...")
        break

    # pasta materias
    elif menu == 2:
        conteudos()

    elif menu == 3:
        print("👋 Saindo do JOVIX...")
        break
