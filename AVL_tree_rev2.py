#from collections import deque

class AVL_tree:
    def __init__(self):
        self.entrance = None
        self.nodes = {}

    def balance_LL(self, node):
        new_node = node['left']
        lost_kid = new_node['right'] if (new_node['right']) else None
        parent = node['parent'] if (node['parent']) else None

        new_node['right'] = node
        node['parent'] = new_node

        if (lost_kid):
            node['left'] = lost_kid
            lost_kid['parent'] = node
        else:
            node['left'] = None

        new_node['parent'] = parent

        if (parent):
            if (new_node['value'] < parent['value']):
                parent['left'] = new_node
            else:
                parent['right'] = new_node
        else:
            self.entrance = new_node

        node['height'] = max(node['left']['height'] + 1 if (node['left']) else 0, node['right']['height'] + 1 if (node['right']) else 0)
        new_node['height'] = max(new_node['left']['height'] + 1, new_node['right']['height'] + 1)
        
        return new_node['height']

    def balance_LR(self, node):
        new_node = node['left']['right']
        left_sibling = node['left']
        left_lost_kid = new_node['left'] if (new_node['left']) else None
        right_lost_kid = new_node['right'] if (new_node['right']) else None
        parent = node['parent'] if (node['parent']) else None
        
        new_node['right'] = node
        new_node['right']['parent'] = new_node
        #new_node['right']['left'] = None

        new_node['left'] = left_sibling
        new_node['left']['parent'] = new_node
        #new_node['left']['right'] = None

       
        if (right_lost_kid):
            new_node['right']['left'] = right_lost_kid
            right_lost_kid['parent'] = new_node['right']
            #node['left'] = None
            new_node['right']['height'] = max(right_lost_kid['height'] + 1, new_node['right']['right']['height'] + 1 if (new_node['right']['right']) else 0)
        else:
            new_node['right']['left'] = None
            new_node['right']['height'] = new_node['right']['right']['height'] + 1 if (new_node['right']['right']) else 0

        if (left_lost_kid):
            new_node['left']['right'] = left_lost_kid
            left_lost_kid['parent'] = new_node['left']
            new_node['left']['height'] = max(left_lost_kid['height'] + 1, new_node['left']['left']['height'] + 1 if (new_node['left']['left']) else 0)
        else:
            new_node['left']['right'] = None
            new_node['left']['height'] = new_node['left']['left']['height'] + 1 if (new_node['left']['left']) else 0

        new_node['parent'] = parent
        if (parent):
            if (new_node['value'] < parent['value']):
                parent['left'] = new_node
            else:
                parent['right'] = new_node
        else:
            self.entrance = new_node

        new_node['height'] = max(new_node['left']['height'] + 1, new_node['right']['height'] + 1)
        
        return new_node['height']

    def balance_RL(self, node):
        new_node = node['right']['left']
        right_sibling = node['right']
        left_lost_kid = new_node['left'] if (new_node['left']) else None
        right_lost_kid = new_node['right'] if (new_node['right']) else None
        parent = node['parent'] if (node['parent']) else None

        new_node['left'] = node
        new_node['left']['parent'] = new_node

        new_node['right'] = right_sibling
        new_node['right']['parent'] = new_node
        
        if(left_lost_kid):
            new_node['left']['right'] = left_lost_kid
            left_lost_kid['parent'] = new_node['left']
            #node['right'] = None
            new_node['left']['height'] = max(left_lost_kid['height'] + 1, new_node['left']['left']['height'] + 1 if (new_node['right']['right']) else 0)
        else:
            new_node['left']['right'] = None
            new_node['left']['height'] = new_node['left']['left']['height'] + 1 if (new_node['left']['left']) else 0

        if (right_lost_kid):
            new_node['right']['left'] = right_lost_kid
            right_lost_kid['parent'] = new_node['right']
            #node['left'] = None
            new_node['right']['height'] = max(right_lost_kid['height'] + 1, new_node['right']['right']['height'] + 1 if (new_node['right']['right']) else 0)
        else:
            new_node['right']['left'] = None
            new_node['right']['height'] = new_node['right']['right']['height'] + 1 if (new_node['right']['right']) else 0

        new_node['parent'] = parent
        if (parent):
            if (new_node['value'] < parent['value']):
                parent['left'] = new_node
            else:
                parent['right'] = new_node
        else:
            self.entrance = new_node

        new_node['height'] = max(new_node['left']['height'] + 1, new_node['right']['height'] + 1)
        
        return new_node['height']

    def balance_RR(self, node):
        new_node = node['right']
        lost_kid = new_node['left'] if (new_node['left']) else None
        parent = node['parent'] if (node['parent']) else None

        new_node['left'] = node
        node['parent'] = new_node

        if (lost_kid):
            node['right'] = lost_kid
            lost_kid['parent'] = node
        else:
            node['right'] = None

        new_node['parent'] = parent

        if (parent):
            if (new_node['value'] < parent['value']):
                parent['left'] = new_node
            else:
                parent['right'] = new_node
        else:
            self.entrance = new_node

        node['height'] = max(node['left']['height'] + 1 if (node['left']) else 0, node['right']['height'] + 1 if (node['right']) else 0)
        new_node['height'] = max(new_node['left']['height'] + 1, new_node['right']['height'] + 1)
        
        return new_node['height']

    def add(self, key, value):
        def recursive(node, key, value):
            if (value < node['value']):
                if (not node['left']):    #конечный случай
                    node['left'] = {
                        'key': key,
                        'value': value,
                        'height': 0,
                        'left': None,
                        'right': None,
                        'middle': {},
                        'parent': node,
                        'pool': False
                    }
                    self.nodes[key] = node['left']
                    if (node['right']):
                        return 0
                    else:
                        node['height'] = 1
                        return 1
                else:    #рекурсивный случай
                    new_left_height = recursive(node['left'], key, value) + 1
                    right_height = node['right']['height'] + 1 if node['right'] else 0
                    if ((new_left_height - right_height) >= 2):
                        left_kid_height = node['left']['left']['height'] + 1 if (node['left']['left']) else 0
                        right_kid_height = node['left']['right']['height'] + 1 if (node['left']['right']) else 0
                        if ((left_kid_height - right_kid_height) >= 1):
                            #Left_Left_balance_operation
                            #print('Node ' + str(node['key']) + ' needs Left_Left_balance')
                            return self.balance_LL(node)
                        else:
                            #left_Right_balance_operation
                            #print('Node ' + str(node['key']) + ' needs Left_Right_balance')
                            return self.balance_LR(node)
                            #pass
                        #return new_left_height
                    else:
                        node['height'] = new_left_height
                        return new_left_height
            elif (value > node['value']):    #конечный случай
                if (not node['right']):
                    node['right'] = {
                        'key': key,
                        'value': value,
                        'height': 0,
                        'left': None,
                        'right': None,
                        'middle': {},
                        'parent': node,
                        'pool': False
                    }
                    self.nodes[key] = node['right']
                    if (node['left']):
                        return 0
                    else:
                        node['height'] = 1
                        return 1
                else:    #рекурсивный случай
                    new_right_height = recursive(node['right'], key, value) + 1
                    left_height = node['left']['height'] + 1 if node['left'] else 0
                    if ((new_right_height - left_height) >= 2):
                        left_kid_height = node['right']['left']['height'] + 1 if (node['right']['left']) else 0
                        right_kid_height = node['right']['right']['height'] + 1 if (node['right']['right']) else 0
                        if ((left_kid_height - right_kid_height) >= 1):
                            #Right_Left_balance_operation
                            #print('Node ' + str(node['key']) + ' needs Right_Left_balance')
                            #pass
                            return self.balance_RL(node)
                        else:
                            #Right_Right_balance_operation
                            #print('Node ' + str(node['key']) + ' needs Right_Right_balance')
                            return self.balance_RR(node)
                        #return new_right_height
                    else:
                        node['height'] = new_right_height
                        return new_right_height
            else:    #конечный случай
                node['middle'][key] = {
                        'key': key,
                        'value': value,
                        'height': 0,
                        'left': None,
                        'right': None,
                        'middle': {},
                        'parent': None,
                        'pool': True
                    }
                self.nodes[key] = node['middle'][key]
                return node['height']
                    
        
        if (not self.entrance):
            self.entrance = {
                'key': key,
                'value': value,
                'height': 0,
                'left': None,
                'right': None,
                'middle': {},
                'parent': None,
                'pool': False
            }
            self.nodes[key] = self.entrance
            return
        recursive(self.entrance, key, value)

    def remove(self, node):
        #del self.nodes[node['key']]
        def recursive(node, delete_node):
            if (delete_node['value'] < node['value']):
                new_left_height = recursive(node['left'], delete_node) + 1
                right_height = node['right']['height'] + 1 if (node['right']) else 0
                return self.balance_factor(node, new_left_height, right_height)
            elif (delete_node['value'] > node['value']):
                new_right_height = recursive(node['right'], delete_node) + 1
                left_height = node['left']['height'] + 1 if (node['left']) else 0
                return self.balance_factor(node, left_height, new_right_height)
            elif (delete_node == node):
                if (delete_node['middle']):
                    right_tree = delete_node['right'] if (delete_node['right']) else None
                    left_tree = delete_node['left'] if (delete_node['left']) else None
                    parent = delete_node['parent'] if (delete_node['parent']) else None
                    middle = delete_node['middle']
                    new_node_key = list(middle.keys())[0]
                    new_node = middle[new_node_key]
                    del middle[new_node_key]
                    #del self.nodes[delete_node['key']]

                    new_node['right'] = right_tree
                    if (right_tree):
                        right_tree['parent'] = new_node
                    
                    new_node['left'] = left_tree
                    if (left_tree):
                        left_tree['parent'] = new_node

                    new_node['middle'] = middle
                    
                    new_node['parent'] = parent
                    if (parent):
                        if(parent['value'] > new_node['value']):
                            parent['left'] = new_node
                        else:
                            parent['right'] = new_node
                    else:
                        self.entrance = new_node

                    new_node['height'] = delete_node['height']
                    return new_node['height']
                else: #hard part
                    if (delete_node['height'] == 0):
                        #del self.nodes[delete_node['key']]
                        if (delete_node == self.entrance):
                            self.entrance = None
                            return
                        else:
                            if (node['parent']['left'] == node):
                                node['parent']['left'] = None
                            else:
                                node['parent']['right'] = None
                            return -1
                    elif (node['height'] == 1):
                        #del self.nodes[delete_node['key']]
                        if (node['right']):
                            node['right']['parent'] = node['parent'] if (node['parent']) else None
                            if (node['parent']):
                                if (node['parent']['left'] == node):
                                    node['parent']['left'] = node['right']
                                    print('first')
                                else:
                                    node['parent']['right'] = node['right']
                                if (node['left']):
                                    node['right']['height'] = 1
                                    node['right']['left'] = node['left']
                                    node['left']['parent'] = node['right']
                                    return 1
                                else:
                                    return 0
                            else:
                                self.entrance = node['right']
                                if(node['left']):
                                    node['right']['height'] = 1
                                    node['right']['left'] = node['left']
                                    node['left']['parent'] = node['right']
                                return
                        else:
                            node['left']['parent'] = node['parent'] if (node['parent']) else None
                            if (node['parent']):
                                if (node['parent']['left'] == node):
                                    node['parent']['left'] = node['left']
                                else:
                                    node['parent']['right'] = node['left']
                                return 0
                            else:
                                self.entrance = node['left']

                    else:
                        #del self.nodes[delete_node['key']]
                        if (delete_node['left']['height'] <= delete_node['right']['height']):
                            if (delete_node['right']['left']):
                                new_node_obj = self.get_right_node(node['right'], delete_node)
                                left_subTree = delete_node['left']
                                right_subTree = delete_node['right']
                                parent = delete_node['parent'] if (delete_node['parent']) else None

                                new_node_obj['new_node']['left'] = left_subTree
                                left_subTree['parent'] = new_node_obj['new_node']

                                new_node_obj['new_node']['right'] = right_subTree
                                right_subTree['parent'] = new_node_obj['new_node']

                                if (parent):
                                    if (new_node_obj['new_node']['value'] < parent['value']):
                                        parent['left'] = new_node_obj['new_node']
                                    else:
                                        parent['right'] = new_node_obj['new_node']
                                    new_node_obj['new_node']['parent'] = parent
                                    return self.balance_factor(new_node_obj['new_node'], left_subTree['height'] + 1, new_node_obj['height'] + 1)
                                else:
                                    self.entrance = new_node_obj['new_node']
                                    new_node_obj['new_node']['parent'] = None
                                    self.balance_factor(new_node_obj['new_node'], left_subTree['height'] + 1, new_node_obj['height'] + 1)
                            else:
                                new_node = delete_node['right']
                                left_subTree = delete_node['left']
                                parent = delete_node['parent'] if (delete_node['parent']) else None

                                new_node['left'] = left_subTree
                                left_subTree['parent'] = new_node
                                
                                """ print(new_node['parent'])
                                print(new_node['left']['key'])
                                print(new_node['right']['key']) """

                                if (parent):
                                    if (new_node['value'] < parent['value']):
                                        parent['left'] = new_node
                                    else:
                                        parent['right'] = new_node
                                    new_node['parent'] = parent
                                    return self.balance_factor(new_node, left_subTree['height'] + 1, new_node['right']['height'] + 1)
                                else:
                                    self.entrance = new_node
                                    new_node['parent'] = None
                                    """ print(new_node['parent'])
                                    print(new_node['left']['key'])
                                    print(new_node['right']['key']) """
                                    #self.balance_factor(new_node, left_subTree['height'] + 1, new_node['right']['height'] + 1)
            else:
                #del self.nodes[delete_node['key']]
                del node['middle'][delete_node['key']]
                return node['height']
                pass
        recursive(self.entrance, node)
        del self.nodes[node['key']]


    def find(self, value):
        def recursive(node, value):
            #конечный случай
            if (node['value'] == value):
                return node
            #рекурсивный случай
            if (value < node['value']):
                if (node['left'] == None):
                    return "Nothing"
                else:
                    return recursive(node['left'], value)
            else:
                if (node['right'] == None):
                    return "Nothing"
                else:
                    return recursive(node['right'], value)
        
        return recursive(self.entrance, value)
            
    def get_max_floor(self):
        return self.entrance['height'] if (self.entrance) else 0

    def do_with_nodes(self, function, type):
        def recursive_reverse(node, function):
            if (node['right']):
                recursive_reverse(node['right'], function)
            if (node['left']):
                function(node)
                if (len(node['middle'])):
                    for n in node['middle']:
                        function(node['middle'][n])
                recursive_reverse(node['left'], function)
                return
            else:
                function(node)
                if (len(node['middle'])):
                    for n in node['middle']:
                        function(node['middle'][n])
                return
            
        def recursive_straight(node, function):
            if (node['left']):
                recursive_straight(node['left'], function)
            if (node['right']):
                function(node)
                if (node['middle']):
                    for n in node['middle']:
                        function(node['middle'][n])
                recursive_straight(node['right'], function)
                return
            else:
                function(node)
                if (node['middle']):
                    for n in node['middle']:
                        function(node['middle'][n])
                return
        
        def recursive_tree(node, function):
            function(node)
            if (node['middle']):
                for n in node['middle']:
                    function(node['middle'][n])
            if (node['left']): recursive_tree(node['left'], function)
            if (node['right']): recursive_tree(node['right'], function)
            return

        methods = {
            'reverse': recursive_reverse,
            'straight': recursive_straight,
            'tree': recursive_tree,
        }

        methods.get(type)(self.entrance, function)

    def count_sums(self):
        result = {
            'a': 0,
            'b': 0
        }
        counter = {
            'c': 0
        }
        def recursive(node, counter, result):
            if (node['left']):
                recursive(node['left'], counter, result)
            if (node['right']):
                if (counter['c'] <= len(self.nodes)/2):
                    result['a'] += node['value']
                else:
                    result['b'] += node['value']
                counter['c'] += 1

                if(node['middle']):
                    for key in node['middle']:
                        if (counter['c'] <= len(self.nodes)/2):
                            result['a'] += node['middle'][key]['value']
                        else:
                            result['b'] += node['middle'][key]['value']
                        counter['c'] += 1

                recursive(node['right'], counter, result)
                return
            else:
                if (counter['c'] <= len(self.nodes)/2):
                    result['a'] += node['value']
                else:
                    result['b'] += node['value']
                counter['c'] += 1

                if(node['middle']):
                    for key in node['middle']:
                        if (counter['c'] <= len(self.nodes)/2):
                            result['a'] += node['middle'][key]['value']
                        else:
                            result['b'] += node['middle'][key]['value']
                        counter['c'] += 1
                return
        recursive(self.entrance, counter, result)
        return result

    def balance_factor(self, node, left_height, right_height):
        if ((right_height - left_height) > 1):
            right_left_height = node['right']['left']['height'] + 1 if (node['right']['left']) else 0
            right_right_height = node['right']['right']['height'] + 1 if (node['right']['right']) else 0
            if (right_left_height < right_right_height):
                return self.balance_RR(node)
            else:
                return self.balance_RL(node)
        elif ((left_height - right_height) > 1):
            left_left_height = node['left']['left']['height'] + 1 if (node['left']['left']) else 0
            left_right_height = node['left']['right']['height'] + 1 if (node['left']['right']) else 0
            if (left_left_height < left_right_height):
                return self.balance_LL(node)
            else:
                return self.balance_LR(node)
        elif(left_height >= right_height):
            node['height'] = left_height
            return left_height
        else:
            node['height'] = right_height
            return right_height
        
    def get_right_node(self, node, delete_node):
        if (node['left']):
            next_right = self.get_right_node(node['left'], delete_node)
            right_height = node['right']['height'] + 1 if (node['right']) else 0
            next_right['height'] = self.balance_factor(node, next_right['height'] + 1, right_height)
            return next_right
        else:
            if (node == delete_node['right']):
                return {
                    'new_node': node,
                    'height': 1 if (node['right']) else 0
                }
            else:
                if (node['right']):
                    node['parent']['left'] = node['right']
                    node['right']['parent'] = node['parent']
                else:
                    node['parent']['left'] = None
                return {
                    'new_node': node,
                    'height': node['right']['height'] if (node['right']) else -1
                }
            
    def get_left_node(self, node, delete_node):
        if (node['right']):
            next_left = self.get_left_node(node['right'], delete_node)
            left_height = node['left']['height'] + 1 if (node['left']) else 0
            next_left['height'] = self.balance_factor(node, left_height, next_left['height'] + 1)
            return next_left
        else:
            if (node['left']):
                node['parent']['right'] = node['left']
                node['left']['parent'] = node['parent']
                return {
                    'new_node': node,
                    'height': 0
                }
            else:
                node['parent']['right'] = None
                return {
                    'new_node': node,
                    'height': -1
                }

    def get(self):
        pass

#tree = AVL_tree()

""" tree.add(1, 4)
tree.add(2, 1)
tree.add(3, 8)
tree.add(4, 3)
tree.add(5, 2)
tree.add(6, 9)
tree.add(7, 7)
tree.add(8, 5) """

""" tree.add(1, 1)
tree.add(2, 2)
tree.add(3, 3)
tree.add(4, 4)
tree.add(5, 5)
tree.add(6, 6)
tree.add(7, 7)
tree.add(8, 8) """
# ALL RR

""" tree.add(1, 8)
tree.add(2, 7)
tree.add(3, 6)
tree.add(4, 5)
tree.add(5, 4)
tree.add(6, 3)
tree.add(7, 2)
tree.add(8, 1) """
# All LL

""" tree.add(1, 10)
tree.add(2, 5)
tree.add(3, 20)
tree.add(4, 15)
tree.add(5, 13) """
# 3 LL, 1 RL

""" tree.add(1, 20)
tree.add(2, 40)
tree.add(3, 30)
tree.add(4, 35)
tree.add(5, 33) """
# 1 RL, 2 LR, 1 RL, 3 RL, 2 LR, 1 RL

""" tree.add(1, 40)
tree.add(2, 10)
tree.add(3, 60)
tree.add(4, 8)
tree.add(5, 20)
tree.add(6, 15) """
# 1 LR

""" tree.add(1, 10)
tree.add(2, 9)
tree.add(3, 8) """

""" tree.add(1, 10)
tree.add(2, 9)
tree.add(3, 20)
tree.add(4, 19)
tree.add(5, 18) """

""" tree.add(1, 20)
tree.add(2, 18)
tree.add(3, 30)
tree.add(4, 17)
tree.add(5, 27)
tree.add(6, 31)
tree.add(7, 24)
tree.add(8, 28)
tree.add(9, 25) """


""" arr = []
def f(n, a = arr):
    a.append('-'.join([str(n['value']), str(n['height'])]))

tree.do_with_nodes(f, True)
print(', '.join(arr)) """