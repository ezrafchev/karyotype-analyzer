# Karyotype Analyzer

Este software automatiza a análise citogenética de cariótipos humanos, empregando técnicas de processamento de imagem para identificar e classificar possíveis aberrações cromossômicas.

## Requisitos do Sistema

- Windows 10 ou superior (também compatível com Linux e macOS)
- Python 3.7 ou superior (recomendado: Python 3.12)
- Conexão com a internet para baixar as dependências

## Instalação e Configuração

1. **Instale o Python:**
   - Baixe e instale Python 3.12 do [site oficial](https://www.python.org/downloads/).
   - Durante a instalação, marque a opção "Add Python to PATH".

2. **Baixe o Projeto:**
   - Clique no botão verde "Code" no topo desta página do GitHub.
   - Selecione "Download ZIP".
   - Extraia o arquivo ZIP para uma pasta de sua escolha.

3. **Prepare o Ambiente:**
   - Abra o Prompt de Comando (Windows) ou Terminal (Linux/macOS).
   - Navegue até a pasta do projeto:
     ```
     cd caminho/para/karyotype-analyzer
     ```

4. **Crie um Ambiente Virtual:**
   ```
   python -m venv venv
   ```

5. **Ative o Ambiente Virtual:**
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No Linux ou macOS:
     ```
     source venv/bin/activate
     ```

6. **Atualize o pip:**
   ```
   python -m pip install --upgrade pip
   ```

7. **Instale as Dependências:**
   ```
   pip install -r requirements.txt
   ```

## Preparação de Imagens de Amostra

1. Dentro da pasta do projeto, crie uma pasta chamada "samples" se ela ainda não existir.
2. Coloque suas imagens de cariótipos na pasta "samples".
   - Formatos suportados: .png, .jpg, .jpeg, .tiff, .bmp
   - Nomeie as imagens de forma descritiva, por exemplo: "amostra001.jpg", "paciente_xyz.png"

## Executando o Programa

Com o ambiente virtual ativado, execute:
```
python main.py
```

## Usando o Programa

1. A interface gráfica do programa será aberta.
2. Você verá uma lista das imagens de amostra disponíveis.
3. Clique no botão "Refresh Samples" se não vir suas imagens na lista.
4. Selecione a imagem que deseja analisar.
5. Clique no botão "Analyze Sample".
6. Escolha um local e nome para salvar o arquivo de resultados JSON.
7. Aguarde a análise ser concluída.
8. Os resultados serão salvos no arquivo JSON escolhido.
9. Uma imagem dos cromossomos segmentados será salva no mesmo diretório.

## Interpretação dos Resultados

- O arquivo JSON contém:
  - Timestamp da análise
  - Lista de possíveis anomalias detectadas
  - Dados detalhados sobre cada cromossomo identificado
- A imagem segmentada mostra os cromossomos identificados com cores diferentes para facilitar a visualização.

## Estrutura do Projeto

- `main.py`: Arquivo principal para executar a aplicação
- `karyotype_analyzer.py`: Contém a lógica de análise de cariótipos
- `gui.py`: Implementa a interface gráfica do usuário
- `requirements.txt`: Lista de dependências do projeto

## Solução de Problemas

- Se encontrar erros ao criar o ambiente virtual, certifique-se de que o Python está corretamente instalado e adicionado ao PATH do sistema.
- Em caso de problemas com a instalação de dependências, tente atualizar o setuptools:
  ```
  pip install --upgrade setuptools
  ```
- Se o programa não abrir, verifique se todas as dependências foram instaladas corretamente.
- Para problemas específicos com bibliotecas como OpenCV ou scikit-image, consulte a documentação oficial dessas bibliotecas.

## Desenvolvimento e Contribuição

- Para contribuir, faça um fork do repositório, crie uma branch para sua feature, e envie um pull request.
- Mantenha o código bem documentado e siga as boas práticas de programação em Python.
- Adicione testes para novas funcionalidades quando possível.

## Suporte

Se encontrar problemas ou tiver dúvidas:
1. Verifique as issues existentes no GitHub.
2. Se não encontrar uma solução, abra uma nova issue detalhando o problema.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Agradecimentos

Agradecemos a todos os contribuidores e à comunidade open-source pelas ferramentas e bibliotecas utilizadas neste projeto.
