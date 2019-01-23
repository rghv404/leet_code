class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merege_k_sorted_list(lists):
    # merge k sorted linked nodes_lists
    # if nodes_lists is None:
    #     return
    # if len(nodes_lists) == 1:
    #     return nodes_lists[0]
    #
    # res = nodes_lists[0]
    # for list_ in nodes_lists[1:]:
    #     res = merge(res, list_)
    # return res

    lenlists = len(lists)

    if lenlists == 0:
        return lists

    interval = 1

    while interval < lenlists:
        for i in range(0, lenlists - interval, interval*2):
            lists[i] = merge(lists[i], lists[i+interval])
        interval = interval*2

    return lists[0]


def merge(lst1, lst2):
    dummy = ListNode(0)
    tmp1, tmp2 = lst1, lst2
    tmp = dummy
    while tmp1 is not None and tmp2 is not None:
        if tmp1.val < tmp2.val:
            tmp.next = tmp1
            tmp1 = tmp1.next
        else:
            tmp.next = tmp2
            tmp2 = tmp2.next
        tmp = tmp.next

    tmp.next = tmp1 or tmp2
    return dummy.next


def print_list(lst):
    dummy = lst
    res = ''
    while dummy is not None:
        print(dummy.val)
        dummy = dummy.next


node1 = ListNode(1)
node1.next = ListNode(4)

node2 = ListNode(2)
node2.next = ListNode(3)

node3 = ListNode(1.5)
node3.next = ListNode(5)
res = merege_k_sorted_list([node1, node2, node3])
print_list(res)
