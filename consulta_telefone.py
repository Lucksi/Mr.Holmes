import phonenumbers
from phonenumbers import carrier, geocoder

numero = input("Digite o número com DDD (ex: +55 92 99999-9999): ")

try:
    telefone = phonenumbers.parse(numero, "BR")

    if not phonenumbers.is_valid_number(telefone):
        print("\n❌ Número inválido.")
    else:
        regiao = geocoder.description_for_number(telefone, "pt-BR")
        operadora = carrier.name_for_number(telefone, "pt-BR")
        tipo = phonenumbers.number_type(telefone)

        tipos = {
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixo",
            phonenumbers.PhoneNumberType.MOBILE: "Celular",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixo ou celular",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Número pessoal",
            phonenumbers.PhoneNumberType.TOLL_FREE: "0800/Gratuito",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Tarifado",
            phonenumbers.PhoneNumberType.SHARED_COST: "Custo compartilhado",
            phonenumbers.PhoneNumberType.UAN: "UAN",
            phonenumbers.PhoneNumberType.VOICEMAIL: "Correio de voz",
            phonenumbers.PhoneNumberType.UNKNOWN: "Desconhecido",
        }

        print("\n📱 INFORMAÇÕES DO NÚMERO")
        print("-" * 35)
        print(f"Número: {phonenumbers.format_number(telefone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Região/DDD: {regiao or 'Não identificada'}")
        print(f"Operadora: {operadora or 'Não identificada'}")
        print(f"Tipo: {tipos.get(tipo, 'Desconhecido')}")

except phonenumbers.NumberParseException:
    print("\n❌ Não foi possível interpretar o número.")
