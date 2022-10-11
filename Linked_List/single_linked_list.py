class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        //TODO 
        self.start_node = None
    
    def insert_at_start(self, data):
        //TODO
        new_node = Node(data)           # 新增 new_node
        new_node.ref = self.start_node  # 新增的 new_node.ref 指向原本的 start_node 的位置
        self.start_node = new_node      # start_node 換成新的節點 new_node

    def insert_at_end(self, data):
        //TODO
        new_node = Node(data)           # 新增 new_node
        if self.start_node.ref is None: # 當 ref 已是最後一個時，start_node = new_node
            self.start_node = new_node
            return

        n = self.start_node      
        while n.ref is not None:  # 當 start_node.ref 還不是 None 時，代表還沒到最後
            n = n.ref             # 直接往後遍歷

        n.ref = new_node          # start_node.ref 是 None 時，start_node = new_node
            
    def insert_after_item(self, x, data):     # 10, 9, 8, 7 需要在 9 後面新增 9.5
        n = self.start_node
        while n.ref is not None:                    # 先 while 確認可否遍歷
            if n.item == x:                         # 如果遍歷時找到目標 x，此時 break 讓 Node 停留   找到 9 且下一筆為 8
                break
            n = n.ref                               # 如果還沒找到目標，繼續遍歷
        if n.ref is None:                           # 如果發現 node 已經沒有後續
            print("item {} is not found !".format(x))
        else:                                       # 當 n.item == x 且 n.ref is not None 時
            new_node = Node(data)                   # 新增 new_node = 9.5
            new_node.ref = n.ref                    # new_node 的後面接找到的 item.ref   9.5 後面改接 8  -|
            n.ref = new_node                        # 把找到的 n.ref = 8 改成 9.5                       -| 同步後移一位
            


    def remove(self):
        //TODO

    def traverse(self):
        //TODO
        if self.start_node is None:  # 當裡面 LinkedList 還沒有任何 item
            print("List has no element")
            return
        else:   # n > n - 1 > n - 2 > n - 3   n 會越變越小
            n = self.start_node  # 開始有 item 後，n 從 start_node 開始
            while n is not None: # 當 n 還有 item
                print(n.item, " ")
                n = n.ref        # n = start_node 的下一個節點


    def sort(self):
        //TODO

    