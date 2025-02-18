import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import timedelta

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv")]
    )
    return arquivo

def ler_arquivo(arquivo):
    if arquivo.endswith(".xlsx"):
        df = pd.read_excel(arquivo, header=None)
    elif arquivo.endswith(".csv"):
        df = pd.read_csv(arquivo, header=None)
    else:
        print("Formato de arquivo não suportado.")
        return None
    return df

def converter_para_segundos(tempo):
    try:
        h, m, s = map(int, tempo.split(':'))
        return h * 3600 + m * 60 + s
    except ValueError:
        print(f"Formato de tempo inválido: {tempo}")
        return None

def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = int(segundos % 60)
    return f"{minutos}m{segundos_restantes}s"

def calcular_tma():
    arquivo = selecionar_arquivo()
    if not arquivo:
        print("Nenhum arquivo selecionado.")
        return
    
    df = ler_arquivo(arquivo)
    if df is None:
        return
    
    # Converter tempos para segundos e validar
    df['tempo_segundos'] = df[0].astype(str).apply(converter_para_segundos)
    if df['tempo_segundos'].isnull().any():
        print("Erro: Alguns tempos estão em formato inválido.")
        return
    
    # Calcular TMA atual
    tma_atual = df['tempo_segundos'].mean()
    tma_limite = converter_para_segundos("00:18:50")
    atendimentos_abaixo_tma = (df['tempo_segundos'] < tma_limite).sum()
    
    # Calcular quantos atendimentos abaixo de 17 minutos são necessários
    tempo_necessario = converter_para_segundos("00:17:00")
    if tma_atual > tma_limite:
        diferenca_total = (tma_atual - tma_limite) * len(df)
        atendimentos_necessarios = diferenca_total / (tma_limite - tempo_necessario)
        atendimentos_necessarios = int(atendimentos_necessarios) + 1
    else:
        atendimentos_necessarios = 0
    
    # Exibir resultados
    print(f"Média TMA atual: {formatar_tempo(tma_atual)}")
    print(f"Atendimentos abaixo do TMA desejado (18min50seg): {atendimentos_abaixo_tma}")
    if atendimentos_necessarios > 0:
        print(f"Você precisa de {atendimentos_necessarios} atendimentos abaixo de 17m para atingir a média desejada de 18m50s. (Esse cálculo pode conter erros)")
    else:
        print("A média já está dentro do desejado.")

calcular_tma()

input("\nPressione Enter para sair...")
