# Karyotype Analyzer

Este software automatiza a análise citogenética de cariótipos humanos, empregando técnicas de processamento de imagem para identificar e classificar possíveis aberrações cromossômicas.

## Requisitos do Sistema

- Windows 10 ou superior
- Python 3.7 ou superior (recomendado: Python 3.12)
- Privilégios de administrador para instalar pacotes

## Instalação

1. Baixe e instale Python 3.12 do [site oficial](https://www.python.org/downloads/). Durante a instalação, marque a opção "Add Python to PATH".

2. Baixe este projeto:
   - Clique no botão verde "Code" no topo desta página
   - Selecione "Download ZIP"
   - Extraia o arquivo ZIP para uma pasta de sua escolha

3. Abra o PowerShell como administrador:
   - Clique com o botão direito no menu Iniciar
   - Selecione "Windows PowerShell (Admin)"

4. Navegue até a pasta do projeto:
   ```
   cd "C:\Caminho\Para\A\Pasta\karyotype-analyzer"
   ```
   Substitua o caminho pelo local onde você extraiu o arquivo ZIP.

5. Atualize o pip:
   ```
   python -m pip install --upgrade pip --user
   ```

6. Instale as dependências:
   ```
   pip install -r requirements.txt --user
   ```

## Preparação de Imagens de Amostra

1. Dentro da pasta do projeto, crie uma pasta chamada "samples" se ela ainda não existir.
2. Coloque suas imagens de cariótipos na pasta "samples".
   - Formatos suportados: .png, .jpg, .jpeg, .tiff, .bmp
   - Nomeie as imagens de forma descritiva, por exemplo: "amostra001.jpg", "paciente_xyz.png"

## Executando o Programa

1. No PowerShell, ainda na pasta do projeto, execute:
   ```
   python main.py
   ```
2. A interface gráfica do programa será aberta.

## Usando o Programa

1. Na interface, você verá uma lista das imagens de amostra disponíveis.
2. Clique no botão "Refresh Samples" se não vir suas imagens na lista.
3. Selecione a imagem que deseja analisar.
4. Clique no botão "Analyze Sample".
5. Escolha um local e nome para salvar o arquivo de resultados JSON.
6. Aguarde a análise ser concluída.
7. Os resultados serão salvos no arquivo JSON escolhido.
8. Uma imagem dos cromossomos segmentados será salva no mesmo diretório.

## Solução de Problemas

- Se encontrar erros de permissão ao instalar pacotes, tente adicionar a flag `--user` aos comandos pip.
- Certifique-se de que o Python está corretamente adicionado ao PATH do sistema.
- Se o programa não abrir, verifique se todas as dependências foram instaladas corretamente.

## Suporte

Se encontrar problemas ou tiver dúvidas, por favor, abra uma issue neste repositório GitHub.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
