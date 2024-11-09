
# Karyotype Analyzer

Este software automatiza a análise citogenética de cariótipos humanos, empregando técnicas de processamento de imagem para identificar e classificar possíveis aberrações cromossômicas.

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

### 4. Preparar Imagens de Amostra

1. Dentro da pasta do projeto, crie uma pasta chamada "samples" se ela ainda não existir
2. Coloque suas imagens de cariótipos na pasta "samples"
   - Formatos suportados: .png, .jpg, .jpeg, .tiff, .bmp
   - Nomeie as imagens de forma descritiva, por exemplo: "amostra001.jpg", "paciente_xyz.png"

### 5. Executar o Programa

1. Na mesma janela do Prompt de Comando ou Terminal, execute:
   ```
   python main.py
   ```
2. A interface gráfica do programa será aberta

### 6. Usar o Programa

1. Na interface, você verá uma lista das imagens de amostra disponíveis
2. Clique no botão "Refresh Samples" se não vir suas imagens na lista
3. Selecione a imagem que deseja analisar
4. Clique no botão "Analyze Sample"
5. Escolha um local e nome para salvar o arquivo de resultados JSON
6. Aguarde a análise ser concluída
7. Os resultados serão salvos no arquivo JSON escolhido
8. Uma imagem dos cromossomos segmentados será salva no mesmo diretório

## Estrutura do Projeto

- `main.py`: Arquivo principal para executar a aplicação
- `karyotype_analyzer.py`: Contém a lógica de análise de cariótipos
- `gui.py`: Implementa a interface gráfica do usuário

## Interpretação dos Resultados

O arquivo JSON de resultados conterá:
- Timestamp da análise
- Lista de possíveis anomalias detectadas
- Dados detalhados sobre cada cromossomo identificado

A imagem segmentada mostrará os cromossomos identificados com cores diferentes para facilitar a visualização.

## Suporte

Se encontrar problemas ou tiver dúvidas, por favor, abra uma issue no GitHub do projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
