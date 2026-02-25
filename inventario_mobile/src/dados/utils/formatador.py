from datetime import datetime
import re

def gerar_texto_whatsapp(turno, conferente, inventario):
    data_atual = datetime.now().strftime("%d, %m, %Y, %H:%M")
    
    
    texto_final = f"Relatório de Inventário\nTurno: {turno}\nConferente: {conferente}\n Data: {data_atual}\n"
    
   
    for categoria, produtos in inventario.items():
        if produtos:
            texto_final += f"\n*{categoria}*\n"
            total_categoria = 0
            for nome, qtd in produtos.items():
                texto_final += f" - {nome}: {qtd}\n"
                try:

                    numeros_encontrados = re.findall(r'\d+', qtd)
                    soma_numeros = sum(int(n)for n in numeros_encontrados)
                    total_categoria += soma_numeros
                except(ValueError, IndexError):
                    pass
                    

            texto_final += f"Total {categoria}: {total_categoria}\n"
            texto_final+= "-----------------------------\n"

    return texto_final