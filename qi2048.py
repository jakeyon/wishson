#2048game by hyj as learning python
import random,sys,pygame
from pygame.locals import*
                               
qipan=[[0 for i in range(4)] for i in range(4)] #初始化棋盘赋值棋子0
PIXEL = 120
SCORE_PIXEL = 100
scores = 0

def fuzhi(l=[]):     #fuzhi 在空位上随机填入2或4,1/4概率4
	list_temp=[]
	for i in range(16):
		if l[i//4][i%4]==0:
			list_temp.append(i)
	if len(list_temp)>0:
		i_pos=random.choice(list_temp)
		i_val=random.choice([2,2,2,4])
		l[i_pos//4][i_pos%4]=i_val

def over(l=[]):   #判断是否无旗可下
	for i in range(16):
		if l[i//4][i%4]==2048:
			return True
	for i in range(16):		 
		if l[i//4][i%4]==0:
			return False
	for i in range(4):
		for j in range(3):
			if l[i][j]==l[i][j+1]:
				return False
			if l[j][i]==l[j+1][i]:
				return False
	return True

def juzhen90(l=[]):   #矩阵逆时针90度旋转
	qipantemp=[[0 for i in range(4)] for i in range(4)] 
	for i in range(4):
		for j in range(4):
			qipantemp[i][j]=l[j][3-i]
	for i in range(4):
		for j in range(4):
			l[i][j]=qipantemp[i][j]
			
def calline(l=[]):   #计算单向量
	global scores
	for i in range(3):
		if l[2-i]==0:
			del l[2-i]
			l.append(0)
	b=0
	e=3
	while b<e:
		if l[b]==l[b + 1]:
			l[b]=l[b]+l[b+1]
			scores = scores + l[b]
			del l[b+1]
			l.append(0)
			e=e-1
		b=b+1

def cal(l=[]):
	for i in range(4):
		calline(l[i])
		
def move(flag=0,l=[]):
	if flag>0:
		juzhen90(l)
	if flag>1:
		juzhen90(l)
	if flag>2:
		juzhen90(l)
	cal(l)
	if flag==3:
		juzhen90(l)
	if flag==2:
		juzhen90(l)
		juzhen90(l)
	if flag==1:
		juzhen90(l)
		juzhen90(l)
		juzhen90(l)
 
# 显示结果

def show(l=[]):
    for i in range(4):
        for j in range(4):
            screen.blit(l[i][j] == 0 and block[(i + j) % 2] or block[2 + (i + j) % 2], (PIXEL * j, PIXEL * i))
            # 数值显示
            if l[i][j] != 0:
                map_text = qipan_font.render(str(l[i][j]), True, (106, 90, 205))
                text_rect = map_text.get_rect()
                text_rect.center = (PIXEL * j + PIXEL // 2, PIXEL * i + PIXEL // 2)
                screen.blit(map_text, text_rect)

    # 分数显示
    screen.blit(score_block, (0, PIXEL * 4))
    score_text = score_font.render( "Score: " + str(scores), True, (106, 90, 205))
    score_rect = score_text.get_rect()
    score_rect.center = (PIXEL * 4 // 2, PIXEL * 4 + SCORE_PIXEL // 2)
    screen.blit(score_text, score_rect)
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((PIXEL * 4, PIXEL * 4 + SCORE_PIXEL))

pygame.display.set_caption("2048")
fuzhi(qipan)
fuzhi(qipan)
block = [pygame.Surface((PIXEL, PIXEL)) for i in range(4)]
block[0].fill((152, 251, 152))
block[1].fill((240, 255, 255))
block[2].fill((0, 255, 127))
block[3].fill((225, 255, 255))
score_block = pygame.Surface((PIXEL * 4, SCORE_PIXEL))
score_block.fill((245, 245, 245))
# 设置字体
qipan_font = pygame.font.Font(None, PIXEL * 2 // 3)
score_font = pygame.font.Font(None, SCORE_PIXEL * 2 // 3)
clock = pygame.time.Clock()

show(qipan)

while not over(qipan):
	clock.tick(12)
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		pressed_keys = pygame.key.get_pressed()
		if  pressed_keys[K_UP]:
			move(1,qipan)
			fuzhi(qipan)
			show(qipan)
		elif pressed_keys[K_DOWN]:
			move(3,qipan)
			fuzhi(qipan)
			show(qipan)
		elif pressed_keys[K_LEFT]:
			move(0,qipan)
			fuzhi(qipan)
			show(qipan)
		elif pressed_keys[K_RIGHT]:
			move(2,qipan)
			fuzhi(qipan)
			show(qipan)
	

pygame.time.delay(3000)
