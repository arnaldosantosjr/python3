import re

# Dicionário de aliases para emojis
emoji_aliases = {
    ':smiley:': '\U0001F603',
    ':heart:': '\U00002764',
    # Adicione mais aliases e seus códigos Unicode conforme necessário
}

def substituir_aliases_por_emoji(texto, aliases):
    padrao = '|'.join(re.escape(alias) for alias in aliases)
    return re.sub(padrao, lambda match: aliases[match.group(0)], texto)

mensagem = 'Olá, mundo! :smiley: :heart:'
mensagem_com_emoji = substituir_aliases_por_emoji(mensagem, emoji_aliases)

print(mensagem_com_emoji)