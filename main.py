import pandas as pd

doc = pd.read_csv('./br-capes-bolsistas-uab.csv', encoding='ISO-8859-1',sep=';')

anos_presentes = doc['AN_REFERENCIA'].unique()


def search_year():
    try:
        ano_escolhido = int(input('Digite o ano desejado para consulta do bolsista zero:  '))
    except ValueError:
        print("Digite um numero!")
        ano_escolhido = int(input('Digite o ano desejado para consulta do bolsista zero:  '))
    while(type(ano_escolhido) != int or int(ano_escolhido) not in anos_presentes):
        print("Ano inválido, digite novamente...\n")
        ano_escolhido = int(input('Digite o ano desejado para consulta do bolsista zero:  '))

    candidato = doc[doc['AN_REFERENCIA'] == ano_escolhido].iloc[-1]

    print(f"Nome: {candidato['NM_BOLSISTA']} \nCPF: {candidato['CPF_BOLSISTA']} \nEntidade de Ensino: {candidato['NM_ENTIDADE_ENSINO']} \nValor: {candidato['VL_BOLSISTA_PAGAMENTO']}")

def search_name():
    name = input('Digite o nome para pesquisa e encrypting: ')
    
    try:
        candidato = doc[doc['NM_BOLSISTA'].str.contains(name.upper())].iloc[0]
        
        nome_candidato = candidato['NM_BOLSISTA'].split(' ')
        cyphered_name = []
        for name in nome_candidato:
            name_cifrado = name[-1] + name[1:-1] + name[0]
            substituted_name = ''

            if name_cifrado[::-1] != name:
                name_cifrado = name_cifrado[::-1]
            
            for letter in name_cifrado:
                code=ord(letter)
                nxt_letter=chr(code+1) if code != 90 else 'A' 
                substituted_name=substituted_name+ nxt_letter 
            
            cyphered_name.append(substituted_name)

        return_name = ' '.join(cyphered_name)

        print(f"Nome: {return_name} \n CPF: {candidato['CPF_BOLSISTA']} \n Entidade de Ensino: {candidato['NM_ENTIDADE_ENSINO']} \n Valor: {candidato['VL_BOLSISTA_PAGAMENTO']} \n ")
    except IndexError:
        print("Nome não encontrado na planilha!\n")
        print("Voltando ao menu do sistema...\n")

    

def search_average():
    try:
        ano_escolhido = int(input("Digite o ano para média anual das bolsas: "))
    except ValueError:
        print("Digite um numero!")
        ano_escolhido = int(input("Digite o ano para média anual das bolsas: "))
    while(type(ano_escolhido) != int or int(ano_escolhido) not in anos_presentes):
        print("Ano inválido, digite novamente...\n")
        ano_escolhido = int(input("Digite o ano para média anual das bolsas: "))

    media_bolsas = doc[doc['AN_REFERENCIA'] == ano_escolhido]['VL_BOLSISTA_PAGAMENTO']
    media_bolsas = round(media_bolsas.sum()/media_bolsas.size, 2)
    print(f"O valor da média das bolsa do ano {ano_escolhido} é R$ {media_bolsas}\n\n".replace(".", ","))

def search_value_ranking():

    sorted_doc = doc.sort_values(by=['VL_BOLSISTA_PAGAMENTO'], ascending=False, ignore_index=True)

    print(f"""

Top 3 Alunos:
    1
    Nome: {sorted_doc['NM_BOLSISTA'][0]}
    CPF: {sorted_doc['CPF_BOLSISTA'][0]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][0]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][0]}
    
    2
    Nome: {sorted_doc['NM_BOLSISTA'][1]}
    CPF: {sorted_doc['CPF_BOLSISTA'][1]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][1]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][1]}
    
    3
    Nome: {sorted_doc['NM_BOLSISTA'][2]}
    CPF: {sorted_doc['CPF_BOLSISTA'][2]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][2]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][2]}
    
Bottom 3 Alunos:
    1
    Nome: {sorted_doc['NM_BOLSISTA'][len(doc)-1]}
    CPF: {sorted_doc['CPF_BOLSISTA'][len(doc)-1]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][len(doc)-1]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][len(doc)-1]}
    
    2
    Nome: {sorted_doc['NM_BOLSISTA'][len(doc)-2]}
    CPF: {sorted_doc['CPF_BOLSISTA'][len(doc)-2]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][len(doc)-2]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][len(doc)-2]}
    
    3
    Nome: {sorted_doc['NM_BOLSISTA'][len(doc)-3]}
    CPF: {sorted_doc['CPF_BOLSISTA'][len(doc)-3]}
    Entidade de Ensino: {sorted_doc['NM_ENTIDADE_ENSINO'][len(doc)-3]}
    Valor: {sorted_doc['VL_BOLSISTA_PAGAMENTO'][len(doc)-3]}

    """)

def main():
    while True:
        option = int(input('Olá, seja bem vindo ao sistema. \n\nDigite 1 para pesquisar o primeiro candidato de um ano específico \nDigite 2 para pesquisar um candidato pelo nome \nDigite 3 para pesquisar a media do valor pago em um ano específico \nDigite 4 para pesquisar os 3 melhores e piores alunos \nDigite 5 para sair \n\nEscolha qual opção você quer acessar: '))

        if option == 1:
            search_year()
            continue

        elif option == 2:
            search_name()
            continue

        elif option == 3:
            search_average()
            continue

        elif option == 4:
            search_value_ranking()
            continue
        
        elif option == 5:
            print("Saindo do programa...")
            break
        else:
            print('Opção invalida, digite novamente...')
            continue

main()




