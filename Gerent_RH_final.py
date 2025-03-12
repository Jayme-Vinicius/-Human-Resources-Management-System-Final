class Funcionários():

    def __init__(self):
        self.nome = "N/D"
        self.senha = "N/D"
        self.idade = 0
        self.função = "N/D"
        self.salario = 0
        self.salario_total = 0
        self.horas_semanais = 0
        self.status = "N/D"
        self.nota_média = 0
        self.nota_liderança = 0
        self.nota_desempenho = 0
        self.nota_profissionalismo = 0
        self.nota_habilidades_interpessoais = 0
        self.descrição = "N/D"
        self.faltas = 0
        self.benefícios_totais = 0
        self.benefícios = []
        self.descontos_totais = 0
        self.descontos = []
        self.leis = []

    def Print_Informação_Funcionário_teste(self, lista_de_funcionários, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        print(f"""
        Nome: {lista_de_funcionários[indice].nome}
        Idade: {lista_de_funcionários[indice].idade}
        Cargo: {lista_de_funcionários[indice].função}
        Salário Base: {lista_de_funcionários[indice].salario}
        Salário Total: {lista_de_funcionários[indice].salario_total}
        Benefícios Totais: {lista_de_funcionários[indice].benefícios_totais}
        Descontos Totais: {lista_de_funcionários[indice].descontos_totais}
        Horários: {lista_de_funcionários[indice].horas_semanais}
        Status: {lista_de_funcionários[indice].status}\n""")
        return lista_de_funcionários
    
# funções de background
    def Registro_Automatico_Violação_de_Lei_trabalhista(self, funcionário, lista_de_leis):
        lista_de_leis_do_funcionário = getattr(funcionário, "leis")
        lista_de_leis_do_funcionário.clear()
        for indice in range(0, len(lista_de_leis)):
            if(self.Sentença_Logica(funcionário, lista_de_leis[indice])):
                continue
            else:
                lista_de_leis_do_funcionário.append(lista_de_leis[indice])
        if lista_de_leis_do_funcionário == []:
            print(f"O Funcionário {funcionário.nome} está Regular com as leis trabalhistas\n")
            setattr(funcionário, "status", "Ativo")
        else:
            print(f"O Funcionário {funcionário.nome} está Irregular com as leis trabalhistas\n")
            setattr(funcionário, "status", "Irregular")
        return funcionário

    def Sentença_Logica(self, funcionário, sentença_logica): #caso sentença logica do beneficio/desconto para funcionario sejá verdadeiro retorna True, caso falso retorna False
        if isinstance(sentença_logica.termo_logico_1, str):
            termo_logico_1 = getattr(funcionário, sentença_logica.termo_logico_1)
        elif isinstance(sentença_logica.termo_logico_1, int):
            termo_logico_1 = sentença_logica.termo_logico_1
        else:
            print(f"erro ao identificar termo_logico_1: {sentença_logica.termo_logico_1}\n")
            return False
        if isinstance(sentença_logica.termo_logico_2, str):
            termo_logico_2 = getattr(funcionário, sentença_logica.termo_logico_2)
        elif isinstance(sentença_logica.termo_logico_2, int):
            termo_logico_2 = sentença_logica.termo_logico_2
        else:
            print(f"erro ao identificar termo_logico_2: {sentença_logica.termo_logico_2}\n")
            return False
        if sentença_logica.condição == ">":
            return termo_logico_1 > termo_logico_2
        elif sentença_logica.condição == "<":
            return termo_logico_1 < termo_logico_2
        elif sentença_logica.condição == "==":
            return termo_logico_1 == termo_logico_2
        elif sentença_logica.condição == ">=":
            return termo_logico_1 >= termo_logico_2
        elif sentença_logica.condição == "<=":
            return termo_logico_1 <= termo_logico_2
        elif sentença_logica.condição == "!=":
            return termo_logico_1 != termo_logico_2
        else:
            print(f"erro na sentença logica {termo_logico_1} {sentença_logica.condição} {termo_logico_2}")
            return False

    def Definir_Termo_Lógico(self, termo_logico, posição, objeto):
        while True:
            opção = input(f"O {posição} termo será um atributo ou um número: ")
            if opção == "número":
                termo_logico = input_inteiro(f"Digite o número que será o {posição} termo da sequencia lógica: ")
                return termo_logico
            elif opção == "atributo":
                termo_logico = input(f"Qual atributo que será comparado para obtenção do {objeto}(caso não saiba as opções de atributo digite 0): ")
                if termo_logico == "0":
                    print("""
idade
função
salario
salario_total
horas_semanais
nota_média
nota_liderança
nota_desempenho
nnota_profissionalismo
nnota_habilidades_interpessoais
faltas
benefícios_totais
descontos_totais
(é extremamente importante escrever exatamente igual)""")
                    continue
                if hasattr(Funcionários(), termo_logico):
                    return termo_logico
                else:
                    print("Atributo escrito errado")
            else:
                print("opção invalida, escolha entre atributo e número")
            
    def Definir_Condição_Logica(self, condição, objeto):
        while True:
            condição = input(f"qual o condição(operador lógico) que será usado para obtenção do {objeto}(caso não saiba as opções digite 0): ")
            if condição == 0:
                print("> , < , == , >= , <= , !=\n")
            if condição in [">", "<", "==", ">=", "<=", "!="]:
                return condição
            else:
                print("Condição invalida")

    def Registro_Benefício_Desconto_Automatico_teste(self, funcionário, lista_de_benefícios_descontos_do_funcionário, lista_beneficio_desconto):
        for indice_1 in range(0, len(lista_de_benefícios_descontos_do_funcionário)):
            for indice_2 in range(0, len(lista_de_benefícios_descontos_do_funcionário)):
                if lista_de_benefícios_descontos_do_funcionário[indice_2].condição != "N/D":
                    lista_de_benefícios_descontos_do_funcionário.pop(indice_2)
                    break
        for indice in range(0 , len(lista_beneficio_desconto)):
            if lista_beneficio_desconto[indice].condição == "N/D":
                continue
            if self.Sentença_Logica(funcionário, lista_beneficio_desconto[indice]):
                lista_de_benefícios_descontos_do_funcionário.append(lista_beneficio_desconto[indice])
        return funcionário

    def Calcular_Salario_Total(self, funcionário, lista_de_benefícios_descontos_funcionário, objeto): #Calcular o salario_total, beneficios_totais/descontos_totais de um funcionário e retorna o objeto funcionário (aplicado em Registrar, Remover e Atualizar beneficio e informações)
        objeto_total = 0
        for indice in range(0 , len(lista_de_benefícios_descontos_funcionário)):
            tipo_de_aumento = lista_de_benefícios_descontos_funcionário[indice].tipo_de_aumento
            quantia = lista_de_benefícios_descontos_funcionário[indice].quantia
            if tipo_de_aumento == "%":
                objeto_total = objeto_total + (funcionário.salario / 100 * quantia)
            elif tipo_de_aumento == "*":
                objeto_total = objeto_total + (funcionário.salario * (quantia - 1))
            elif tipo_de_aumento == "+":
                objeto_total = objeto_total + quantia
            else:
                print(f"erro na adição do tipo de aumento de {lista_de_benefícios_descontos_funcionário[indice].nome}\n")
        if objeto == "benefícios_totais":
            salario_total = funcionário.salario + objeto_total - funcionário.descontos_totais
        elif objeto == "descontos_totais":
            
            salario_total = funcionário.salario - objeto_total + funcionário.benefícios_totais
        else:
            print(f"{objeto} não é nem benefícios_totais, nem descontos_totais")
        setattr(funcionário, objeto, objeto_total)
        setattr(funcionário, "salario_total", salario_total)
        return funcionário

class Gerente(Funcionários):

    def Atualizar_Informações_teste(self, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, indice, busca, objeto):
        print(f"As Informações do {objeto} {lista_de_funcionários[indice].nome} serão serão atualizadas\n")
        lista_de_funcionários[indice].nome = input("Nome Funcionário: ")
        lista_de_funcionários[indice].senha = input("Senha do Funcionário: ")
        lista_de_funcionários[indice].idade = input_inteiro("idade do Funcionário: ")
        lista_de_funcionários[indice].função = input("função do Funcionário: ")
        lista_de_funcionários[indice].salario = input_inteiro("salário do Funcionário: ")
        lista_de_funcionários[indice].horas_semanais = input_inteiro("carga horaria do Funcionário(horas/semana): ")
        lista_de_funcionários[indice].status  = "Ativo"
        lista_de_funcionários[indice] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice], lista_de_funcionários[indice].benefícios, lista_de_benefícios)
        lista_de_funcionários[indice] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice], lista_de_funcionários[indice].descontos, lista_de_descontos)
        lista_de_funcionários[indice] = self.Calcular_Salario_Total(lista_de_funcionários[indice], lista_de_funcionários[indice].benefícios, "benefícios_totais")
        lista_de_funcionários[indice] = self.Calcular_Salario_Total(lista_de_funcionários[indice], lista_de_funcionários[indice].descontos, "descontos_totais")
        lista_de_funcionários[indice] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice], lista_de_leis)
        return lista_de_funcionários

    def Avaliação_funcionário_teste(self, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, indice, busca, objeto):
        lista_de_funcionários[indice].nota_liderança = input_inteiro(f"Em uma escala de zero a dez como você avaliaria o funcionário {lista_de_funcionários[indice].nome} em sua liderança:")
        lista_de_funcionários[indice].nota_desempenho = input_inteiro(f"Em uma escala de zero a dez como você avaliaria o funcionário {lista_de_funcionários[indice].nome} em seu desempenho:")
        lista_de_funcionários[indice].nota_profissionalismo = input_inteiro(f"Em uma escala de zero a dez como você avaliaria o funcionário {lista_de_funcionários[indice].nome} em seu profissionalismo:")
        lista_de_funcionários[indice].nota_habilidades_interpessoais = input_inteiro(f"Em uma escala de zero a dez como você avaliaria o funcionário {lista_de_funcionários[indice].nome} em suas habilidades interpessoais:")
        lista_de_funcionários[indice].descrição = input(f"como você descreveria o funcionário {lista_de_funcionários[indice].nome}:")
        lista_de_funcionários[indice].faltas = input_inteiro(f"quantas faltas o funcionário {lista_de_funcionários[indice].nome} teve nesse mês:")
        lista_de_funcionários[indice].nota_média = (lista_de_funcionários[indice].nota_liderança + lista_de_funcionários[indice].nota_desempenho + lista_de_funcionários[indice].nota_profissionalismo + lista_de_funcionários[indice].nota_habilidades_interpessoais) / 4
        lista_de_funcionários[indice] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice], lista_de_funcionários[indice].benefícios, lista_de_benefícios)
        lista_de_funcionários[indice] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice], lista_de_funcionários[indice].descontos, lista_de_descontos)
        lista_de_funcionários[indice] = self.Calcular_Salario_Total(lista_de_funcionários[indice], lista_de_funcionários[indice].benefícios, "benefícios_totais")
        lista_de_funcionários[indice] = self.Calcular_Salario_Total(lista_de_funcionários[indice], lista_de_funcionários[indice].descontos, "descontos_totais")
        lista_de_funcionários[indice] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice], lista_de_leis)
        return lista_de_funcionários
    
    def Print_Avaliação_funcionário_teste(self, lista_de_funcionários, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        print(f"Nome: {lista_de_funcionários[indice].nome}")
        print(f"Nota Média: {lista_de_funcionários[indice].nota_média}")
        print(f"Nota de Liderança: {lista_de_funcionários[indice].nota_liderança}")
        print(f"Nota de Desempenho: {lista_de_funcionários[indice].nota_desempenho}")
        print(f"Nota de Profissionalismo: {lista_de_funcionários[indice].nota_profissionalismo}")
        print(f"Nota de Habilidades Interpessoais: {lista_de_funcionários[indice].nota_habilidades_interpessoais}")
        print(f"Descrição: {lista_de_funcionários[indice].descrição}")
        print(f"Faltas: {lista_de_funcionários[indice].faltas}")
        return lista_de_funcionários
    
    def Print_Benefício_Desconto_teste(self, lista_de_benefícios_descontos, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        print(f"Nome do {objeto}: {lista_de_benefícios_descontos[indice].nome}")
        print(f"Tipo de {objeto}: {lista_de_benefícios_descontos[indice].tipo_de_aumento}")
        print(f"Quantia do {objeto}: {lista_de_benefícios_descontos[indice].quantia}")
        if lista_de_benefícios_descontos[indice].condição == "N/D":
            print(f"Sentença lógica para a Obtenção do {objeto}: Não foi automatizado")
        else:
            print(f"Sentença lógica para a Obtenção do {objeto}: {lista_de_benefícios_descontos[indice].termo_logico_1} {lista_de_benefícios_descontos[indice].condição} {lista_de_benefícios_descontos[indice].termo_logico_2}")
        return lista_de_benefícios_descontos
    
    def Print_Benefício_Desconto_Funcionários(self, lista_de_funcionarios, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        objeto_atributo = objeto.split()[0].lower()
        objeto = objeto.split()[0][0:-1]
        lista_de_benefício_desconto_do_funcionário = getattr(lista_de_funcionários[indice], objeto_atributo)
        print(f"O Funcionário {lista_de_funcionarios[indice].nome} tem os seguintes {objeto_atributo}\n")
        if len(lista_de_benefício_desconto_do_funcionário) == 0:
            print(f"O {lista_de_funcionarios[indice].nome} Não possui {objeto_atributo}\n")
        for indice_0 in range(0, len(lista_de_benefício_desconto_do_funcionário)):
            print(f"Nome: {lista_de_benefício_desconto_do_funcionário[indice_0].nome}")
            print(f"Tipo de {objeto}: {lista_de_benefício_desconto_do_funcionário[indice_0].tipo_de_aumento}")
            print(f"Quantia do {objeto}: {lista_de_benefício_desconto_do_funcionário[indice_0].quantia}")
            if lista_de_benefício_desconto_do_funcionário[indice_0].condição == "N/D":
                print(f"Sentença lógica para a Obtenção do {objeto}: Não foi automatizado")
            else:
                print(f"Sentença lógica para a Obtenção do {objeto}: {lista_de_benefício_desconto_do_funcionário[indice_0].termo_logico_1} {lista_de_benefício_desconto_do_funcionário[indice_0].condição} {lista_de_benefício_desconto_do_funcionário[indice_0].termo_logico_2}")
        return lista_de_funcionarios
    
    def Registrar_Benefício_Desconto_teste(self, lista_de_funcionários, lista_de_benefícios_descontos, lista_vazia_3, lista_de_leis, indice, busca, objeto):
            objeto_atributo = objeto.split()[0].lower() #
            lista_de_benefício_desconto_do_funcionário = getattr(lista_de_funcionários[indice], objeto_atributo) 
            while True:
                escolha = input(f"O Registro do {objeto}s será automatico ou manual: ").strip().lower()    
                if escolha == "manual":
                    for indice_0 in range(0 , len(lista_de_benefícios_descontos)):
                        benefício_desconto = input(f"O funcionário {lista_de_funcionários[indice].nome} Recebe o {objeto} {lista_de_benefícios_descontos[indice_0].nome}(sim ou não): ").strip().lower()
                        if lista_de_benefícios_descontos[indice_0] in lista_de_benefício_desconto_do_funcionário:
                            print(f"O Funcionário {lista_de_funcionários[indice].nome} já tem o {objeto.split()[0][0:-1]} {lista_de_benefícios_descontos[indice_0].nome} Registrado\n")
                            continue
                        if benefício_desconto == "sim":
                            lista_de_benefício_desconto_do_funcionário.append(lista_de_benefícios_descontos[indice_0])
                    break
                elif escolha == "automatico": 
                    print(f"Os {objeto_atributo} Automatizados foram Automaticamente aplicados a {lista_de_funcionários[indice].nome}")
                    for indice_0 in range(0 , len(lista_de_benefícios_descontos)):
                        if lista_de_benefícios_descontos[indice_0].condição == "N/D":
                            print(f"{lista_de_benefícios_descontos[indice_0].nome} não foi automatizado logo não será considerado\n")
                            continue
                        if lista_de_benefícios_descontos[indice_0] in lista_de_benefício_desconto_do_funcionário:
                            print(f"O Funcionário {lista_de_funcionários[indice].nome} já tem o {objeto.split()[0][0:-1]} {lista_de_benefícios_descontos[indice_0].nome} Registrado\n")
                            continue
                        if self.Sentença_Logica(lista_de_funcionários[indice], lista_de_benefícios_descontos[indice_0]):
                            print(f"O Funcionário {lista_de_funcionários[indice].nome},  receberá o {objeto.split()[0][0:-1]} {lista_de_benefícios_descontos[indice_0].nome}")
                            lista_de_benefício_desconto_do_funcionário.append(lista_de_benefícios_descontos[indice_0])
                        else:
                            print(f"O Funcionário {lista_de_funcionários[indice].nome}, Não receberá o {objeto.split()[0][0:-1]} {lista_de_benefícios_descontos[indice_0].nome}")
                    break
                else:
                    print("escolha entre manual ou automatica\n")
            lista_de_funcionários[indice] = self.Calcular_Salario_Total(lista_de_funcionários[indice], lista_de_benefício_desconto_do_funcionário, objeto.split()[0].lower() + "_totais")
            lista_de_funcionários[indice] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice], lista_de_leis)
            return lista_de_funcionários

    def Print_Leis_teste(self, lista_de_leis, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
            print(f"Nome da {objeto}: {lista_de_leis[indice].nome}")
            print(f"Sentença lógica para o cumprimento da {objeto}: {lista_de_leis[indice].termo_logico_1} {lista_de_leis[indice].condição} {lista_de_leis[indice].termo_logico_2}\n")
            return lista_de_leis
    
    def Print_Leis_dos_Funcionários(self, lista_de_funcionários, lista_vazia_2, lista_vazia_3, lista_vazia_4,  indice, busca, objeto):
        if lista_de_funcionários[indice].leis == []:
            (f"Parabens, O Funcionário {lista_de_funcionários[indice].nome} não possui as nenhuma {objeto} trabalhista em estado de irregularridadezn\n")
        else:
            print(f"O Funcionário {lista_de_funcionários[indice].nome} possui as seguintes {objeto}s em estado de irregularridade\n")
            for indice_0 in range(0, len(lista_de_funcionários[indice].leis)):
                print(f"Nome: {lista_de_funcionários[indice].leis[indice_0].nome}")
                print(f"Sentença Logica Necessária para o Cumprimento da lei: {lista_de_funcionários[indice].leis[indice_0].termo_logico_1} {lista_de_funcionários[indice].leis[indice_0].condição} {lista_de_funcionários[indice].leis[indice_0].termo_logico_2}\n")
        return lista_de_funcionários

class Chefe(Gerente):
    
    
    def Adicionar_funcionário_teste(self, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, objeto):
        novo_funcionário = Funcionários()
        novo_funcionário.nome = input(f"Nome do {objeto}: ")
        novo_funcionário.senha = input(f"Senha do {objeto}: ")
        novo_funcionário.idade = input_inteiro(f"Idade do {objeto}: ")
        novo_funcionário.função = input(f"Função do {objeto}: ")
        novo_funcionário.salario = input_inteiro(f"Salário do {objeto}: ")
        novo_funcionário.salario_total = novo_funcionário.salario
        novo_funcionário.horas_semanais = input_inteiro(f"Carga Horaria do {objeto}(horas/semana): ")
        novo_funcionário.status  = "Ativo"
        novo_funcionário = self.Registro_Benefício_Desconto_Automatico_teste(novo_funcionário, novo_funcionário.benefícios, lista_de_benefícios)
        novo_funcionário = self.Registro_Benefício_Desconto_Automatico_teste(novo_funcionário, novo_funcionário.descontos, lista_de_descontos)
        novo_funcionário = self.Calcular_Salario_Total(novo_funcionário, novo_funcionário.benefícios, "benefícios_totais")
        novo_funcionário = self.Calcular_Salario_Total(novo_funcionário, novo_funcionário.descontos, "descontos_totais")
        novo_funcionário = self.Registro_Automatico_Violação_de_Lei_trabalhista(novo_funcionário, lista_de_leis)
        lista_de_funcionários.append(novo_funcionário)
        return lista_de_funcionários

    def Remover_Funcionário_teste(self, lista_de_funcionários, lista_vazia_2, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        if(busca == "todos"):
            print("todos os funcionarios foram Demitidos\n")
            lista_de_funcionários.clear()
        else:
            print(f"O Funcionário {lista_de_funcionários[indice].nome} foi Demitido\n")
            lista_de_funcionários.pop(indice)
        return lista_de_funcionários

    def Adicionar_Benefício_Desconto_teste(self, lista_de_benefícios_descontos, lista_de_funcionários, lista_vazia_3, lista_de_leis, objeto):
        objeto_atributo = objeto.lower() + "s" 
        novo_benefício = Benefício_Desconto()
        novo_benefício.nome = input(f"Nome Do {objeto}: ")
        while True:    
            novo_benefício.tipo_de_aumento = input(f"Tipo de {objeto} Será:\nPercentual(%)\nMultiplicatio(*)\nSomativo(+): ")
            if novo_benefício.tipo_de_aumento in ["%", "*", "+"]:
                    break
            else:
                print("Opção invalida")
        novo_benefício.quantia = input_inteiro(f"Quantia desse {objeto}: ")
        automatização = input(f"Deseja adicionar uma Expressão lógica para automatizar o Registro do(a) {objeto}(sim ou não):").strip().lower()
        if automatização == "não":
            novo_benefício.termo_logico_1 = "N/D"
            novo_benefício.condição = "N/D"
            novo_benefício.termo_logico_2 = "N/D"
        elif automatização == "sim":
            while True:
                novo_benefício.termo_logico_1 = self.Definir_Termo_Lógico(novo_benefício.termo_logico_1, "1°", objeto)
                novo_benefício.condição = self.Definir_Condição_Logica(novo_benefício.condição, objeto)
                novo_benefício.termo_logico_2 = self.Definir_Termo_Lógico(novo_benefício.termo_logico_2, "2°", objeto)
                escolha = input(f"a sentença logica para obtenção do {objeto} ficou assim({novo_benefício.termo_logico_1} {novo_benefício.condição} {novo_benefício.termo_logico_2}), Deseja confirmar essa sentença lógica(sim ou não): ").strip().lower()
                if escolha == "sim":
                    break  
                elif escolha == "não":
                    continue
                else: 
                    print("Opção invalida, escolha entre sim ou não")
        else:
            print("Opção invalida, escolha entre sim ou não")
        lista_de_benefícios_descontos.append(novo_benefício)
        for indice_0 in range(0, len(lista_de_funcionários)):
            lista_de_benefícios_descontos_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
            lista_de_funcionários[indice_0] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, lista_de_benefícios_descontos)
            lista_de_funcionários[indice_0] = self.Calcular_Salario_Total(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, objeto_atributo + "_totais")
            lista_de_funcionários[indice_0] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice_0], lista_de_leis)
        return lista_de_benefícios_descontos
    
    def Remover_Benefício_Desconto_teste(self, lista_de_benefícios_descontos, lista_de_funcionários, lista_vazia_3, lista_de_leis, indice, busca, objeto):
        objeto_atributo = objeto.lower() + "s"
        if busca == "todos":
            print(f"todos os {objeto}s foram Removidos")
            lista_de_benefícios_descontos.clear()
            for indice_0 in range(0, len(lista_de_funcionários)):
                lista_de_benefício_desconto_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
                lista_de_benefício_desconto_do_funcionário.clear()
        else:
            print(f"o {objeto} {lista_de_benefícios_descontos[indice].nome} foi Removido")
            for indice_0 in range(0 , len(lista_de_funcionários)):
                lista_de_benefício_desconto_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
                for indice_1 in range(0 , len(lista_de_benefício_desconto_do_funcionário)):
                    if lista_de_benefício_desconto_do_funcionário[indice_1].nome == lista_de_benefícios_descontos[indice].nome:
                        lista_de_benefício_desconto_do_funcionário.pop(indice_1)
                        break
            lista_de_benefícios_descontos.pop(indice)
        for indice_0 in range(0, len(lista_de_funcionários)):
            lista_de_benefícios_descontos_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
            lista_de_funcionários[indice_0] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, lista_de_benefícios_descontos)
            lista_de_funcionários[indice_0] = self.Calcular_Salario_Total(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, objeto_atributo + "_totais")
            lista_de_funcionários[indice_0] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice_0], lista_de_leis)
        return lista_de_benefícios_descontos
    
    def Atualizar_Benefício_Deconto_teste(self, lista_de_benefícios_descontos, lista_de_funcionários, lista_vazia_3, lista_de_leis, indice, busca, objeto):
        objeto_atributo = objeto.lower() + "s"#
        antigo_benefício_desconto = Benefício_Desconto()
        antigo_benefício_desconto = lista_de_benefícios_descontos[indice]
        print(f"As informações do {objeto} {lista_de_benefícios_descontos[indice].nome} serão modificadas\n")
        lista_de_benefícios_descontos[indice].nome = input(f"Nome Do {objeto}: ")
        while True:    
            lista_de_benefícios_descontos[indice].tipo_de_aumento = input(f"Tipo de {objeto} Será:\nPercentual(%)\nMultiplicatio(*)\nSomativo(+): ")
            if lista_de_benefícios_descontos[indice].tipo_de_aumento in ["%", "*", "+"]:
                    break
            else:
                print("Opção invalida")
        lista_de_benefícios_descontos[indice].quantia = input_inteiro(f"Quantia desse {objeto}: ")
        automatização = input(f"Deseja adicionar uma Expressão lógica para automatizar o Registro do(a) {objeto}(sim ou não):").strip().lower()
        if automatização == "não":
            lista_de_benefícios_descontos[indice].termo_logico_1 = "N/D"
            lista_de_benefícios_descontos[indice].condição = "N/D"
            lista_de_benefícios_descontos[indice].termo_logico_2 = "N/D"
        elif automatização == "sim":
            while True:
                lista_de_benefícios_descontos[indice].termo_logico_1 = self.Definir_Termo_Lógico(lista_de_benefícios_descontos[indice].termo_logico_1, "1°", objeto)
                lista_de_benefícios_descontos[indice].condição = self.Definir_Condição_Logica(lista_de_benefícios_descontos[indice].condição, objeto)
                lista_de_benefícios_descontos[indice].termo_logico_2 = self.Definir_Termo_Lógico(lista_de_benefícios_descontos[indice].termo_logico_2, "2°", objeto)
                escolha = input(f"a sentença logica para obtenção do {objeto} ficou assim({lista_de_benefícios_descontos[indice].termo_logico_1} {lista_de_benefícios_descontos[indice].condição} {lista_de_benefícios_descontos[indice].termo_logico_2}), Deseja confirmar essa sentença lógica(sim ou não): ").strip().lower()
                if escolha == "sim":
                    break  
                elif escolha == "não":
                    continue
                else: 
                    print("Opção invalida, escolha entre sim ou não")
        else:
            print("Opção invalida, escolha entre sim ou não")
        for indice_0 in range(0, len(lista_de_funcionários)):
            lista_de_benefícios_descontos_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
            for indice_1 in range(0 , len(lista_de_benefícios_descontos_do_funcionário)):
                if lista_de_benefícios_descontos_do_funcionário[indice_1].nome == antigo_benefício_desconto.nome:
                    print(f"O {objeto} {antigo_benefício_desconto.nome} do Funcionário {lista_de_funcionários[indice_0].nome} foi atualizado\n")
                    lista_de_benefícios_descontos_do_funcionário[indice_1] = lista_de_benefícios_descontos[indice]
        for indice_0 in range(0, len(lista_de_funcionários)):
            lista_de_benefícios_descontos_do_funcionário = getattr(lista_de_funcionários[indice_0], objeto_atributo) 
            lista_de_funcionários[indice_0] = self.Registro_Benefício_Desconto_Automatico_teste(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, lista_de_benefícios_descontos)
            lista_de_funcionários[indice_0] = self.Calcular_Salario_Total(lista_de_funcionários[indice_0], lista_de_benefícios_descontos_do_funcionário, objeto_atributo + "_totais")
            lista_de_funcionários[indice_0] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice_0], lista_de_leis)
        return lista_de_benefícios_descontos

    def Adicionar_Lei_teste(self, lista_de_leis, lista_de_funcionários, lista_vazia_3, lista_vazia_4, objeto):
        nova_lei = Lei()
        nova_lei.nome = input(f"Nome da {objeto}: ")
        while True:    
            nova_lei.termo_logico_1 = self.Definir_Termo_Lógico(nova_lei.termo_logico_1, "1°", objeto)
            nova_lei.condição = self.Definir_Condição_Logica(nova_lei.condição, objeto)
            nova_lei.termo_logico_2 = self.Definir_Termo_Lógico(nova_lei.termo_logico_2, "2°", objeto)
            escolha = input(f"a sentença logica para obtenção do {objeto} ficou assim({nova_lei.termo_logico_1} {nova_lei.condição} {nova_lei.termo_logico_2}), Deseja confirmar essa sentença lógica(sim ou não): ").strip().lower()
            if escolha == "sim":
                break  
            elif escolha == "não":
                continue
            else: 
                print("Opção invalida, escolha entre sim ou não")
        lista_de_leis.append(nova_lei)
        for indice in range(0, len(lista_de_funcionários)):
            lista_de_funcionários[indice] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice], lista_de_leis)
        return lista_de_leis
    
    def Remover_Lei_teste(self, lista_de_leis, lista_de_funcionários, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        if busca == "todos":
            lista_de_leis.clear()
            for indice_0 in range(0 , len(lista_de_funcionários)):
                lista_leis_funcionários = getattr(lista_de_funcionários[indice_0], "leis")
                lista_leis_funcionários.clear()
        else:
            print(f"A {objeto} {lista_de_leis[indice].nome} foi excluida\n")
            for indice_0 in range(0 , len(lista_de_funcionários)):
                lista_leis_funcionários = getattr(lista_de_funcionários[indice_0], "leis") 
                for indice_1 in range(0 , len(lista_leis_funcionários)):
                    if lista_leis_funcionários[indice_1].nome == lista_de_leis[indice].nome:
                        lista_leis_funcionários.pop(indice_1)
                        break
            lista_de_leis.pop(indice)
            for indice_0 in range(0, len(lista_de_funcionários)):
                lista_de_funcionários[indice_0] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice_0], lista_de_leis)
        return lista_de_leis
    
    def Atualizar_Lei_teste(self, lista_de_leis, lista_de_funcionários, lista_vazia_3, lista_vazia_4, indice, busca, objeto):
        print(f"As informações do {objeto} {lista_de_leis[indice].nome} serão modificadas\n")
        lista_de_leis[indice].nome = input(f"Nome da {objeto}: ")
        while True:    
            lista_de_leis[indice].termo_logico_1 = self.Definir_Termo_Lógico(lista_de_leis[indice].termo_logico_1, "1°", objeto)
            lista_de_leis[indice].condição = self.Definir_Condição_Logica(lista_de_leis[indice].condição, objeto)
            lista_de_leis[indice].termo_logico_2 = self.Definir_Termo_Lógico(lista_de_leis[indice].termo_logico_2, "2°", objeto)
            escolha = input(f"a sentença logica para obtenção do {objeto} ficou assim({lista_de_leis[indice].termo_logico_1} {lista_de_leis[indice].condição} {lista_de_leis[indice].termo_logico_2}), Deseja confirmar essa sentença lógica(sim ou não): ").strip().lower()
            if escolha == "sim":
                break  
            elif escolha == "não":
                continue
            else: 
                print("Opção invalida, escolha entre sim ou não")
        for indice in range(0, len(lista_de_funcionários)):
            lista_de_funcionários[indice] = self.Registro_Automatico_Violação_de_Lei_trabalhista(lista_de_funcionários[indice], lista_de_leis)
        return lista_de_leis
    

class Lei():
    def __init__(self):
        self.nome = "N/D"
        self.termo_logico_1 = "N/D"
        self.condição = "N/D"
        self.termo_logico_2 = "N/D" 
    
class Benefício_Desconto(Lei):
    
    def __init__(self):
        super().__init__()
        self.tipo_de_aumento = "N/D"
        self.quantia = 0

def input_inteiro(mensagem):
        while True:
            try:
                valor = int(input(mensagem))
                return valor
            except ValueError:
                print("Erro: Por favor, digite apenas números inteiros.")

def função_sem_busca(função, lista_1, lista_2, lista_3, lista_4, ação,  objeto):
    while True:
        lista_1 = função(lista_1, lista_2, lista_3, lista_4, objeto)
        while True:    
            escolha = (input(f"Deseja continuar {ação} {objeto}s ou Deseja sair\n\n"))
            match escolha:
                case 'sair':
                    return lista_1
                case 'continuar':
                    print("\n")
                    break
                case _:
                    print("Opção invalida")
                    continue 

def função_com_busca(função, lista_1, lista_2, lista_3, lista_4, ação, objeto):
    if lista_1 == []:
        print(f"a lista de {objeto.split()[0]}s está vazia")
        return lista_1
    while True: 
        busca = input (f"Deseja {ação} todos os {objeto}s, uma lista de {objeto}s ou em um {objeto} em especifico\n").strip().lower()   
        match busca:
            case "todos":
                for indice in range(0, len(lista_1)):
                    lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
            case "lista":
                tamanho_lista = input_inteiro(f"quantos {objeto}s você procura: ")
                lista_temporaria = []
                print(f"Coloque o nome dos {objeto}s que você procura:")
                for indice_0 in range(0, tamanho_lista):
                    objeto_procurado = input(f"{objeto} {indice_0}: ").strip().lower()
                    lista_temporaria.append(objeto_procurado)
                for indice_1 in range(0, tamanho_lista):
                    achado = 0
                    for indice_2 in range(0, len(lista_1)):
                        if lista_temporaria[indice_1] == (lista_1[indice_2].nome).strip().lower():    
                            lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                            achado = 1
                    for indice_2 in range(0, len(lista_2)):
                        if lista_temporaria[indice_1] == (lista_2[indice_2].nome).strip().lower():    
                            lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                            achado = 1
                    for indice_2 in range(0, len(lista_3)):
                        if lista_temporaria[indice_1] == (lista_3[indice_2].nome).strip().lower():    
                            lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                            achado = 1
                    for indice_2 in range(0, len(lista_4)):
                        if lista_temporaria[indice_1] == (lista_3[indice_2].nome).strip().lower():    
                            lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                            achado = 1
                    if achado == 0:
                        print(f"O {objeto} procurado {lista_temporaria[indice_1]} não foi encontrado\n")
            case "especifico":
                objeto_procurado = input(f"qual {objeto} você está buscando: ").strip().lower()
                achado = 0
                for indice in range(0, len(lista_1)):
                    if (lista_1[indice].nome).strip().lower() == objeto_procurado:
                        lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                        achado = 1
                for indice in range(0, len(lista_2)):
                    if (lista_2[indice].nome).strip().lower() == objeto_procurado:
                        lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                        achado = 1
                for indice in range(0, len(lista_3)):
                    if (lista_3[indice].nome).strip().lower() == objeto_procurado:
                        lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                        achado = 1
                for indice in range(0, len(lista_4)):
                    if (lista_4[indice].nome).strip().lower() == objeto_procurado:
                        lista_1 = função(lista_1, lista_2, lista_3, lista_4, indice, busca, objeto)
                        achado = 1
                if achado == 0:
                    print(f"O {objeto} procurado {objeto_procurado} não foi encontrado\n")    
            case _:
                print("escolha invalida, escolha entre todos, lista ou especifico\n")
                continue
        while True:    
            escolha = (input(f"Deseja continuar {ação[0:-1] + "ndo"} {objeto}s ou Deseja sair\n\n"))
            match escolha:
                case 'sair':
                    return lista_1
                case 'continuar':
                    print("\n")
                    break
                case _:
                    print("Opção invalida")
                    continue 

print("Olá seja bem vindo ao gerenciador de RH\n")
funcionário_atual = Chefe()
lista_de_funcionários = []
lista_de_benefícios = []
lista_de_descontos = []
lista_de_leis = []
lista_vazia = [] #tapa os buracos na chamada da função, já que para funções gerais e funções com busca alguns funções precisam de mais do que outras então esse "tapa o buraco" com nada evitando possiveis dores de cabeça
while (1):
    choice_1 = (input("""
Selecione a opção que desejar:
Visualizar opções(0)\n\n"""))
    match choice_1:
        case '0':
            print("""
Visualizar sobre Funcionários (1)
Visualizar Sobre Pagamentos, Benefícios e Descontos (2)
Visualizar Sobre Leis Trabalhistas (3)
Sair(-1)\n""")
        case '1':
            choice_2 = (input("""
Visualizar Lista de Funcionários (1)
Contratar Funcionários (2)
Demitir Funcionários (3)
Atualizar o Perfil dos Funcionários(4)
Ver Avaliação Funcionários (5)                              
Avaliar os Funcionários (6)
Registrar Benefício dos Funcionários (7)
Registrar Descontos dos Funcionários (8)                              
Voltar (-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Print_Informação_Funcionário_teste, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Visualizar a Lista de", "Funcionário")
                case '2':
                    lista_de_funcionários = função_sem_busca(funcionário_atual.Adicionar_funcionário_teste, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, "Adicionar", "Funcionário")#
                case '3':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Remover_Funcionário_teste, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Remover", "Funcionário")
                case '4':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Atualizar_Informações_teste, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, "Atualizar informações de", "Funcionário")#
                case '5':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Print_Avaliação_funcionário_teste, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Mostrar Avaliações de", "Funcionário")
                case '6':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Avaliação_funcionário_teste, lista_de_funcionários, lista_de_benefícios, lista_de_descontos, lista_de_leis, "Avaliar de", "Funcionário")#
                case '7':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Registrar_Benefício_Desconto_teste, lista_de_funcionários, lista_de_benefícios, lista_vazia, lista_vazia, "Registrar", "Benefícios dos Funcionário")
                case '8':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Registrar_Benefício_Desconto_teste, lista_de_funcionários, lista_de_descontos, lista_vazia, lista_vazia, "Registrar", "Descontos dos Funcionário")
                case '-1':
                    continue
                case _:
                    print("Opção invalida\n\n")
        case '2':
            choice_2 = (input("""
Ver Lista de Benefícios (1)
Ver os Funcionários que Recebem Benefício (2)                             
Adicionar Benefícios (3)
Remover Benefícios (4)
Atualizar Benefícios (5)
Ver Lista de Descontos (6)    
Ver os Funcionários que Recebem Desconto (7)                          
Adicionar Descontos (8)
Remover Descontos (9)
Atualizar Descontos (10)
Voltar(-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_benefícios = função_com_busca(funcionário_atual.Print_Benefício_Desconto_teste, lista_de_benefícios, lista_vazia, lista_vazia, lista_vazia, "Visualizar a lista de", "Benefício")
                case '2':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Print_Benefício_Desconto_Funcionários, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Visualizar", "Benefícios dos Funcionários")
                case '3':
                    lista_de_benefícios = função_sem_busca(funcionário_atual.Adicionar_Benefício_Desconto_teste, lista_de_benefícios, lista_de_funcionários, lista_vazia, lista_de_leis, "Adicionar", "Benefício")# 
                case '4':                                                                                                                                                                
                    lista_de_benefícios = função_com_busca(funcionário_atual.Remover_Benefício_Desconto_teste, lista_de_benefícios, lista_de_funcionários, lista_vazia, lista_vazia, "Remover", "Benefício")#
                case '5':
                    lista_de_benefícios = função_com_busca(funcionário_atual.Atualizar_Benefício_Deconto_teste, lista_de_benefícios, lista_de_funcionários, lista_vazia, lista_de_leis, "Modificar a lista de", "Benefício")#
                case '6':
                    lista_de_descontos = função_com_busca(funcionário_atual.Print_Benefício_Desconto_teste, lista_de_descontos, lista_vazia, lista_vazia, lista_vazia, "Visualizar a lista de", "Desconto")
                case '7':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Print_Benefício_Desconto_Funcionários, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Visualizar", "Descontos dos Funcionários")
                case '8':
                    lista_de_descontos = função_sem_busca(funcionário_atual.Adicionar_Benefício_Desconto_teste, lista_de_descontos, lista_de_funcionários, lista_vazia, lista_de_leis, "Adicionar", "Desconto")#
                case '9':
                    lista_de_descontos = função_com_busca(funcionário_atual.Remover_Benefício_Desconto_teste, lista_de_descontos, lista_de_funcionários, lista_vazia, lista_vazia, "Remover", "Desconto")#
                case '10':
                    lista_de_descontos = função_com_busca(funcionário_atual.Atualizar_Benefício_Deconto_teste, lista_de_descontos, lista_de_funcionários, lista_vazia, lista_de_leis, "Modificar a lista de", "Desconto")#
        case '3':
            choice_3 = input("""
Ver Lista de Leis Trabalhistas (1)
Ver Lista de Trabalhadores Irregulares(2)
Adicionar Leis Trabalhistas (3)
Remover Leis Trabalhistas (4)
Atualizar Leis Trabalhitas (5)\n\n""")        
            match choice_3:
                case '1':
                    lista_de_leis = função_com_busca(funcionário_atual.Print_Leis_teste, lista_de_leis, lista_vazia, lista_vazia, lista_vazia, "Visualizar a lista de", "Lei")
                case '2':
                    lista_de_funcionários = função_com_busca(funcionário_atual.Print_Leis_dos_Funcionários, lista_de_funcionários, lista_vazia, lista_vazia, lista_vazia, "Visualizar a lista de", "Leis Irregulares dos Funcionários")
                case '3':
                    lista_de_leis = função_sem_busca(funcionário_atual.Adicionar_Lei_teste, lista_de_leis, lista_de_funcionários, lista_vazia, lista_vazia, "Adicionar", "Lei")
                case '4':
                    lista_de_leis = função_com_busca(funcionário_atual.Remover_Lei_teste, lista_de_leis, lista_de_funcionários, lista_vazia, lista_vazia, "Remover", "Lei")
                case '5':
                    lista_de_leis = função_com_busca(funcionário_atual.Atualizar_Lei_teste, lista_de_leis, lista_de_funcionários, lista_vazia, lista_vazia, "Atualizar", "Lei")
        case '-1':
            print("Obrigado pela preferencia :)")
            break
        case _:
            print("Opção invalida")  