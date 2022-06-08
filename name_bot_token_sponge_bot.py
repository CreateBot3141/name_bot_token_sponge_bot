

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import time
    import iz_func
    import iz_telegram    
    import datetime



    if message_in == 'Русский':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'/start','S',0)

    if message_in == 'English':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'/start','S',0)



    if message_in == '/start':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Выбор языка','S',0)
        
    if message_in == 'Отмена':
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ""

    if message_in == 'Вывод':
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод BNB')

    if status == 'Ввод BNB':
        iz_telegram.save_variable (user_id,namebot,"status",'')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Информация записана",'S',0) 
        status = ''
        login      = ""
        project    = "" 
        summ       = ""
        system     = ""
        wallet     = ""
        komment    = ""
        adress     = message_in
        telefon    = "" 
        db,cursor = iz_func.connect ()
        sql = "INSERT INTO bot_active_user (language,namebot,user_id,login,project,summ,`system`,wallet,komment,adress,telefon) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format ('ru',namebot,user_id,login,project,summ,system,wallet,komment,adress,telefon)
        cursor.execute(sql)
        db.commit() 

    if message_in == 'Баланс':
        message_out,menu = iz_telegram.get_message (user_id,'Текущий баланс',namebot)
        balans = iz_telegram.load_variable (user_id,namebot,'Баланс')
        if balans == '':
            balans = 0
        message_out = message_out.replace('%%ТекушийБаланс%%',str(balans)+" BNB")   
        #message_out = message_out.replace('%%Заявка%%',str(command))
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == 'Приглашений':
        message_out,menu = iz_telegram.get_message (user_id,'Всего приглашений',namebot)
        refer = 0
        db,cursor = iz_func.connect ()
        sql = "select id from bot_refer where namebot = '"+namebot+"' and user_id_refer = '"+str(user_id)+"'"
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id = row.values()
            refer = refer + 1
        message_out = message_out.replace('%%Приглашений%%',str(refer)+"")   
        #message_out = message_out.replace('%%Заявка%%',str(command))
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == 'Airdrop':        
        message_out,menu = iz_telegram.get_message (user_id,'Вывести задание',namebot)
        refer = iz_telegram.load_variable (user_id,namebot,'refer')
        message_out = message_out.replace('%%персональная ссылка%%',str(refer)+"")   
        #message_out = message_out.replace('%%Заявка%%',str(command))
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

