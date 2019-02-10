#留言分析
rws_data = []
rws_lens = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		rws_data.append(line)
		rws_lens += len(line)
print('讀取完畢，共有', count, '筆留言，每筆留言平均長度為', rws_lens / len(rws_data))

#依長度篩選留言
rws_100 = []
for data in rws_data:
	if len(data) < 100:
		rws_100.append(data)
print('留言長度小於 100 的共有', len(rws_100), '筆')