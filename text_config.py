import json

operator_number = "8-800-100-10-10"
help = "Телефон оператора: " + operator_number + " "
greeting = "Добрый день! Пожалуйста, выберите тип оказываемой услуги:"
phys = "Физическое лицо"
corp = "Юридическое лицо"
phys_service_list = "1) Найти отделения банка"
corp_service_list = "1) Найти отделения банка"
msg_unrec = "Извините, ваше сообщение нераспознано. Попробуйте воспользоваться кнопками команд."
dep_list = "Найти ближайшие отделения"
back = "Назад"
to_filters = "Фильтры поиска"
search_dep = "Поиск"
share_loc = "Поделиться локацией"

services = {3: {0: 'target_credit', 1: 'consumer_credit', 2: 'autocredit', 3: 'mortgage'},
 4: {0: 'payments_to_charities',
  1: 'payment_of_ip_telephony',
  2: 'payment_of_cellular_communication',
  3: 'payment_for_phone',
  4: 'payment_security_system',
  5: 'payment_of_commercial_tv',
  6: 'pay_for_internet_access',
  7: 'payment_for_communal_services',
  8: 'payment_for_education',
  9: 'payment_of_fines_stsi'},
 2: {0: 'deposit_rur', 1: 'deposit_eur', 2: 'deposit_usd'},
 1: {0: 'by_internet'},
 0: {0: 'eurocard_mastercard', 1: 'visa_international', 2: 'americanexpress'}}

service_categories = {0: 'issued_bank_cards',
 1: 'remote_service',
 2: 'currency_deposit',
 3: 'loans_private_individuals',
 4: 'additional_features'}


translationsENRU = {
    "target_credit":"Оформление целевого кредита",
    "consumer_credit":"Оформление потребительского кредита",
    "autocredit":"Оформление автомобильного кредита",
    "mortgage":"Оформление ипотечный кредит",
    "payments_to_charities":"Благотворительность",
    "payment_of_ip_telephony":"Оплата ip-телефонии",
    "payment_of_cellular_communication":"Оплата мобильной связи",
    "payment_for_phone":"Оплата телефона",
    "payment_security_system":"Оплата охранной системы",
    "payment_of_commercial_tv":"Оплата телевидения",
    "pay_for_internet_access":"Оплата интернета",
    "payment_for_communal_services":"Оплата коммунальных услуг",
    "payment_for_education":"Оплата обучения",
    "payment_of_fines_stsi":"Оплата штрафов",
    "deposit_rur":"Депозит в рублях",
    "deposit_eur":"Депозит в евро",
    "deposit_usd":"Депозит в долларах",
    "by_internet":"Удаленный сервис по интернету",
    "eurocard_mastercard":"Обслуживание Mastercard",
    "visa_international":"Обслуживание Visa",
    "americanexpress":"Обслуживание AmericanExpress",
    "issued_bank_cards":"Выпущенные банковские карты",
    "remote_service":"Удаленные сервисы",
    "currency_deposit":"Валютный депозит",
    "loans_private_individuals":"Займы частным лицам",
    "additional_features":"Дополнительные услуги",
    "Фильтры поиска":"Фильтры поиска",
    "Назад":"Назад"

}

translationsRUEN = {}
for key in translationsENRU:
    value = translationsENRU[key]
    translationsRUEN[value] = key
print(translationsRUEN)
filter_names = []

for category in services:
    for service in services[category].values():
        filter_names.append(service)
