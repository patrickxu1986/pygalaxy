#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


class Node(object):
    """
    节点类
    """
    def __init__(self, node_name: str, node_value: str=None):
        """
        初始化节点
        name: 节点名称, 需要保持唯一性
        value: 节点对应的实际值，用于在虚拟节点中获取实际需要的值
        series_number: 通过hash及取模计算node在hash环上的序列号
        """
        self.name = node_name
        if node_value is None:
            if '#' in node_name:
                self.value = node_name.split('#')[0]
            else:
                self.value = node_name
        else:
            self.value = node_value
        self.series_number = 0
        if node_name:
            hash_value = self.generate_hash(node_name)
            series_number = self.generate_series_number(hash_value)
            self.series_number = series_number

    @staticmethod
    def generate_hash(resource: str):
        """
        通过hash算法算出目标字符串的hash值
        """
        result = hashlib.sha256(resource.encode(encoding='utf-8'))
        result = result.hexdigest()
        return result

    @classmethod
    def generate_series_number(cls, hash_value: str):
        """
        通过取模计算节点hash值在hash环上的位置
        """
        result = int(hash_value, 16)
        result = result % (2 ** 32)
        return result

    def __str__(self):
        str_list = []
        for key in self.__dict__.keys():
            val = self.__dict__[key]
            if isinstance(val, list):
                for item in val:
                    str_list.append(item.__str__())
            else:
                str_list.append('{0}: {1}'.format(key, val))
        return self.__class__.__name__ + '(' + ', '.join(str_list) + ')'


class ConsistentHash(object):
    """
    一致性hash
    """
    def __init__(self, virtual_node_numbers=5):
        """
        初始化
        _virtual_node_numbers: 每个节点需要映射的虚拟节点数
        _node_dict: 存放节点series值与node的对应关系, key是节点的series number, value为节点
        _hash_ring: 用于存放所有的节点的series number，需要保持排序
        """
        self._virtual_node_numbers = virtual_node_numbers
        self._node_dict = dict()
        self._hash_ring = []

    def add_node(self, node: Node):
        """
        增加节点
        1. 将节点加入到hash环中
        2. 根据虚拟节点的数目，创建所有的虚拟节点，并将其与对应的node关联起来
        3. 将虚拟节点的hash值放到排序列表中
        4. 添加节点后，需要保持虚拟节点hash值的顺序
        """
        if node is None:
            return
        self._node_dict[node.series_number] = node
        self._hash_ring.append(node.series_number)
        for i in range(self._virtual_node_numbers):
            virtual_node_name = "%s#%s" % (node.name, i + 1)
            virtual_node = Node(virtual_node_name)
            virtual_node.value = node.value
            self._node_dict[virtual_node.series_number] = virtual_node
            self._hash_ring.append(virtual_node.series_number)
        self._hash_ring.sort()

    def remove_node(self, node: Node):
        """
        移除节点
        1. 删除节点
        2. 删除对应的虚拟节点
        """
        del self._node_dict[node.series_number]
        self._hash_ring.remove(node.series_number)
        for i in range(self._virtual_node_numbers):
            virtual_node_name = "%s#%s" % (node.name, i + 1)
            virtual_node = Node(virtual_node_name)
            del self._node_dict[virtual_node.series_number]
            self._hash_ring.remove(virtual_node.series_number)

    def get_node(self, resource: str):
        """
        返回资源应该存放的对应node
        1. 计算资源对应的series number
        2. 在hash环中找到第一个series number大于等于资源series number的node，然后返回node
           如果series number大于所有的节点的series number，那么用hash环中第一个的节点
        """
        if self._hash_ring:
            hash_value = Node.generate_hash(resource)
            resource_series_number = Node.generate_series_number(hash_value)
            for node_series_number in self._hash_ring:
                if node_series_number >= resource_series_number:
                    return self._node_dict[node_series_number]
            return self._node_dict[self._hash_ring[0]]
        else:
            return None

    def get_nodes(self):
        """
        获取hash环中的所有节点
        """
        node_list = []
        if self._node_dict and len(self._node_dict) > 0:
            for key in self._node_dict:
                node = self._node_dict[key]
                node_list.append(node)
        return node_list

    def get_sored_nodes(self):
        """
        获取排好序的hash环中的所有节点
        """
        node_list = []
        if self._hash_ring and len(self._hash_ring) > 0:
            for key in self._hash_ring:
                node = self._node_dict[key]
                node_list.append(node)
        return node_list


if __name__ == '__main__':
    consistent_hash = ConsistentHash()
    consistent_hash.add_node(Node(node_name='server1', node_value='192.168.1.121'))
    consistent_hash.add_node(Node(node_name='server2', node_value='192.168.1.122'))
    consistent_hash.add_node(Node(node_name='server3', node_value='192.168.1.123'))
    consistent_hash.add_node(Node(node_name='server4', node_value='192.168.1.124'))
    consistent_hash.add_node(Node(node_name='server5', node_value='192.168.1.125'))
    consistent_hash.add_node(Node(node_name='server6', node_value='192.168.1.126'))
    consistent_hash.add_node(Node(node_name='server7', node_value='192.168.1.127'))
    consistent_hash.add_node(Node(node_name='server8', node_value='192.168.1.128'))
    consistent_hash.add_node(Node(node_name='server9', node_value='192.168.1.128'))
    consistent_hash.add_node(Node(node_name='server10', node_value='192.168.1.128'))
    n = consistent_hash.get_node('this is resource name')
    print(n)
