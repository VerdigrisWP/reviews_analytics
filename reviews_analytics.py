#留言分析
reviews_data = []
reviews_len = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		reviews_data.append(line)
		reviews_len += len(line)
print('讀取完畢，共有', count, '筆留言，每筆留言平均長度為', reviews_len / count)