import tkinter as tk
import random

class Food:
    luckynum=7
    unluckynum=7
    def grow(self,G):
        global snake_list,draw_a_unit
        if(G==True):
            draw_a_unit(canvas, snake_list[-1][0], snake_list[-1][1], unit_color = "green")
            snake_list.append([snake_list[-1][0],snake_list[-1][1]])
            print("成長")
            state_now['text'] = "成長"
        else:
            print("萎縮")
            state_now['text'] = "萎縮"
            if(len(snake_list)>3):
                draw_a_unit(canvas, snake_list[-2][0], snake_list[-2][1], unit_color = "silver")
                snake_list.pop()
                
        
    def harest(self,G):
        global maxFood
        if(G==True):
            maxFood+=1
            print("豐收")
            state_now['text'] = "豐收"
        else:
            print("歉收")
            state_now['text'] = "歉收"
            if(maxFood>1):
                maxFood-=1
            
    def lifeUp(self):
        global extendLife
        if(extendLife<3):
            extendLife+=1
            print("護身符")
            state_now['text'] = "護身符"
            life_num['text'] = int(life_num['text']) + 1
            
            
    def summonRock(self):
        global snake_list,Food_coord,Rock_coord,draw_a_unit,canvas
        global Column, Row
        while(True):
            t=0
            c=random.choice(range(Column))
            r=random.choice(range(Row))
            temp=[[c,r]]
            temp.append([c+1,r])
            temp.append([c,r+1])
            temp.append([c+1,r+1])
            for i in range (4):    
                if (temp[i] in snake_list or temp[i] in Food_coord or temp[i] in Rock_coord):
                    t=1
                    break
            if(t):
                continue
            draw_a_unit(canvas,c,r,"black")
            draw_a_unit(canvas,c+1,r,"black")
            draw_a_unit(canvas,c,r+1,"black")
            draw_a_unit(canvas,c+1,r+1,"black")
            Rock_coord+=temp
            print("障礙生成")
            state_now['text'] = "障礙生成"
            win.update()
            break
        
    def slow(self):
        global effectTime,FPS
        if(effectTime[2][1]):
            effectTime[2][2]=0
            print("緩速重置")
            state_now['text'] = "緩速時間重置"
        else:
            effectTime[2][1]=True
            FPS+=50
            print("緩速")
            state_now['text'] = "緩速"
    
    def accelerate(self):
        global effectTime,FPS
        if(effectTime[3][1]):
            effectTime[3][2]=0
            print("加速重置")
            state_now['text'] = "加速時間重置"
        else:
            effectTime[3][1]=True
            FPS-=50
            print("加速")
            state_now['text'] = "加速"
            
    def magnet(self):
        global eatRange,effectTime
        eatRange=8
        if(effectTime[4][1]):
            effectTime[4][2]=0
            print("磁鐵")
            state_now['text'] = "磁鐵時間重置"
        else:
            effectTime[4][1]=True
            print("磁鐵重置")
            state_now['text'] = "磁鐵"
        
    def destroyRock(self):
        global effectTime
        if(effectTime[5][1]):
            effectTime[5][2]=0
            print("尖頭")
            state_now['text'] = "尖頭時間重置"
        else:
            effectTime[5][1]=True
            print("尖頭重置")
            state_now['text'] = "尖頭"
            
    def bigharest(self,G):
        global maxFood,effectTime,tempFood
        if(G==True):
            if not effectTime[7][1]:
                if(effectTime[6][1] ):
                    effectTime[6][2]=0
                    print("大豐收重置")
                    state_now['text'] = "大豐收時間重置"
                else:
                    effectTime[6][1]=True
                    tempFood=maxFood
                    maxFood*=2
                    tempFood=maxFood-tempFood
                    print("大豐收")
                    state_now['text'] = "大豐收"
            else:
                self.rand(True,False)
        else:
            if not effectTime[6][1]:
                if(effectTime[7][1]):
                    effectTime[7][2]=0
                    print("大歉收重置")
                    state_now['text'] = "大歉收時間重置"
                elif(maxFood !=1):
                        tempFood=maxFood
                        maxFood=maxFood/2
                        maxFood=int(maxFood)
                        tempFood-=maxFood    
                        for i in range (tempFood):
                            draw_a_unit(canvas, Food_coord[-1][0], Food_coord[-1][1],"silver")
                            Food_coord.pop()
                            
                        effectTime[7][1]=True
                        print("大歉收")
                        state_now['text'] = "大歉收"
            else:
                self.rand(False,True)
                
    def bigGrow(self):
        global growNum,effectTime,snake_list,tempLong
        if(effectTime[8][1] ):
            effectTime[8][2]=0
            print("爆發重置")
            state_now['text'] = "爆發成長時間重置"
        else:
            growNum=len(snake_list)-1
            tempLong=growNum
            effectTime[8][1]=True
            print("爆發")
            state_now['text'] = "爆發成長"
    
    def confusion(self):
        global effectTime
        if(effectTime[9][1] ):
            effectTime[9][2]=0
            print("方向重置")
            state_now['text'] = "方向喪失時間重置"
        else:
            effectTime[9][1]=True
            print("方向")
            state_now['text'] = "方向喪失"
    
    def rand(self,G,B):
        global effectTime,growNum
        if (growNum!=0):
            return
        if(G==True):
            r=random.choices(range(self.luckynum),[0.125,0.125,0.125,0.021875,0.021875,0.021875,0.021875])[0]
            if(r==0):
                self.grow(False)
            elif(r==1):
                self.harest(True)
            elif(r==2):
                self.lifeUp()
            elif(r==3):
                self.slow()
            elif(r==4):
                self.magnet()
            elif(r==5):
                self.destroyRock()
            elif(r==6):
                self.bigharest(True)
        elif(B==True):
            r=random.choices(range(self.unluckynum),[0.125,0.125,0.125,0.028125,0.028125,0.28125,0.028125])[0]
            if(r==0):
                self.grow(True)
            elif(r==1):
                self.harest(False)
            elif(r==2):
                self.summonRock()
            elif(r==3):
                self.accelerate()
            elif(r==4):
                self.bigharest(False)
            elif(r==5):
                self.bigGrow()
            elif(r==6):
                self.confusion()
        else:
            r=random.choices(range(4),[0.4625,0.4875,0.0375,0.0125])[0]
            if(r==0):
                self.rand(1,0)
            elif(r==1):
                self.rand(0,1)
            elif(r==2):
                self.rand(1,0)
                effectTime[0][1]=True
                print("幸運")
                luck_time['text'] = "幸運"
            else:
                self.rand(0,1)
                effectTime[1][1]=True
                print("厄運")
                badluck_time['text'] = "厄運"
            
Fd=Food()        
Row = 20
Column = 20
Unit_size = 20
Height = Row * Unit_size
Width = Column * Unit_size
Direction = 2                   #上下左右-1 1 -2 2
FPS = 150
Have_food = 0
maxFood=1
tempFood=0
Food_coord = []
Rock_coord = []
Score = 0
snake_list = [[11, 10], [10, 10], [9, 10]]
game_map = []
effectTime=dict()
extendLife=0
eatRange=8
growNum=0
tempLong=0
def draw_a_unit(canvas, col, row, unit_color = "green") :
    # 畫一個以左上角為参照的(c,r)的方塊
    x1 = col * Unit_size
    y1 = row * Unit_size
    x2 = (col + 1) * Unit_size
    y2 = (row + 1) * Unit_size
    # 從(x0,y0)畫到(x1,y1)
    canvas.create_rectangle(x1, y1, x2, y2, fill = unit_color, outline = "white")
def put_a_backgroud(canvas, color = 'silver') :
    # 建立像素網格
    for x in range(Column) :
        for y in range(Row) :
            draw_a_unit(canvas, x, y, unit_color = color)
            game_map.append([x, y])
            
def draw_the_snake (canvas, snake_list, color = 'green') :
    for i in snake_list :
        draw_a_unit(canvas, i[0], i[1], unit_color = color)
        
def snake_move(snake_list, dire) :
    global Row, Column
    global Have_food
    global Food_coord
    global Score,growNum
    global effectTime
    new_coord = [0, 0]
    if dire % 2 == 1:
        new_coord[0] = snake_list[0][0]
        new_coord[1] = snake_list[0][1] + dire
    else :
        new_coord[0] = snake_list[0][0] + (int)(dire / 2)
        new_coord[1] = snake_list[0][1]
    snake_list.insert(0, new_coord)
    draw_a_unit(canvas, snake_list[-1][0], snake_list[-1][1], unit_color = "silver")
    draw_a_unit(canvas, snake_list[0][0], snake_list[0][1], )
    temp=[]
    for i in range(len(Food_coord)):
        if((snake_list[0][0]-Food_coord[i][0])**2+(snake_list[0][1]-Food_coord[i][1])**2<=eatRange):
            if(Food_coord[i]==snake_list[0]):    
                draw_a_unit(canvas, Food_coord[i][0], Food_coord[i][1], unit_color = "green")
            else:
                draw_a_unit(canvas, Food_coord[i][0], Food_coord[i][1], unit_color = "silver")
        
            Have_food -= 1
            Score += 10
            str_score.set('Your Score:' + str(Score))
            temp.append(Food_coord[i])
    for i in range (len(temp)):
        Food_coord.remove(temp[i]) 
    for i in range (len(temp)):
        Fd.rand(effectTime[0][1], effectTime[1][1])
    if(growNum==0):    
        snake_list.pop()
    else:
        growNum-=1
    return snake_list

def callback (event) :
    #判断是否可以向上向下操作
    #上下左右-1 1 -2 2
    global Direction,effectTime
    ch = event.keysym
    if not effectTime[9][1]:
        if  ch == 'Up':
            if snake_list[0][0] != snake_list[1][0] :
                Direction = -1
        elif ch == 'Down' :
            if snake_list[0][0] != snake_list[1][0] :
                Direction = 1
        elif ch == 'Left' :
            if snake_list[0][1] != snake_list[1][1] :
                Direction = -2
        elif ch == 'Right' :
            if snake_list[0][1] != snake_list[1][1] :
                Direction = 2
    else:
        if  ch == 'Up':
            if snake_list[0][0] != snake_list[1][0] :
                Direction = 1
        elif ch == 'Down' :
            if snake_list[0][0] != snake_list[1][0] :
                Direction = -1
        elif ch == 'Left' :
            if snake_list[0][1] != snake_list[1][1] :
                Direction = 2
        elif ch == 'Right' :
            if snake_list[0][1] != snake_list[1][1] :
                Direction = -2
    return

def snake_death_judge (snake_list) :
    #return 1代表死亡
    global effectTime
    set_list = snake_list[1:]
    if snake_list[0] in set_list:
        return 1
    elif snake_list[0] in Rock_coord  and not effectTime[5][1]:
        return 1
    elif snake_list[0] in Rock_coord:
        Rock_coord.remove(snake_list[0])
        return 0
    elif snake_list[0][0] >= 20 or snake_list[0][0] < 0:
        return 1
    elif snake_list[0][1] >= 20 or snake_list[0][1] < 0:
        return 1;
    else :
        return 0
    
def food(canvas, snake_list) :
    #隨機生成的位置(x1, y1)
    global Column, Row, Have_food, Food_coord,Rock_coord
    global game_map
    if Have_food==maxFood :
        return
    for i in range(Have_food,maxFood):
        while(True):
            temp=[random.choice(range(Column)),random.choice(range(Row))]
            if (temp not in snake_list and temp not in Food_coord and temp not in Rock_coord):
                Food_coord.append(temp)
                draw_a_unit(canvas, Food_coord[i][0], Food_coord[i][1], unit_color = 'red')
                Have_food += 1
                break
    
def game_loop() :
    global FPS,extendLife,Score,maxFood,tempFood,Food_coord,tempLong,canvas, Column, Row,Direction
    global snake_list,eatRange
    global effectTime,over_label
    win.update()
    food(canvas, snake_list)
    snake_list = snake_move(snake_list, Direction)
    flag = snake_death_judge(snake_list)
    if flag and not extendLife :
        over_label.place(x = 40, y = Height / 2, bg = None)
        return
    elif flag:
        extendLife-=1
        life_num['text'] = int(life_num['text']) - 1
        start(Score)
        return
    for i in range(len(effectTime)):
        if(effectTime[i][1]==True):
            effectTime[i][2]+=FPS
            
            if i == 0:
                luck_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 1:
                badluck_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 2:
                slow_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 3:
                fast_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 4:
                magnet_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 5:
                hard_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 6:
                harvest_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 7:
                unharvest_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 8:
                bigrow_time['text'] = int(10 - effectTime[i][2]/1000)
            if i == 9:
                dic_time['text'] = int(10 - effectTime[i][2]/1000)
                
            if(effectTime[i][2]>effectTime[i][3]*1000):
                effectTime[i][1]=False
                effectTime[i][2]=0
                if(i==2):
                    FPS-=50
                elif(i==3):
                    FPS+=50;
                elif(i==4):
                    eatRange=0
                elif(i==6):
                    maxFood-=tempFood
                    if(maxFood>1):    
                        for i in range (tempFood):
                            draw_a_unit(canvas, Food_coord[-1][0], Food_coord[-1][1],"silver")
                            Food_coord.pop()
                    else:
                        maxFood=1
                        Food_coord=[]
                elif(i==7):
                    maxFood+=tempFood
                elif(i==8):
                    j=0
                    while(j<tempLong):
                        if(len(snake_list)>2):
                            draw_a_unit(canvas, snake_list[-1][0], snake_list[-1][1],"silver")
                            snake_list.pop() 
                        j+=1
    win.after(FPS, game_loop)
    
def start(score=0):
    global Direction,Have_food,Food_coord,score_label,maxFood,over_label,tempLong
    global snake_list,game_map,Score,str_score,Rock_coord,FPS,eatRange,tempFood,growNum
    over_label.place_forget()
    Direction = 2                   #上下左右-1 1 -2 2
    Have_food = 0
    maxFood=1
    FPS=150
    Food_coord = []
    Rock_coord = []
    Score=score
    eatRange=0
    tempFood=0
    growNum=0
    tempLong=0
    canvas1 = tk.Canvas(win, width = Width, height = Height + 2 * Unit_size)
    snake_list = [[11, 10], [10, 10], [9, 10]]
    put_a_backgroud(canvas)
    draw_the_snake(canvas1, snake_list)
    str_score.set('Your Score:' + str(Score))
    draw_the_snake(canvas1, snake_list)
    effectTime[0]=["幸運",False,0,10]
    effectTime[1]=["厄運",False,0,10]
    effectTime[2]=["緩速",False,0,10]
    effectTime[3]=["加速",False,0,10]
    effectTime[4]=["磁鐵",False,0,10]
    effectTime[5]=["尖頭",False,0,10]
    effectTime[6]=["大豐收",False,0,10]
    effectTime[7]=["大歉收",False,0,10]
    effectTime[8]=["爆發成長",False,0,10]
    effectTime[9]=["方向喪失",False,0,10]
    luck_time['text'] = "0"
    badluck_time['text'] = "0"
    slow_time['text'] = "0"
    fast_time['text'] = "0"
    magnet_time['text'] = "0"
    hard_time['text'] = "0"
    harvest_time['text'] = "0"
    unharvest_time['text'] = "0"
    bigrow_time['text'] = "0"
    dic_time['text'] = "0"
    
    game_loop()
    
def rule():
    rulepage = tk.Tk()
    rulepage.title('規則')
    label_1 = tk.Label(rulepage ,text = "正面永久效果:")
    label_2 = tk.Label(rulepage ,text = "萎縮:減少1長度，若長度小於2不發動")
    label_3 = tk.Label(rulepage ,text = "豐收:增加1果實生成量")
    label_4 = tk.Label(rulepage ,text = "護身符:允許失敗一次，保留分數並重置，上限為3")
    
    label_5 = tk.Label(rulepage ,text = "負面永久效果:")
    label_6 = tk.Label(rulepage ,text = "成長:增加1長度")
    label_7 = tk.Label(rulepage ,text = "歉收:減少1果實生成量，若小於1則不發動")
    label_8 = tk.Label(rulepage ,text = "障礙生成:隨機生成2x2大小的石頭，視為牆壁")
    
    label_9 = tk.Label(rulepage ,text = "正面暫時效果:")
    label_10 = tk.Label(rulepage ,text = "緩速:速度降低三分之一")
    label_11 = tk.Label(rulepage ,text = "磁鐵:能吃到距離頭一圈範圍的果實")
    label_12 = tk.Label(rulepage ,text = "尖頭:能破壞碰到頭的石頭")
    label_13 = tk.Label(rulepage ,text = "大豐收:產生目前生成量的兩倍果實，期間內只會發動永久效果")
    label_14 = tk.Label(rulepage ,text = "幸運:期間內只發動正面效果")
    
    label_15 = tk.Label(rulepage ,text = "負面暫時效果:")
    label_16 = tk.Label(rulepage ,text = "爆發成長:固定尾巴，拖成兩倍長度後開始計算時間")
    label_17 = tk.Label(rulepage ,text = "加速:速度加快三分之一")
    label_18 = tk.Label(rulepage ,text = "方向喪失:控制鍵上下顛倒，左右相反")
    label_19 = tk.Label(rulepage ,text = "大歉收:目前生成量減半，期間內只會發動負面效果")
    label_20 = tk.Label(rulepage ,text = "厄運:期間內只發動負面效果")
    
    label_1.grid(row = 0, column = 0)
    label_2.grid(row = 1, column = 0,sticky = 'w')
    label_3.grid(row = 2, column = 0,sticky = 'w')
    label_4.grid(row = 3, column = 0,sticky = 'w')
    label_5.grid(row = 4, column = 0)
    label_6.grid(row = 5, column = 0,sticky = 'w')
    label_7.grid(row = 6, column = 0,sticky = 'w')
    label_8.grid(row = 7, column = 0,sticky = 'w')
    label_9.grid(row = 8, column = 0)
    label_10.grid(row = 9, column = 0,sticky = 'w')
    label_11.grid(row = 10, column = 0,sticky = 'w')
    label_12.grid(row = 11, column = 0,sticky = 'w')
    label_13.grid(row = 12, column = 0,sticky = 'w')
    label_14.grid(row = 13, column = 0,sticky = 'w')
    label_15.grid(row = 14, column = 0)
    label_16.grid(row = 15, column = 0,sticky = 'w')
    label_17.grid(row = 16, column = 0,sticky = 'w')
    label_18.grid(row = 17, column = 0,sticky = 'w')
    label_19.grid(row = 18, column = 0,sticky = 'w')
    label_20.grid(row = 19, column = 0,sticky = 'w')

win = tk.Tk()
win.title('貪吃蛇')

canvas = tk.Canvas(win, width = Width, height = Height + 2 * Unit_size)
canvas.grid(row = 0, column = 0,sticky = 'w',columnspan = 4)

str_score = tk.StringVar()
score_label = tk.Label(win, textvariable = str_score, font = ('楷體', 20), width = 30, height = 1)
str_score.set('Your Score:' + str(Score))
score_label.place(x = 0, y = Height)

put_a_backgroud(canvas)
draw_the_snake(canvas, snake_list)

over_label = tk.Label(win, text = 'Game Over', font = ('楷體', 25), width = 15, height = 1)
state_label = tk.Label(win, text = "發動的效果:")
state_now = tk.Label(win, text = "")
life_label = tk.Label(win, text = "所持護身符:")
life_num = tk.Label(win, text = "0")
button_Start = tk.Button(win,text = "開始",command = start)
button_Rule = tk.Button(win,text = "規則",command = rule)
button_Start.grid(row = 1, column = 0)
button_Rule.grid(row = 1, column = 1)
state_label.grid(row = 6, column = 0)
state_now.grid(row = 6, column = 1)
life_label.grid(row = 7, column = 0)
life_num.grid(row = 7, column = 1)

effect_label = tk.Label(win,text = "暫時效果計時器:")
effect_label.grid(row = 1, column = 2,columnspan = 2)

label_luck = tk.Label(win,text = "幸運:")
luck_time = tk.Label(win,text = "0")
label_luck.grid(row = 2, column = 2)
luck_time.grid(row = 2, column = 3)

label_badluck = tk.Label(win,text = "厄運:")
badluck_time = tk.Label(win,text = "0")
label_badluck.grid(row = 3, column = 2)
badluck_time.grid(row = 3, column = 3)

label_slow = tk.Label(win,text = "緩速:")
slow_time = tk.Label(win,text = "0")
label_slow.grid(row = 4, column = 2)
slow_time.grid(row = 4, column = 3)

label_fast = tk.Label(win,text = "加速:")
fast_time = tk.Label(win,text = "0")
label_fast.grid(row = 5, column = 2)
fast_time.grid(row = 5, column = 3)

label_magnet = tk.Label(win,text = "磁鐵:")
magnet_time = tk.Label(win,text = "0")
label_magnet.grid(row = 6, column = 2)
magnet_time.grid(row = 6, column = 3)

label_hard = tk.Label(win,text = "尖頭:")
hard_time = tk.Label(win,text = "0")
label_hard.grid(row = 7, column = 2)
hard_time.grid(row = 7, column = 3)

label_harvest = tk.Label(win,text = "大豐收:")
harvest_time = tk.Label(win,text = "0")
label_harvest.grid(row = 8, column = 2)
harvest_time.grid(row = 8, column = 3)

label_unharvest = tk.Label(win,text = "大歉收:")
unharvest_time = tk.Label(win,text = "0")
label_unharvest.grid(row = 9, column = 2)
unharvest_time.grid(row = 9, column = 3)

label_bigrow = tk.Label(win,text = "爆發成長:")
bigrow_time = tk.Label(win,text = "0")
label_bigrow.grid(row = 10, column = 2)
bigrow_time.grid(row = 10, column = 3)

label_dic = tk.Label(win,text = "方向喪失:")
dic_time = tk.Label(win,text = "0")
label_dic.grid(row = 11, column = 2)
dic_time.grid(row = 11, column = 3)

canvas.focus_set()
canvas.bind("<KeyPress-Left>",  callback)
canvas.bind("<KeyPress-Right>", callback)
canvas.bind("<KeyPress-Up>",    callback)
canvas.bind("<KeyPress-Down>",  callback)
win.mainloop()