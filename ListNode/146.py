#146
#LRU cache
class Node :
    __slots__ ='pre' , 'next' , 'key' , 'value'
    def __init__(self , key = 0 , value = 0):
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node: #没有这本书
            return None
        node = self.key_to_node[key] #有这本书
        self.remove(node) #抽出来
        self.push_front(node)#放到最上面
        return node

    def get(self,key:int) -> int :
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None :
        node = self.get_node(key)
        if node :
            node.value = value
            return
        self.key_to_node[key] = node =Node(key , value)
        self.push_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.pre
            del self.key_to_node[back_node.key]
            self.remove(back_node)

    def remove(self,x:Node) ->None :
        x.pre.next = x.next
        x.next.pre = x.pre

    def push_front(self, x:Node) -> None:
        x.pre = self.dummy
        x.next = self.dummy.next
        x.pre.next = x
        x.next.pre = x
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)