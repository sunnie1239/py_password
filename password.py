password = 'a123456'
x = 2

while True:
	user_insert = input('請輸入密碼:')
	if user_insert == password :
		print('登入成功!!')
		break
	else :
		print('密碼錯誤!! 還有', x, '機會')
		x = x - 1
		if x < 0 :
			break