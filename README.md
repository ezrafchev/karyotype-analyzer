
# Karyotype Analyzer

Este software automatiza a análise citogenética de cariótipos humanos, empregando inteligência artificial (IA) para identificar e classificar aberrações cromossômicas.

## Requisitos

- Python 3.7+
- OpenCV
- NumPy
- scikit-image
- matplotlib
- tkinter

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/karyotype-analyzer.git
   cd karyotype-analyzer
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Execute o programa principal:

```
python main.py
```

1. Insira o ID da amostra na interface gráfica.
2. Clique em "Analyze Sample".
3. Escolha um local para salvar o arquivo de resultados JSON.
4. Os resultados da análise serão salvos no arquivo JSON, e uma imagem dos cromossomos segmentados será salva no mesmo diretório.

## Estrutura do Projeto

- `main.py`: Arquivo principal para executar a aplicação.
- `karyotype_analyzer.py`: Contém a lógica de análise de cariótipos.
- `lab_integration.py`: Simula a integração com robôs laboratoriais.
- `gui.py`: Implementa a interface gráfica do usuário.

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue para discutir mudanças importantes antes de submeter um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
