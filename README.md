# Monitor de Desempenho - TMA (Tempo Médio de Atendimento)

Este é um projeto pessoal desenvolvido para me ajudar a monitorar meu desempenho no trabalho, especificamente em relação ao **TMA (Tempo Médio de Atendimento)**. A empresa onde trabalho estabelece uma meta de TMA, e este script me auxilia a calcular se estou dentro da média desejada e quantos atendimentos rápidos são necessários para atingir a meta.

---

## Como funciona

O script faz o seguinte:

1. **Seleciona um arquivo**: O usuário seleciona um arquivo Excel (`.xlsx`) ou CSV (`.csv`) contendo os tempos de atendimento.
2. **Calcula o TMA atual**: O script calcula a média dos tempos de atendimento.
3. **Compara com a meta**: Verifica quantos atendimentos estão abaixo do TMA desejado (18 minutos e 50 segundos).
4. **Sugere melhorias**: Se o TMA atual estiver acima da meta, o script calcula quantos atendimentos rápidos (abaixo de 17 minutos) são necessários para atingir a média desejada. (Ainda em desenvolvimento, pois o tempo de cada atendimento varia, não trazendo uma quantidade exata de quanto ainda precisa).

---

## Como usar

### Pré-requisitos
- Python 3.9+ instalado.
- Bibliotecas necessárias: `pandas` e `tkinter`.

Instale as dependências com:
```bash
pip install pandas
Executando o script
Clone este repositório ou baixe o arquivo .py.

Execute o script com:

bash
Copiar
Editar
python calcular_tma.py
Selecione um arquivo Excel ou CSV contendo os tempos de atendimento (um tempo por linha, no formato HH:MM:SS).

O script exibirá:

O TMA atual.
Quantos atendimentos estão abaixo da meta.
Quantos atendimentos rápidos são necessários para atingir a meta (se aplicável).
Exemplo de arquivo de entrada
Um arquivo Excel ou CSV deve conter uma coluna, sem cabeçalho, com os tempos de atendimento no formato HH:MM:SS. Exemplo:

Tempo
00:15:30
00:19:10
00:17:45
00:20:00
Resultados esperados
Ao executar o script com o arquivo acima, você verá algo como:

Média TMA atual: 18m11s
Atendimentos abaixo do TMA desejado (18min50seg): 3
Você precisa de 2 atendimentos abaixo de 17m para atingir a média desejada de 18m50s. (Esse cálculo pode conter erros)
Licença
Este projeto é pessoal e não está associado à empresa onde trabalho. Sinta-se à vontade para usar, modificar e distribuir conforme a licença MIT.


MIT License
Contribuições
Este projeto foi criado para fins pessoais, mas se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Contato
Se tiver dúvidas ou quiser entrar em contato, você pode me encontrar no [LinkedIn](https://www.linkedin.com/in/marianapacini-dataengineer/).

Nota: Este script foi desenvolvido para uso pessoal e pode conter erros ou limitações, pois ainda se encontra em desenvolvimento. Use por sua própria conta e risco.