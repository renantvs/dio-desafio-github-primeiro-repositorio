# Código Sistema de Recomendação de Cursos
# INÍCIO
nome = input('Como deseja ser chamado(a)?\n') 
print(f'Olá, {nome}! Temos diversos temas legais para você, aproveite! :)')

categorias = ["Introdução ao Wordpress", 
              "Google Ads", 
              "E-commerce na Prática", 
              "Design Gráfico", 
              "Programação", 
              "Criação de Conteúdo", 
              "Marketing Digital", 
              "Youtube", 
              "Negócios", 
              "Vendas com WhatsApp Business",
              "Criação de Sites",
              "Afiliado de Sucesso", 
              "Desenvolvimento de Plugins para Wordpress", 
              "Canva: Design fácil para Empreendedores"]

for i in range(len(categorias)):
  
 print(f'{i}. {categorias[i]}')

num_das_categorias = input(
    'Digite o número dos assuntos de seu interesse (utilize vírgulas):\n'
    )

tempo = float (input("Quanto tempo gostaria de estudar? (min)\n"))

mostrar_premium = input("Mostrar cursos Premium (S/N)?\n")


print(type(nome))
print(type(num_das_categorias))
print(type(tempo))
print(type(mostrar_premium))

if mostrar_premium == 'N' or mostrar_premium == 'n':
  mostrar_premium = False
else:
  mostrar_premium = True

num_das_categorias = num_das_categorias.split(",")
ncategorias = []
for elemento in num_das_categorias:
  numero = int(elemento.strip())
  ncategorias.append(numero)

print(ncategorias)

print(f'Nome: {nome}')
print(f'ID das Categorias: {ncategorias}')
print(f'Tempo: {tempo}')
print(f'Mostrar Premium?: {mostrar_premium}')


cursos = ["Introdução ao Wordpress", 
          "Google Ads", 
          "E-Commerce na Prática", 
          "Design Gráfico", 
          "Programação", 
          "Criação de Conteúdo", 
          "Marketing Digital", 
          "Youtube", 
          "Negócios", 
          "Vendas com WhatsApp Business", 
          "Criação de Sites",
          "Afiliado de Sucesso", 
          "Desenvolvimento de Plugins para Wordpress", 
          "Canva: Design fácil para Empreendedores"
          ]

tempos = [95,
          25,
          40,
          85,
          75,
          150,
          140,
          120,
          85,
          335,
          160,
          70,
          145,
          110,]

categorias_dos_cursos = [
                         ['wordpress', 'criação de sites'],
                         ['marketing digital','vendas'], 
                         ['e-commerce', 'criação de sites', 'wordpress'], 
                         ['design', 'marketing digital'], 
                         ['criação de sites', 'vendas', 'google ads'], 
                         ['google ads', 'marketing digital'], 
                         ['marketing digital', 'e-commerce', 'vendas', 'negócios'], 
                         ['youtube', 'google ads', 'design', 'negócios'], 
                         ['negócios', 'criação de sites', 'google ads'], 
                         ['vendas', 'negocios', 'google ads', 'criação de sites'],
                         ['criação de sites', 'negócios', 'wordpress'], 
                         ['vendas', 'negócios'],
                         ['programação', 'criação de sites'], 
                         ['design, negócios', 'vendas'],                      
                        ]          
gratuidade = [True,
              False,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              False,
              False]



categorias_selecionadas = []
for n in ncategorias:
  categorias_selecionadas.append(categorias[n].upper())

print(categorias_selecionadas)


print(f"Olá, {nome}! Com base no seu perfil, achamos que você iria gostar dos seguintes cursos:")
for cat in categorias_selecionadas: 
 print (f"{cat}:")
 for linha in range(len(cursos)):
  if gratuidade[linha] or mostrar_premium:
   if (cat.lower() in categorias_dos_cursos[linha]
       and tempos[linha] <= tempo):
     print(f"- {cursos[linha]} ({tempos[linha]} min)") 