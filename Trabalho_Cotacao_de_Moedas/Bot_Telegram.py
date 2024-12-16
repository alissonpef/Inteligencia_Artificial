from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

TELEGRAM_BOT_TOKEN = "7981119215:AAFKtXJMBnNzMHTft2g3qwr3tL5xU0ted9g"
EXCHANGE_RATE_API_KEY = "bf39c5f20ffb5302aa1754cd"
BASE_CURRENCY = "BRL"

# Função para buscar cotações com base na moeda base
def get_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/{BASE_CURRENCY}"
    response = requests.get(url)  # Faz uma requisição GET para a API
    if response.status_code == 200:
        return response.json().get('conversion_rates', {})  # Retorna as taxas de câmbio como um dicionário
    else:
        return None

# Função que lista todas as moedas disponíveis
async def listar_moedas(update: Update, context: CallbackContext):
    rates = get_exchange_rates()
    if rates:
        moedas = ', '.join(list(rates.keys()))  # Lista todas as moedas
        await update.message.reply_text(f"As moedas disponíveis são: {moedas}")
    else:
        await update.message.reply_text("Erro ao obter a lista de moedas.")

# Função que lista o preço de todas as moedas em relação a moeda base
async def listar_precos(update: Update, context: CallbackContext):
    rates = get_exchange_rates()
    if rates:
        precos = '\n'.join([f"1 {BASE_CURRENCY} = {rate:.2f} {moeda}" for moeda, rate in rates.items()])  # Formata os preços
        await update.message.reply_text(f"Preços das moedas em relação ao {BASE_CURRENCY}:\n\n{precos}")
    else:
        await update.message.reply_text("Erro ao obter os preços das moedas.")

# Função para obter a cotação de uma moeda específica em relação à moeda base
async def cotacao(update: Update, context: CallbackContext):
    rates = get_exchange_rates()
    if rates:
        currency = context.args[0].upper() if context.args else None  # Obtém a moeda passada pelo usuário
        if currency in rates:
            rate = rates[currency]
            await update.message.reply_text(f"A cotação atual de 1 {BASE_CURRENCY} para {currency} é: {rate:.2f}")
        else:
            await update.message.reply_text(f"Moeda {currency} não encontrada.")
    else:
        await update.message.reply_text("Erro ao obter a cotação.")

# Função para converter um valor de uma moeda para outra
async def converter(update: Update, context: CallbackContext):
    try:
        base_currency = context.args[0].upper()  # Moeda base
        target_currency = context.args[1].upper()  # Moeda alvo
        amount = float(context.args[2])  # Valor a ser convertido

        # Busca as taxas de câmbio
        rates = get_exchange_rates()
        if not rates or base_currency not in rates or target_currency not in rates:  # Verifica se as moedas são válidas e se elas foram obtidas
            await update.message.reply_text("Moedas não encontradas. Use /listar_moedas para ver as moedas disponíveis.")
            return

        # Calcula a conversão
        if base_currency == BASE_CURRENCY:  # Se a moeda base for a mesma do bot
            converted_amount = amount * rates[target_currency]
        else:
            moeda_to_base = 1 / rates[base_currency]  # Converte para a moeda base do bot
            converted_amount = amount * moeda_to_base * rates[target_currency] 

        await update.message.reply_text(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    except (IndexError, ValueError):
        await update.message.reply_text("Uso correto: /converter [MOEDA_BASE] [MOEDA_ALVO] [VALOR]")

# Função para configurar a moeda base
async def configurar_base(update: Update, context: CallbackContext):
    global BASE_CURRENCY
    try:
        nova_base = context.args[0].upper()  # Obtém a nova moeda base
        BASE_CURRENCY = nova_base
        await update.message.reply_text(f"Moeda base configurada para {nova_base}.")
    except (IndexError, ValueError):
        await update.message.reply_text("Uso correto: /configurar_base [MOEDA]")

# Função de início do bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Olá! Eu sou o bot de cotações de moedas. Use os seguintes comandos:\n"
        "/listar_moedas - Lista todas as moedas disponíveis.\n"
        "/precos - Mostra o preço de todas as moedas em relação a moeda base.\n"
        "/cotacao [MOEDA] - Mostra a cotação de uma moeda específica em relação a moeda base\n"
        "/converter [MOEDA_BASE] [MOEDA_ALVO] [VALOR] - Converte um valor de uma moeda para outra.\n"
        "/configurar_base [MOEDA] - Configura a moeda base para todas as operações.\n"
    )

def main():
    # Configuração do bot com o token usando Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Configuração dos comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("listar_moedas", listar_moedas))
    application.add_handler(CommandHandler("precos", listar_precos))
    application.add_handler(CommandHandler("cotacao", cotacao))
    application.add_handler(CommandHandler("converter", converter))
    application.add_handler(CommandHandler("configurar_base", configurar_base))

    # Inicia o bot
    application.run_polling()

if __name__ == "__main__":
    main()

