# read.py
import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open ('reviews.txt', 'r') as f:
    #start_time = time.time()
    for line in f:
        data.append(line)
        count = count + 1
        #if count % 1000  == 0:
            #print(len(data))
        bar.update(count)

    #end_time = time.time()
#print('共讀了', end_time - start_time, '秒')
print('檔案讀取完了,共有 ', len(data), '筆留言資料')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言的平均長度為 ', sum_len / len(data) )

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('一共有', len(new), '比留言長度小於 100 ') 
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有 ', len(good), '筆留言有說到 good ')

print(good[0])


# 文字計數
start_time = time.time()
wc = {}
for d in data :
    words = d.split()
    for word in words :
        if word in wc :
            wc[word] += 1
        else :
            wc[word] = 1 # 新增資料
end_time = time.time()
print('共讀了', end_time - start_time, '秒')

for word in wc :
    if wc[word] > 1000000 :
        print(word, wc[word])

print(len(wc))    

while True :
    word = input('請輸入你要查的字')  
    if word == 'q' :
        break
    if word in wc :
        print(word, '出現了', wc[word],'次')
    else:
        print('此字未曾出現')
        break       
print('感謝使用本查詢功能')

