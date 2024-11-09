
# Karyotype Analyzer

Este software automatiza a análise citogenética de cariótipos humanos, empregando inteligência artificial (IA) para identificar e classificar aberrações cromossômicas.

## Passo a Passo para Instalação e Uso

### 1. Instalação do Python

1. Acesse o site oficial do Python: https://www.python.org/downloads/
2. Baixe a versão mais recente do Python 3 (3.7 ou superior)
3. Execute o instalador e siga as instruções na tela
   - Importante: Marque a opção "Add Python to PATH" durante a instalação

### 2. Baixar o Projeto

1. Acesse https://github.com/ezrafchev/karyotype-analyzer
2. Clique no botão verde "Code"
3. Selecione "Download ZIP"
4. Extraia o arquivo ZIP para uma pasta de sua escolha

### 3. Instalar Dependências

1. Abra o Prompt de Comando (Windows) ou Terminal (Mac/Linux)
2. Navegue até a pasta do projeto extraído:
   ```
   cd caminho/para/karyotype-analyzer
   ```
3. Instale as dependências com o comando:
   ```
   pip install -r requirements.txt
   ```

### 4. Executar o Programa

1. Na mesma janela do Prompt de Comando ou Terminal, execute:
   ```
   python main.py
   ```
2. A interface gráfica do programa será aberta

### 5. Usar o Programa

1. Na interface, insira um ID para a amostra (por exemplo, "Amostra001")
2. Clique no botão "Analyze Sample"
3. Escolha um local e nome para salvar o arquivo de resultados JSON
4. Aguarde a análise ser concluída
5. Os resultados serão salvos no arquivo JSON escolhido
6. Uma imagem dos cromossomos segmentados será salva no mesmo diretório

## Estrutura do Projeto

- `main.py`: Arquivo principal para executar a aplicação
- `karyotype_analyzer.py`: Contém a lógica de análise de cariótipos
- `lab_integration.py`: Simula a integração com robôs laboratoriais
- `gui.py`: Implementa a interface gráfica do usuário

## Suporte

Se encontrar problemas ou tiver dúvidas, por favor, abra uma issue no GitHub do projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
