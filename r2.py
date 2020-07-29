#有一份文字檔,更改模式
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	allen_word_count = 0
	allen_sticker_count =0
	allen_photo_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_photo_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_photo_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_photo_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了', allen_word_count, '個字', '貼圖有', allen_sticker_count, '圖片有', allen_photo_count)
	print('viki說了', viki_word_count,'個字', '貼圖有', viki_sticker_count, '圖片有', viki_photo_count)


def writ_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

	
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#writ_file('output.txt', lines)


main()

		

