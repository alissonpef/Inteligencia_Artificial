# Bot de Cotações de Moedas

Este é um bot do Telegram que permite ao usuário listar moedas, verificar suas cotações em relação a moeda base, converter valores entre moedas e alterar a moeda base para conversões.

## Funcionalidades

- **Listar Moedas**: Exibe todas as moedas suportadas pela API de taxas de câmbio.
- **Preços das Moedas**: Mostra o preço de todas as moedas em relação a moeda base.
- **Cotação de Moeda Específica**: Mostra a cotação de uma moeda específica em relação a moeda base.
- **Converter Moedas**: Converte um valor de uma moeda para outra.
- **Configurar Moeda Base**: Define uma moeda diferente da atual como base para todas as operações.

## Pré-requisitos

1. **Bibliotecas Necessárias**: Instale as bibliotecas necessárias usando o `pip`:
    ```bash
    pip install python-telegram-bot requests
    ```

2. **Versão do python-telegram-bot**: Este projeto foi desenvolvido com a versão 21.6 do `python-telegram-bot`. Se você estiver usando uma versão mais recente, pode ser necessário fazer algumas alterações no código. Para instalar uma versão específica, use o seguinte comando:
    ```bash
    pip install python-telegram-bot==21.6
    ```

3. **Credenciais**:
   - Um token do bot do Telegram (obtenha criando um bot no [BotFather](https://t.me/BotFather)).
   - Uma chave da API de taxas de câmbio (use o [ExchangeRate-API](https://www.exchangerate-api.com/)).

## Instalação

1. Substitua os valores de `TELEGRAM_BOT_TOKEN` e `EXCHANGE_RATE_API_KEY` com suas credenciais:
    ```python
    TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"
    EXCHANGE_RATE_API_KEY = "SUA_API_KEY_AQUI"
    ```

4. Execute o bot:
    ```bash
    python Bot.py
    ```

## Uso

Após iniciar o bot, você pode interagir com ele usando os seguintes comandos no Telegram:

### Comandos Disponíveis

- `/start`: Inicia o bot e exibe as instruções de uso.
- `/listar_moedas`: Lista todas as moedas disponíveis na API de cotações.
- `/precos`: Exibe o preço de todas as moedas em relação a moeda base.
- `/cotacao [MOEDA]`: Mostra a cotação de uma moeda específica em relação a moeda base. Exemplo:
    ```bash
    /cotacao USD
    ```
    Resposta: `A cotação atual de 1 BRL para USD é: 0.20 USD`.

- `/converter [MOEDA_BASE] [MOEDA_ALVO] [VALOR]`: Converte um valor de uma moeda para outra. Exemplo:
    ```bash
    /converter USD EUR 100
    ```
    Resposta: `100 USD = 85.00 EUR` (valores são apenas ilustrativos).

- `/configurar_base [MOEDA]`: Define uma moeda diferente da atual como moeda base. Exemplo:
    ```bash
    /configurar_base EUR
    ```

    Após configurar, todas as conversões e cotações usarão o Euro como moeda base.

## Exemplo de Uso

1. Inicie o bot enviando `/start`.
2. Para listar todas as moedas suportadas, envie `/listar_moedas`.
3. Para obter a cotação do dólar americano (USD) em relação a moeda base, envie `/cotacao USD`.
4. Para converter 50 euros (EUR) para dólares americanos (USD), envie `/converter EUR USD 50`.
5. Para definir o Euro como moeda base, envie `/configurar_base EUR`.
