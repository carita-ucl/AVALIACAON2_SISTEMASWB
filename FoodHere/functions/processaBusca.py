from fila import filaBusca
import json


def processaBusca(termo):
    resultado = []

    try:
        
        with open("FoodHere/Dados/dadosRestaurante.json", "r") as arq:
            restaurantes = json.load(arq)

        
        for restaurante in restaurantes.get('restaurantes', []):  
            pratos = restaurante.get('pratos', [])
            cidade = restaurante.get('cidade', '')

            
            if termo in pratos and termo == cidade:
                resultado.append(restaurante['nome'])
    
        if resultado:
            return {
                    "status": 200,
                    "message": "Restaurantes encontrados com sucesso.",
                    "data": resultado
                }
        else:
            return {
                    "status": 404,
                    "message": "Nenhum restaurante encontrado com o prato ou cidade especificados.",
                    "data": []
                }

    except Exception as e:
        print(f"Erro ao processar a busca: {e}")
        return []