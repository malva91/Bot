pip install telebot

import telebot

API_TOKEN = '2129627912:AAF7SWe9K6vv26muU41TcvXlWTj2abTHkeg'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    bot.reply_to(
        message, 'Ciao, di che appartamento hai bisogno?\n\nPuoi scrivere il nome o il codice, con "Lista" avrai la lista completa degli appartamenti')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    if message.text == 'Bovio' or message.text == 'bovio' or message.text == 'PIPSIF546' or message.text == '546':
        bot.reply_to(message, 'Indirizzo:\nViao Giovanni Bovio, 9,Pisa\n\nNome:\nVia Bovio\n\nCodice:\nPIPSIF546\n\nComposizione:\n1 Matrimoniale\n1 Singola\n1 Bagno\n1 Cucina\n\nNote:\nNOI ABBIAMO CHIAVE DEL PTONE QUELLA DELL APPARTAMENTO è NEL PTA OMBRELLO')


    elif message.text == 'Segromigno' or message.text == 'segromigno':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nGirasole\n\nCodice:\nLUSIMF1081\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' + 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nGirasole\n\nCodice:\nLUSIMF1081\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' +  'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nHibiscus\n\nCodice:\nLUSIMF1082\n\nComposizione:\n1 Matrimoniale\n2 Singoli (fatti a divano in cucina)\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' +   'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nIris\n\nCodice:\nLUSIMF1083\n\nComposizione:\n1 Matrimoniale KING\n3 Singoli\n2 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' +  'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nOrchidea\n\nCodice:\nLUSIMF1084\n\nComposizione:\n1 Matrimoniale KING\n2 Singoli\n2 Bagno\n1 Cucina\n\nNote:\n'  + '\n\n------------------------------\n\n' +   'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nRosmarino\n\nCodice:\nLUSIMF1085\n\nComposizione:\n3 Matrimoniale\n2 Bagno\n1 Cucina\n\nNote:\n'  + '\n\n------------------------------\n\n' +    'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nRosa\n\nCodice:\nLUSIMF1086\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Girasole' or message.text == 'girasole' or message.text == 'LUSIMF1081' or message.text == '1081':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nGirasole\n\nCodice:\nLUSIMF1081\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Hibiscus' or message.text == 'hibiscus' or message.text == 'LUSIMF1082' or message.text == '1082':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nHibiscus\n\nCodice:\nLUSIMF1082\n\nComposizione:\n1 Matrimoniale\n2 Singoli (fatti a divano in cucina)\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Iris' or message.text == 'iris' or message.text == 'LUSIMF1083' or message.text == '1083':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nIris\n\nCodice:\nLUSIMF1083\n\nComposizione:\n1 Matrimoniale KING\n3 Singoli\n2 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Orchidea' or message.text == 'orchidea' or message.text == 'LUSIMF1084' or message.text == '1084':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nOrchidea\n\nCodice:\nLUSIMF1084\n\nComposizione:\n1 Matrimoniale KING\n2 Singoli\n2 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Rosmarino' or message.text == 'rosmarino' or message.text == 'LUSIMF1085' or message.text == '1085':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nRosmarino\n\nCodice:\nLUSIMF1085\n\nComposizione:\n3 Matrimoniale\n2 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Rosa' or message.text == 'rosa' or message.text == 'LUSIMF1086' or message.text == '1086':
        bot.reply_to(message, 'Indirizzo:\nVia delle Selvette, 233, 55018, Capanni, Lucca\n\nNome:\nRosa\n\nCodice:\nLUSIMF1086\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Pisano' or message.text == 'pisano' or message.text == 'PIPSIF464' or message.text == '464':
        bot.reply_to(message, 'Indirizzo:\nViale Giovanni Pisano, 10, Pisa\n\nNome:\nVia Pisano\n\nCodice:\nPIPSIF464\n\nComposizione:\n1 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Puccini' or message.text == 'puccini' or message.text == 'LUVRGF747' or message.text == '747':
        bot.reply_to(message, 'Indirizzo:\nVia Giacomo Puccini, 151, Viareggio\n\nNome:\nVia Puccini\n\nCodice:\nLUVRGF747\n\nComposizione:\n2 Matrimoniale\n2 Divano Letto\n2 Singoli\n2 Bagno\n1 Cucina\n\nNote:\nABBIAMO LA CHIAVE DEL PORTONE MENTRE DELLA CASA è NEL PORTA OMBRELLO')

    elif message.text == 'Ville' or message.text == 'ville' or message.text == 'LUMSGF997' or message.text == '997':
        bot.reply_to(message, 'Indirizzo:\n/\n\nNome:\nVia delle Ville\n\nCodice:\nLUMSGF997\n\nComposizione:\n2 Matrimoniale\n2 Divano Letto\n2 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Alessio' or  message.text == 'alessio' or message.text == 'LULCCF433' or message.text == '433':
        bot.reply_to(message, 'Indirizzo:\nVia di Sant Alessio, 25, Lucca\n\nNome:\nVia di Sant Alessio\n\nCodice:\nLULCCF433\n\nComposizione:\n2 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Antonio' or  message.text == 'antonio' or message.text == 'PIPSIF1102' or message.text == '1102':
        bot.reply_to(message, 'Indirizzo:\nVia di Sant Antonio, 6, Pisa\n\nNome:\nVia di Sant Antonio\n\nCodice:\nPIPSIF1102\n\nComposizione:\n2 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')


    elif message.text == 'Mancini' or  message.text == 'mancini' or message.text == 'LULCCF686' or message.text == '686':
        bot.reply_to(message, 'Indirizzo:\nVia Augusto Mancini, 49, Lucca\n\nNome:\nVia Mancini\n\nCodice:\nLULCCF686\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\nLE CHIAVI SONO NELLA CASSETTA DELLA POSTA')

    elif message.text == 'Gagno Green' or  message.text == 'gagno green' or message.text == 'Gagno green' or message.text == 'gagno Green'or  message.text == 'Gagno Verde' or message.text == 'gagno verde' or message.text == 'Gagno verde' or message.text == 'gagno Verde' or message.text == 'PIPSIF720' or message.text == '720':
        bot.reply_to(message, 'Indirizzo:\nVia di Gagno, 50, Pisa (Primo piano)\n\nNome:\nGagno verde\n\nCodice:\nPIPSIF720\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Gagno Blu' or  message.text == 'gagno blu' or message.text == 'Gagno blu' or message.text == 'gagno Blu'or message.text == 'PIPSIF719' or message.text == '719':
        bot.reply_to(message, 'Indirizzo:\nVia di Gagno, 50, Pisa (Secondo piano)\n\nNome:\nGagno blu\n\nCodice:\nPIPSIF719\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Gagno Yellow' or  message.text == 'gagno yellow' or message.text == 'Gagno yellow' or message.text == 'gagno Yellow'or  message.text == 'Gagno Giallo' or message.text == 'gagno giallo' or message.text == 'Gagno giallo' or message.text == 'gagno Giallo' or message.text == 'PIPSIF1096' or message.text == '1096':
        bot.reply_to(message, 'Indirizzo:\nVia di Gagno, 50, Pisa (Penultimo piano)\n\nNome:\nGagno giallo\n\nCodice:\nPIPSIF1096\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Gagno Red' or  message.text == 'gagno red' or message.text == 'Gagno red' or message.text == 'gagno Red'or  message.text == 'Gagno Rosso' or message.text == 'gagno rosso' or message.text == 'Gagno rosso' or message.text == 'gagno Rosso' or message.text == 'PIPSIF721' or message.text == '721':
        bot.reply_to(message, 'Indirizzo:\nVia di Gagno, 50, Pisa (Ultimo piano)\n\nNome:\nGagno rosso\n\nCodice:\nPIPSIF721\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')


    elif message.text == 'Gagno' or  message.text == 'gagno':
        bot.reply_to(message, 'Indirizzo:\nVia di Gagno, 50, Pisa (Primo piano)\n\nNome:\nGagno verde\n\nCodice:\nPIPSIF720\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' + 'Indirizzo:\nVia di Gagno, 50, Pisa (Secondo piano)\n\nNome:\nGagno blu\n\nCodice:\nPIPSIF719\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' + 'Indirizzo:\nVia di Gagno, 50, Pisa (Penultimo piano)\n\nNome:\nGagno giallo\n\nCodice:\nPIPSIF1096\n\nComposizione:\n1 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' + 'Indirizzo:\nVia di Gagno, 50, Pisa (Ultimo piano)\n\nNome:\nGagno rosso\n\nCodice:\nPIPSIF721\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')


    elif message.text == 'Lenze totale' or  message.text == 'lenze totale' or message.text == 'PIPSIF1031' or message.text == '1031':
        bot.reply_to(message, 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze TOTALE\n\nCodice:\nPIPSIF1031\n\nComposizione:\n3 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Lenze pt' or message.text == 'lenze pt' or message.text == 'PIPSIF1032' or message.text == '1032':
        bot.reply_to(message, 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PIANO TERRA\n\nCodice:\nPIPSIF1032\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Lenze 1p' or message.text == 'lenze 1p' or message.text == 'PIPSIF1033' or message.text == '1033':
        bot.reply_to(message, 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PRIMO PIANO\n\nCodice:\nPIPSIF1033\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Lenze 1pt' or message.text == 'lenze 1pt' or message.text == 'PIPSIF1034' or message.text == '1034':
        bot.reply_to(message, 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PRIMO PIANO CON TERRAZZO\n\nCodice:\nPIPSIF10334\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Lenze' or message.text == 'lenze':
        bot.reply_to(message,'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze TOTALE\n\nCodice:\nPIPSIF1031\n\nComposizione:\n3 Matrimoniale\n1 Bagno\n1 Cucina\n\nNote:\n' + '\n\n------------------------------\n\n' +'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PIANO TERRA\n\nCodice:\nPIPSIF1032\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n'+ '\n\n------------------------------\n\n' + 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PRIMO PIANO CON TERRAZZO\n\nCodice:\nPIPSIF10334\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n'+ '\n\n------------------------------\n\n' + 'Indirizzo:\nVia delle Lenze, 122, 56122 Pisa\n\nNome:\nVia delle Lenze PRIMO PIANO\n\nCodice:\nPIPSIF1033\n\nComposizione:\n2 Matrimoniale\n1 Divano Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Fachini' or message.text == 'facchini' or message.text == 'PIPSIF635' or message.text == '635':
        bot.reply_to(message, 'Indirizzo:\nVia dei Facchini, 10, Pisa\n\nNome:\nVia Facchini\n\nCodice:\nPIPSIF635\n\nComposizione:\n1 Matrimoniale\n1(2) Sigoli a castello\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Vico' or message.text == 'vico' or message.text == 'LUFRTF468' or message.text == '468':
        bot.reply_to(message, 'Indirizzo:\nVia dei Facchini, 10, Pisa\n\nNome:\nVia Facchini\n\nCodice:\nLUFRTF468\n\nComposizione:\n2 Matrimoniale\n1 Sigolo\n1 Poltrola Letto\n1 Bagno\n1 Cucina\n\nNote:\n')

    elif message.text == 'Cisanello' or message.text == 'cisanello'or message.text == '1106' or message.text == 'PIPSIF1106':
        bot.reply_to(message, 'Indirizzo:\nVia Luigi Pera ,14, Pisa\n\nNome:\nCisanello\n\nCodice:\nPIPSIF1106\n\nComposizione:\n\n\n\n\n\n\nNote:\n')


    elif message.text == 'Lista' or message.text == 'lista':
        bot.reply_to(message, '- Bovio\n- Antonio\n- Segromigno(Totatale)\n- Girasole\n- Hibiscus\n- Iris\n- Orchidea\n- Rosmarino\n- Rosa\n- Pisano\n- Puccini\n- Ville\n- Alessio\n- Mancini\n- Gagno verde\n- Gagno blu\n- Gagno giallo\n- Gagno rosso\n- Gagno(mostra tutti i gagno)\n- lenze totale\n- Lenze pt\n- Lenze 1p\n- Lenze 1pt\n- Lenze(Mostra tutto Lenze\n- Facchini\n- Vico')




    else:
        bot.reply_to(message, 'Non riconosco l appartamento')


bot.infinity_polling()
