password = 'a123456'
x = 2

while x >= 0:
	user_insert = input('請輸入密碼:')
	if user_insert == password :
		print('登入成功!!')
		break
	else :
		print('密碼錯誤!!')
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('30秒後再試吧~')
	x = x - 1