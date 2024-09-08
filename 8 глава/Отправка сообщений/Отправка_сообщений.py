def send_messages(mes, sent_messages):
    while mes:
        cur_mess = mes.pop()
        print(cur_mess)
        sent_messages.append(cur_mess)
mes = ['Привет', 'как дела', 'чем занимаешься']
sent_messages = []
send_messages(mes[:], sent_messages)

for m in sent_messages:
    print(m)
    
print('\n')
for i in mes:
    print(i)
