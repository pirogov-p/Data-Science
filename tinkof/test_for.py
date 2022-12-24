my_list = []
for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
                 my_list.append('INSERT INTO transaction (id_transation, price_paper, peper_count,transaction_type,paper_id)'
                                ' VALUES ('+ str(i+5) +', '+str(i*108+100)+','+ str(10-i) +',buy,1);')

for a in my_list:
    print (a)

