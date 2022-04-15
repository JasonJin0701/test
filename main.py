# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm
pointlist = []
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
fatherlist = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
weight = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
visited = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
map = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
pointlist.append([4,0,0])
class point:
    count = 0
    def __init__(self, x, y, father, step):
        self.x = x
        self.y = y
        self.step = step
        point.count += 1
        pointlist.append([x, y, step])
        fatherlist[x][y] = father

def search(nowpoint):
    for i in range(0, 4):
        nextpointx = pointlist[nowpoint][0]+direction[i][0]
        nextpointy = pointlist[nowpoint][1]+direction[i][1]
        if nextpointx >= 0 and nextpointx <= 9 and nextpointy >= 0 and nextpointy <= 9 and visited[nextpointx][nextpointy] == 0 and map[nextpointx][nextpointy] == 0:
            #print(nextpointx,nextpointy)
            weight[nextpointx][nextpointy] = pointlist[nowpoint][2]+1+abs(nextpointy-6)+abs(nextpointx)
            nextpoint = point(nextpointx, nextpointy, nowpoint, pointlist[nowpoint][2]+1)
            visited[nextpointx][nextpointy] = 1
        elif nextpointx >= 0 and nextpointx <= 9 and nextpointy >= 0 and nextpointy <= 9 and visited[nextpointx][nextpointy] == 1 and map[nextpointx][nextpointy] == 0:
            if pointlist[nowpoint][2]+1+abs(nextpointy-6)+abs(nextpointx) < weight[nextpointx][nextpointy]:
                weight[nextpointx][nextpointy] = pointlist[nowpoint][2]+1+abs(nextpointy-6)+abs(nextpointx)
                fatherlist[nextpointx][nextpointy] = nowpoint
mincount = 0
def searchnext():
    min = 9999
    global mincount
    for i in range(0,point.count+1):
        if visited[pointlist[i][0]][pointlist[i][1]] == 1:
            if weight[pointlist[i][0]][pointlist[i][1]] < min:
                min = weight[pointlist[i][0]][pointlist[i][1]]
                mincount = i
    visited[pointlist[mincount][0]][pointlist[mincount][1]] = 2
    return mincount

visited[4][0] = 1
weight[4][0] = 0
nextcount = searchnext()
judge = -1
print("探索过程为:")
while(judge == -1):
    #print(pointlist[nextcount][0],pointlist[nextcount][1],weight[pointlist[nextcount][0]][pointlist[nextcount][1]])
    print(pointlist[nextcount][0],pointlist[nextcount][1])
    search(nextcount)
    nextcount = searchnext()
    if pointlist[nextcount][0] == 0 and pointlist[nextcount][1] == 6:
        print("Find it!\n")
        judge = 1
print("路径为(路径正确，但先后顺序相反): ")
while(1):
    if pointlist[nextcount][0] == 4 and pointlist[nextcount][1] == 0:
        print(pointlist[nextcount][0], pointlist[nextcount][1])
        break
    else:
        print(pointlist[nextcount][0], pointlist[nextcount][1])
        nextcount = fatherlist[pointlist[nextcount][0]][pointlist[nextcount][1]]