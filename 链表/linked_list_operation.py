# coding: utf-8
"""
本代码是算法第四版的Page89 - Page107中所涉及的链表，本文件主要是涉及链表的定义、删除、增加等基础操作
"""


class Node(object):
    """
    define linked list structure
    """
    def __init__(self):
        self.item = None
        self.next = None


class LinkedListOperator(object):
    """
    class for basic operations of linked list
    """
    def __init__(self):
        """
        init
        """
        pass

    def create_linked_list(self, elements_list):
        """
        create  linked list from elements_list
        :param elements_list:
        :return:
        """
        linked_lists = []
        for i in range(len(elements_list)):
            node_i = Node()
            node_i.item = elements_list[i]
            linked_lists.append(node_i)
        for i in range(len(linked_lists)-1):
            linked_lists[i].next = linked_lists[i+1]
        first = linked_lists[0]
        return first

    def get_linked_list_ele(self, node):
        """
        get elements of the linked list
        :param node:
        :return:
        """
        results = []
        while not node is None:
            results.append(node.item)
            node = node.next
        return results

    def get_linked_list_length(self, node):
        """
        calculate the length of the linked list
        :param node:
        :return:
        """
        get_length = 0
        while not node is None:
            get_length += 1
            node = node.next
        return get_length

    def insert_element(self, first, postition, element):
        """
        insert an element to the position of the node
        :param node:
        :param postition:
        :param element:
        :return:
        """
        results = []
        insert_node = Node()
        insert_node.item = element
        if postition == 0:
            old_node = first
            insert_node.next = old_node
            results.append(insert_node)
        else:
            node_position = 0
            node = first
            results.append(node)
            while not node is None:
                if postition == node_position:
                    old_node = node
                    old_node.next = insert_node
                node_position += 1
                results.append(node.next)
                node = node.next
        return results[0]


if __name__ == '__main__':
    elements_list = [1, 2, 3, 4, 5]
    linked_list = LinkedListOperator()
    node_linked_list = linked_list.create_linked_list(elements_list)
    print(linked_list.get_linked_list_ele(node_linked_list))
    new_linked_list = linked_list.insert_element(node_linked_list, 4, 6)
    print(linked_list.get_linked_list_ele(new_linked_list))
    new_linked_list = linked_list.insert_element(new_linked_list, 0, 0)
    print(linked_list.get_linked_list_ele(new_linked_list))