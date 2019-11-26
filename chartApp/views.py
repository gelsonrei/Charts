import random
from django.shortcuts import render
import json


def chart(request):
    
    graduacaoData = {}
    datasets = {}
    graduacaoData['labels'] = ["Básicas","Gerais","Eespecificas"]
    datasets['label'] = "Graduação"
    datasets['data'] =  [3,5,10,18]
    total = 3+5+10+18
    realizado = 3+5+10
    graduacaoData['centerTotal'] = str((realizado/total)*100)+"%"
    datasets['backgroundColor'] =  ["rgb(255, 99, 132)","rgb(0, 220, 0)","rgb(54, 162, 235)","rgb(255, 255, 255)"]
    graduacaoData['datasets'] = datasets 

    
    nomes = ["Diplomata", "Trader", "A. Negócios"]
    especializacoes = adicionaGrafico(nomes,["rgb(255, 183, 52)","rgb(255, 255, 255)",])
       
    
    nomes = ["Administração", "Contábeis"]
    duplaTitulacao = adicionaGrafico(nomes, ["rgb(225, 228, 35)","rgb(255, 255, 255)",])

    legendas = []
    it=0
    for ele in graduacaoData['labels']:
        legenda = {}
        legenda['label'] = ele
        legenda['color'] = datasets['backgroundColor'][it]
        it+=1
        legendas.append(legenda)
       
    
    context = {
        'graduacaoData': graduacaoData,
        'especializacoes': especializacoes,
        'duplaTitulacao' : duplaTitulacao,
        'legendas': legendas
    }
    
    return render(request, 'chart.html', context)

def especializacao(request):
    
    graduacaoData = {}
    datasets = {}
    graduacaoData['labels'] = ["Básicas","Gerais","Eespecificas"]
    datasets['label'] = "Graduação"
    datasets['data'] =  [3,5,10,18]
    total = 3+5+10+18
    realizado = 3+5+10
    graduacaoData['centerTotal'] = str((realizado/total)*100)+"%"
    datasets['backgroundColor'] =  ["rgb(64, 187, 97)","rgb(255, 183, 52)","rgb(29, 185, 192)","rgb(255, 255, 255)"]
    graduacaoData['datasets'] = datasets 

    
    nomes = ["Diplomata", "Trader", "A. Negócios"]
    especializacoes = adicionaGrafico(nomes,["rgb(255, 183, 52)","rgb(255, 255, 255)",])
       
    
    nomes = ["Administração", "Contábeis"]
    duplaTitulacao = adicionaGrafico(nomes, ["rgb(225, 228, 35)","rgb(255, 255, 255)",])

    legendas = []
    it=0
    for ele in graduacaoData['labels']:
        legenda = {}
        legenda['label'] = ele
        legenda['color'] = datasets['backgroundColor'][it]
        it+=1
        legendas.append(legenda)
       
    
    context = {
        'graduacaoData': graduacaoData,
        'especializacoes': especializacoes,
        'duplaTitulacao' : duplaTitulacao,
        'legendas': legendas
    }
    
    return render(request, 'rota_especializacao.html', context)

#gera valores aletórios para graficos N graficos 
def adicionaGrafico(nomes, cores):
    sz = len(nomes)
    graficos = []
  
    for i in range(sz):
        data = {}
        datasets = {}
        data['labels'] = ["%", "Restam %"]
        datasets['label'] = nomes[i]
        realizado = random.randrange(10, 100, 10)
        datasets['data'] =  [realizado, 100-realizado]
        data['centerTotal'] = str(realizado)+"%"
        datasets['backgroundColor'] =  cores
        data['datasets'] = datasets 
        graficos.append(data)
    
    return graficos
