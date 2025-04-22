import traceback
from AVL_tree_rev2 import AVL_tree

tests = []

def test_1(): #test for left left rotation
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
    except:
        print('FAIL_1 balance_LL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-8-6, 8-None-None, 5-7-3, 9-None-None, 7-None-9, 1-2-5, 2-4-None, 4-None-None'):
            print('PASS_1_1')
        else:
            print('FAIL_1_1    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'])])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 8-0, 5-2, 9-0, 7-1, 1-3, 2-1, 4-0'):
            print('PASS_1_2')
        else:
            print('FAIL_1_2    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-5, 8-3, 5-1, 9-7, 7-5, 1-None, 2-1, 4-2'):
            print('PASS_1_3')
        else:
            print('FAIL_1_3    ' + result)
        arr.clear()
tests.append(test_1)

def test_2(): #test for right right rotation
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 10)
        tree.add(3, 30)
        tree.add(4, 9)
        tree.add(5, 16)
        tree.add(6, 31)
        tree.add(7, 15)
        tree.add(8, 19)
        tree.add(9, 17)
    except:
        print('FAIL_2 balance_RR function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-None-6, 1-5-3, 8-9-None, 9-None-None, 5-2-8, 7-None-None, 2-4-7, 4-None-None'):
            print('PASS_2_1')
        else:
            print('FAIL_2_1    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'])])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 1-3, 8-1, 9-0, 5-2, 7-0, 2-1, 4-0'):
            print('PASS_2_2')
        else:
            print('FAIL_2_2    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-1, 1-None, 8-5, 9-8, 5-1, 7-2, 2-5, 4-2'):
            print('PASS_2_3')
        else:
            print('FAIL_2_3    ' + result)
        arr.clear()
tests.append(test_2)

def test_3(): #test for right left rotation
    tree = AVL_tree()
    try:
        tree.add(1, 10)
        tree.add(2, 9)
        tree.add(3, 20)
        tree.add(4, 8)
        tree.add(5, 15)
        tree.add(6, 25)
        tree.add(7, 22)
        tree.add(8, 26)
        tree.add(9, 23)
    except:
        print('FAIL_3 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '8-None-None, 6-9-8, 9-None-None, 7-3-6, 3-5-None, 5-None-None, 1-2-7, 2-4-None, 4-None-None'):
            print('PASS_3_1')
        else:
            print('FAIL_3_1    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'])])), 'reverse')
        result = ', '.join(arr)
        if (result == '8-0, 6-1, 9-0, 7-2, 3-1, 5-0, 1-3, 2-1, 4-0'):
            print('PASS_3_2')
        else:
            print('FAIL_3_2    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '8-6, 6-7, 9-6, 7-1, 3-7, 5-3, 1-None, 2-1, 4-2'):
            print('PASS_3_3')
        else:
            print('FAIL_3_3    ' + result)
        arr.clear()
tests.append(test_3)

def test_4(): #test for left right rotation
    tree = AVL_tree()

    try:
        tree.add(1, 10)
        tree.add(2, 9)
        tree.add(3, 20)
        tree.add(4, 8)
        tree.add(5, 15)
        tree.add(6, 21)
        tree.add(7, 14)
        tree.add(8, 18)
        tree.add(9, 16)
    except:
        print('FAIL_4 balance_LR function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-None-6, 8-5-3, 9-None-None, 5-7-9, 7-None-None, 1-2-8, 2-4-None, 4-None-None'):
            print('PASS_4_1')
        else:
            print('FAIL_4_1    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'])])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 8-2, 9-0, 5-1, 7-0, 1-3, 2-1, 4-0'):
            print('PASS_4_2')
        else:
            print('FAIL_4_2    ' + result)
        arr.clear()

        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-8, 8-1, 9-5, 5-8, 7-5, 1-None, 2-1, 4-2'):
            print('PASS_4_3')
        else:
            print('FAIL_4_3    ' + result)
        arr.clear()
tests.append(test_4)

def test_5(): #test for right right rotation
    tree = AVL_tree()

    try:
        tree.add(1, 1)
        tree.add(2, 2)
        tree.add(3, 3)
    except:
        print('FAIL_5 balance_RR function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-None-None, 2-1-3, 1-None-None'):
            print('PASS_5_1')
        else:
            print('FAIL_5_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-0, 2-1, 1-0'):
            print('PASS_5_2')
        else:
            print('FAIL_5_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-2, 2-None, 1-2'):
            print('PASS_5_3')
        else:
            print('FAIL_5_3    ' + result)
        arr.clear()
tests.append(test_5)

def test_6(): #test for left right rotation
    tree = AVL_tree()
    try:
        tree.add(1, 3)
        tree.add(2, 1)
        tree.add(3, 2)
    except:
        print('FAIL_6 balance_LR function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-None-None, 3-2-1, 2-None-None'):
            print('PASS_6_1')
        else:
            print('FAIL_6_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-0, 3-1, 2-0'):
            print('PASS_6_2')
        else:
            print('FAIL_6_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-3, 3-None, 2-3'):
            print('PASS_6_3')
        else:
            print('FAIL_6_3    ' + result)
        arr.clear()
tests.append(test_6)

def test_7(): #test for left left rotation
    tree = AVL_tree()
    try:
        tree.add(1, 3)
        tree.add(2, 2)
        tree.add(3, 1)
    except:
        print('FAIL_7 balance_LL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-None-None, 2-3-1, 3-None-None'):
            print('PASS_7_1')
        else:
            print('FAIL_7_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-0, 2-1, 3-0'):
            print('PASS_7_2')
        else:
            print('FAIL_7_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '1-2, 2-None, 3-2'):
            print('PASS_7_3')
        else:
            print('FAIL_7_3    ' + result)
        arr.clear()
tests.append(test_7)

def test_8(): #test for right left rotation
    tree = AVL_tree()
    try:
        tree.add(1, 1)
        tree.add(2, 3)
        tree.add(3, 2)
    except:
        print('FAIL_8 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-None-None, 3-1-2, 1-None-None'):
            print('PASS_8_1')
        else:
            print('FAIL_8_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-0, 3-1, 1-0'):
            print('PASS_8_2')
        else:
            print('FAIL_8_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-3, 3-None, 1-3'):
            print('PASS_8_3')
        else:
            print('FAIL_8_3    ' + result)
        arr.clear()
tests.append(test_8)

def test_9(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
        tree.remove(tree.nodes[5])
    except:
        print('FAIL_9 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-None-6, 8-7-3, 9-None-None, 7-None-9, 1-2-8, 2-4-None, 4-None-None'):
            print('PASS_9_1')
        else:
            print('FAIL_9_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 8-2, 9-0, 7-1, 1-3, 2-1, 4-0'):
            print('PASS_9_2')
        else:
            print('FAIL_9_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-8, 8-1, 9-7, 7-8, 1-None, 2-1, 4-2'):
            print('PASS_9_3')
        else:
            print('FAIL_9_3    ' + result)
        arr.clear()
tests.append(test_9)

def test_10(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
        tree.remove(tree.nodes[3])
    except:
        print('FAIL_10 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-8-None, 8-None-None, 5-7-6, 9-None-None, 7-None-9, 1-2-5, 2-4-None, 4-None-None'):
            print('PASS_10_1')
        else:
            print('FAIL_10_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-1, 8-0, 5-2, 9-0, 7-1, 1-3, 2-1, 4-0'):
            print('PASS_10_2')
        else:
            print('FAIL_10_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-5, 8-6, 5-1, 9-7, 7-5, 1-None, 2-1, 4-2'):
            print('PASS_10_3')
        else:
            print('FAIL_10_3    ' + result)
        arr.clear()
tests.append(test_10)

def test_11(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
        tree.remove(tree.nodes[9])
    except:
        print('FAIL_11 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-8-6, 8-None-None, 5-7-3, 7-None-None, 1-2-5, 2-4-None, 4-None-None'):
            print('PASS_11_1')
        else:
            print('FAIL_11_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 8-0, 5-2, 7-0, 1-3, 2-1, 4-0'):
            print('PASS_11_2')
        else:
            print('FAIL_11_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-5, 8-3, 5-1, 7-5, 1-None, 2-1, 4-2'):
            print('PASS_11_3')
        else:
            print('FAIL_11_3    ' + result)
        arr.clear()
tests.append(test_11)

def test_12(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
        tree.remove(tree.nodes[8])
    except:
        print('FAIL_12 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-None-6, 5-7-3, 9-None-None, 7-None-9, 1-2-5, 2-4-None, 4-None-None'):
            print('PASS_12_1')
        else:
            print('FAIL_12_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 5-2, 9-0, 7-1, 1-3, 2-1, 4-0'):
            print('PASS_12_2')
        else:
            print('FAIL_12_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-5, 5-1, 9-7, 7-5, 1-None, 2-1, 4-2'):
            print('PASS_12_3')
        else:
            print('FAIL_12_3    ' + result)
        arr.clear()
tests.append(test_12)

def test_13(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 2)
        tree.add(2, 1)
        tree.add(3, 3)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_13 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-2-None, 2-None-None'):
            print('PASS_13_1')
        else:
            print('FAIL_13_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-1, 2-0'):
            print('PASS_13_2')
        else:
            print('FAIL_13_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-None, 2-3'):
            print('PASS_13_3')
        else:
            print('FAIL_13_3    ' + result)
        arr.clear()
tests.append(test_13)

def test_14(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 2)
        tree.add(2, 3)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_14 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-None-None'):
            print('PASS_14_1')
        else:
            print('FAIL_14_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-0'):
            print('PASS_14_2')
        else:
            print('FAIL_14_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-None'):
            print('PASS_14_3')
        else:
            print('FAIL_14_3    ' + result)
        arr.clear()
tests.append(test_14)

def test_15(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 2)
        tree.add(2, 1)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_15 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-None-None'):
            print('PASS_15_1')
        else:
            print('FAIL_15_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-0'):
            print('PASS_15_2')
        else:
            print('FAIL_15_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '2-None'):
            print('PASS_15_3')
        else:
            print('FAIL_15_3    ' + result)
        arr.clear()
tests.append(test_15)

def test_16(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_16 balance_RL function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-None-None, 3-8-6, 8-None-None, 5-9-3, 9-None-None, 7-2-5, 2-4-None, 4-None-None'):
            print('PASS_16_1')
        else:
            print('FAIL_16_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-0, 3-1, 8-0, 5-2, 9-0, 7-3, 2-1, 4-0'):
            print('PASS_16_2')
        else:
            print('FAIL_16_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '6-3, 3-5, 8-3, 5-7, 9-5, 7-None, 2-7, 4-2'):
            print('PASS_16_3')
        else:
            print('FAIL_16_3    ' + result)
        arr.clear()
tests.append(test_16)

def test_17(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 2)
        tree.add(2, 1)
        tree.add(3, 3)
        tree.add(4, 4)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_17 balance_RL function error')
    else:
        """ print(tree.entrance['key'])
        print(tree.entrance['left']['key'])
        print(tree.entrance['right']['key'])
        print(tree.entrance['right']['right']['key']) """
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-None-None, 3-2-4, 2-None-None'):
            print('PASS_17_1')
        else:
            print('FAIL_17_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-0, 3-1, 2-0'):
            print('PASS_17_2')
        else:
            print('FAIL_17_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-3, 3-None, 2-3'):
            print('PASS_17_3')
        else:
            print('FAIL_17_3    ' + result)
        arr.clear()
tests.append(test_17)

def test_18(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 10)
        tree.add(2, 5)
        tree.add(3, 15)
        tree.add(4, 10)
        tree.add(5, 10)
        tree.add(6, 10)
        tree.remove(tree.nodes[1])
    except:
        print('FAIL_18 balance function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-None-None, 4-2-3, 5-None-None, 6-None-None, 2-None-None'):
            print('PASS_18_1')
        else:
            print('FAIL_18_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-0, 4-1, 5-0, 6-0, 2-0'):
            print('PASS_18_2')
        else:
            print('FAIL_18_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-4, 4-None, 5-None, 6-None, 2-4'):
            print('PASS_18_3')
        else:
            print('FAIL_18_3    ' + result)
        arr.clear()
tests.append(test_18)

def test_19(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 10)
        tree.add(2, 5)
        tree.add(3, 15)
        tree.add(4, 10)
        tree.add(5, 10)
        tree.add(6, 10)
        tree.remove(tree.nodes[5])
    except:
        print('FAIL_19 balance function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-None-None, 1-2-3, 4-None-None, 6-None-None, 2-None-None'):
            print('PASS_19_1')
        else:
            print('FAIL_19_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-0, 1-1, 4-0, 6-0, 2-0'):
            print('PASS_19_2')
        else:
            print('FAIL_19_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-1, 1-None, 4-None, 6-None, 2-1'):
            print('PASS_19_3')
        else:
            print('FAIL_19_3    ' + result)
        arr.clear()
tests.append(test_19)

def test_20(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 10)
        tree.add(2, 5)
        tree.add(3, 15)
        tree.add(4, 15)
        tree.add(5, 15)
        tree.add(6, 15)
        tree.remove(tree.nodes[3])
    except Exception as e:
        print('FAIL_20 internal tree error')
        print(traceback.format_exc())
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-None-None, 5-None-None, 6-None-None, 1-2-4, 2-None-None'):
            print('PASS_20_1')
        else:
            print('FAIL_20_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-0, 5-0, 6-0, 1-1, 2-0'):
            print('PASS_20_2')
        else:
            print('FAIL_20_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '4-1, 5-None, 6-None, 1-None, 2-1'):
            print('PASS_20_3')
        else:
            print('FAIL_20_3    ' + result)
        arr.clear()
tests.append(test_20)

def test_21(): #test for remove
    tree = AVL_tree()
    try:
        tree.add(1, 10)
        tree.add(2, 5)
        tree.add(3, 15)
        tree.add(4, 5)
        tree.add(5, 5)
        tree.add(6, 5)
        tree.remove(tree.nodes[2])
    except Exception as e:
        print('FAIL_21 internal tree error')
        print(traceback.format_exc())
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-None-None, 1-4-3, 4-None-None, 5-None-None, 6-None-None'):
            print('PASS_21_1')
        else:
            print('FAIL_21_1    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-0, 1-1, 4-0, 5-0, 6-0'):
            print('PASS_21_2')
        else:
            print('FAIL_21_2    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'reverse')
        result = ', '.join(arr)
        if (result == '3-1, 1-None, 4-1, 5-None, 6-None'):
            print('PASS_21_3')
        else:
            print('FAIL_21_3    ' + result)
        arr.clear()
tests.append(test_21)

def test_9(): #test for multiple rotation
    tree = AVL_tree()
    try:
        tree.add(1, 20)
        tree.add(2, 19)
        tree.add(3, 1)
        tree.add(4, 17)
        tree.add(5, 31)
        tree.add(6, 15)
        tree.add(7, 3)
        tree.add(8, 13)
        tree.add(9, 5)
        tree.add(10, 25)
        tree.add(11, 10)
        tree.add(12, 29)
        tree.add(13, 8)
        tree.add(14, 26)
        tree.add(15, 28)
        tree.add(16, 12)
        tree.add(17, 4)
        tree.add(18, 27)
        tree.add(19, 2)
        tree.add(20, 81)

        tree.add(21, 132)
        tree.add(22, 7)
        tree.add(23, 11)
        tree.add(24, 18)
        tree.add(25, 24)
        tree.add(26, 14)
        tree.add(27, 6)
        tree.add(28, 9)
        tree.add(29, 30)
        tree.add(30, 16)

    except:
        print('FAIL_9 balance function error')
    else:
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'tree')
        result = ', '.join(arr)
        print('Kids:    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'tree')
        result = ', '.join(arr)
        print('Height:    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'tree')
        result = ', '.join(arr)
        print('Parents:    ' + result)
        arr.clear()
        print(tree.get_max_floor())
#tests.append(test_9)

def test_10(): #test with the same values
    tree = AVL_tree()
    try:
        tree.add(1, 1)
        tree.add(2, 3)
        tree.add(3, 2)
        tree.add(4, 2)
        tree.add(5, 2)
        tree.add(6, 2)
        tree.add(7, 2)
        tree.add(8, 2)
        tree.add(9, 2)
    except:
        print('FAIL_10 balance_RL function error')
    else:
        if (tree.get_max_floor() == 1):
            print('PASS_10')
        else:
            print('FAIL_10')
#tests.append(test_10)

def test_11(): #test with the same values
    tree = AVL_tree()
    try:
        tree.add(1, 1)
        tree.add(2, 3)
        tree.add(3, 3)
        tree.add(4, 3)
        tree.add(5, 3)
        tree.add(6, 3)
        tree.add(7, 2)
    except:
        print('FAIL_11 balance_RL function error')
    else:
        if (tree.get_max_floor() == 1):
            print('PASS_11')
        else:
            print('FAIL_11')
    
    arr = []
    tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None), str(len(n['middle']) if (n['middle']) else None)])), 'reverse')
    result = ', '.join(arr)
    print('Kids:    ' + result)
    arr.clear()

    arr = []
    for i in tree.nodes:
        arr.append('-'.join([str(i), str(tree.nodes[i]['value'])]))
    print(', '.join(arr))
    arr.clear()
#tests.append(test_11)

def test_12(): #test for remove
    tree = AVL_tree()
    try:
        """ tree.add(1, 20)
        tree.add(2, 18)
        tree.add(3, 30)
        tree.add(4, 17)
        tree.add(5, 27)
        tree.add(6, 31)
        tree.add(7, 24)
        tree.add(8, 28)
        tree.add(9, 25) """
        tree.add(1, 2)
        tree.add(2, 1)
    except:
        print('FAIL_12 balance_LL function error')
    else:
        tree.remove(tree.nodes[1])
        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['left']['key'] if (n['left']) else None), str(n['right']['key'] if (n['right']) else None)])), 'tree')
        result = ', '.join(arr)
        print('Kids:    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['height'] )])), 'tree')
        result = ', '.join(arr)
        print('Height:    ' + result)
        arr.clear()

        arr = []
        tree.do_with_nodes(lambda n, a = arr : a.append('-'.join([str(n['key']), str(n['parent']['key']) if (n['parent']) else 'None'])), 'tree')
        result = ', '.join(arr)
        print('Parents:    ' + result)
        arr.clear()
#tests.append(test_12)

for test in tests:
    test()