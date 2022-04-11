#from itertools import product
class Product:
    codigo=None
    Nome=None
    Preco=None
    Qdemestoque=None

vectproduct=[]
found=False
while True:
    InfProduct=Product()
    InfProduct.codigo=int(input("Digite o código do seu produto:"))
    InfProduct.Nome=input("Digite o nome do seu produto:")
    InfProduct.Preco=float(input("Digite o preco do seu produto:"))
    InfProduct.Qdemestoque=int(input("Digite a quantidade de produto:"))
    vectproduct.append(InfProduct)
    quest=False
    while True:
        question=str(input("deseja continuar?: yes/No:"))
        question=question.lower()
        if question=="yes":
            quest=True
        else:
            quest=False
        break
    if quest==False:
        break    


print("\nRelatório dos produtos:") 
print("============================================================================")   
for prod in vectproduct:
    print("Codigo:",prod.codigo)
    print("Nome:",prod.Nome)
    print("preco:",prod.Preco)
    print("Quantidade em estoque:",prod.Qdemestoque)

print("*****************************************************************************")
print("Atualização dos produtos")
listDosPrdAtualizados=[]
while True:
    Cprod=int(input("digite o codigo do produto:")) 
    if Cprod==0: #digite 0 se quiser encerrar o programa
        break
    for prodt in vectproduct:
        if prodt.codigo ==Cprod:
            achar=True
            prodt.Preco=float(input("digite o novo preco:"))
            prodt.Qdemestoque=int(input("digite a nova quantidade:"))
            listDosPrdAtualizados.append(prodt)
    if achar==False:        
            print("ouppsss erro! voce digitou um codigo diferente!!!")           
  

print("**************************************************************")
print("deseja comprar umas coisas?")
#inicio das compras
listadosProdutosComprados=[]
precoQdComprarVariasPrd=[]#vector que recebe a lista dos produtos comprados
while True:
    found = False
    codDoProduto=int(input("digite o codigo:"))
    if codDoProduto == -1: #para encerrar o programa
        break
    
    for prod in listDosPrdAtualizados:
        if prod.codigo==codDoProduto:
            found = True
            QdAsercomprada=int(input("quantos produtos que deseja comprar?:"))
            if  QdAsercomprada<=prod.Qdemestoque:
                prod.Qdemestoque-=QdAsercomprada
                prod.qdcompr=QdAsercomprada# variavel que recebe a quantidade comprada
                listadosProdutosComprados.append(prod)
            else:
                print(f"voce digitou uma quantidade maior do que esta disponivel! quantidade={prod.Qdemestoque}")    
    if found == False:
        print("ouppss! ocorreu um erro na sua compra voce digitou um codigo errado!!!")

print("=========================================================================================")        
print("CUPOM DOS PRODUTOS COMPRADOS")     
      
print("Impressão das compras") 
print("codigo               Nome                Preco               quantidade")
print("<<<<<<<<<<<....................................................................>>>>>>>>>>>>")
precoG=[]#preco geral
precoT=0    
for prC in listadosProdutosComprados:    # prC lista dos produtos comprados
    print(prC.codigo,"              ",prC.Nome,"                ", prC.Preco, "              ",prC.qdcompr) 
    preco=prC.Preco*prC.qdcompr
    precoT+=preco
precoG.append(precoT)
for C in precoG:
    print("TOTAL=",C) 

print("Compra finalizada com sucesso!! obrigado!")     
print("Fim da mpressão das compras") 

#procurando produtos via codigo
print("******************************************************************************")
print("voce quer procurar um produto via o seu codigo?")
while True:
    verificacao=False
    seachforProd=int(input("digite o codigo do produto:"))
    if seachforProd==-2:# digite -2 se voce quer encerrar o programa
        break
    for prd in vectproduct:
        if prd.codigo == seachforProd:
            verificacao=True
            print("Codigo:",prd.codigo)
            print("Nome:",prd.Nome)
            print("Preco:",prd.Preco)
            print("Quantidade:",prd.Qdemestoque)
    if verificacao==False:
        print("o produto que voce digito nao foi cadastrado")

#impressão de todos os produtos 
print("===============================================================================")
print("Lista dos produtos cadastrados")
print("\nRelatório dos produtos:") 
for p in vectproduct:# ou for p in listDosPrdAtualizados se vc quer dar im print nos produtos atualizados
    print("Codigo:",p.codigo)
    print("Nome:",p.Nome)
    print("preco:",p.Preco)
    print("Quantidade em estoque:",p.Qdemestoque) 
    print("****************************************************************") 