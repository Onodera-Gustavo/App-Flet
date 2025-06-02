import json
import os

def escolher_caminho(caminho: str) -> str:
    """Escolhe o caminho do arquivo"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    if caminho == "Candidato":
        return os.path.join(BASE_DIR, "../assets/arquivos/candidatos.json")
    if caminho == "Aluno":
        return os.path.join(BASE_DIR, "../assets/arquivos/alunos.json")
    if caminho == "Proposta":
        return os.path.join(BASE_DIR, "../assets/salvamentos/propostas.json")
    
    raise ValueError(f"Tipo de caminho inválido: {caminho}")

def carregar_candidatos(caminho: str) -> list:
    """Carrega os dados do arquivo"""
    ARQUIVO = escolher_caminho(caminho=caminho)
    
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    
    # Se o arquivo não existe, cria com lista vazia
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    
    # Tenta carregar o arquivo
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # Se o arquivo estiver corrompido, recria
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

def salvar_candidatos(informacoes: list, caminho: str):
    """Salva os dados no arquivo"""
    ARQUIVO = escolher_caminho(caminho=caminho)
    
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    
    # Salva os dados formatados
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(informacoes, f, ensure_ascii=False, indent=4)

def atualizar(nome: str, numero_identificacao: str, caminho: str):
    """Atualiza os dados do aluno ou candidato"""
    
    informacoes = carregar_candidatos(caminho=caminho)
    
    for item in informacoes:
        if (item.get("matricula") == numero_identificacao or 
            str(item.get("Numero Eleitoral", "")) == numero_identificacao):
            if "votou" in item:  # Para alunos
                item["votou"] = True
                item["nome"] = nome  # Atualiza o nome se necessário
            elif "Votos" in item:  # Para candidatos
                item["Votos"] = item.get("Votos", 0) + 1
    
    salvar_candidatos(informacoes, caminho=caminho)