# 把一个 路径集合 变成一个 树状字典
# list 转 dict
class MyTree:
    def __init__(self):
        self.tree={}

    # onepoint 是 list
    def append_Point_to_tree(self,  onepoint):
        nowPositon = self.tree
        index = 0
        while index < len(onepoint):

            if nowPositon.__contains__(onepoint[index]):
                nowPositon = nowPositon[onepoint[index]]
                index += 1

            else:
                #创建新节点
                nowPositon[onepoint[index]] = {}
        return self.tree

  # 把【 【路径1 a,b,c,d】 ，【路径2】 】
  # 多条路径一次性插入到树中
    def insert_list_to_tree(self, pointlist):
        for onepoint in pointlist:
            self.append_Point_to_tree(onepoint)

a = MyTree()

list_data = [  
    ["3.0", "200", "A20"],
    ["3.0", "200",  "B20"],
    ["3.0",  "210",  "C20"],
    ["3.0",  "210",  "D20"],
    ["2.0", "300",  "A30"],
    ["2.0",  "300",  "B40"],
    ["2.0",  "410",  "C50"],
    ["2.0",  "410",  "D60"],
    ["1.0",  "500",  "E70"],
    ["1.0",  "500",  "F80"],
    ["1.0",  "610",  "G50"],
    ["1.0",  "610",  "H90"]
]  

a.insert_list_to_tree(list_data)
print(a.tree)
