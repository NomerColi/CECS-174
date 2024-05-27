from Interfaces import List


class DLList(List):

    class Node:

        def __init__(self, x):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self, a: list = None):
        """
      constructor; initializes an DLList object
      """

        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
        if a is not None:
            for x in a:
                self.add(self.n, x)

    def _get_node(self, i: int) -> Node:
        """
        helper method; returns the Node at index i of the list
        :param i: int type; the index of interest
        :return: the Node object at index i
        :raises: IndexError if i < 0 or i > n
        """
        if i < 0 or i > self.n:
            return None
        if i == self.n:
            p = self.dummy
        elif i < self.n / 2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy.prev
            for k in range(self.n - i - 1):
                p = p.prev

        return p

    def get(self, i):
        """
        returns the element at index i of the list
        :param i: int type; the index of interest
        :return: object type; the element at index i
        :raises: IndexError if i < 0 or i >= n where n is the number of elements in the list
        """
        return self._get_node(i).x

    def set(self, i: int, x):
        """
        overwrites the element at index i with new element x
        :param i: int type; the index that will be overwritten
        :param x: object type; the new element
        :return: the old element that was replaced
        :raises: IndexError if i < 0 or i >= n where n is the number of elements in the list
        """
        u = self._get_node(i)
        y = u.x
        u.x = x
        return y

    def _add_before(self, w: Node, x):
        """
        helper method; inserts a new node with data x before node w
        :param w: Node type; the node that will come after the newly inserted Node
        :param x: object type; the new element to add
        """
        u = self.Node(x)
        if w == None:
            raise ValueError("w is None")
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u

        self.n += 1

    def add(self, i: int, x):
        """
        inserts new element x to the list at index i
        :param i: int type; the index of insertion
        :param x: object type; the new element
        :raises: IndexError if i < 0 or i > n where n is the number of elements in the list
        """
        if i < 0 or i > self.n:
            raise IndexError("Index out of range")
        self._add_before(self._get_node(i), x)

    def _remove(self, w: Node):
        """
        helper method; removes the given Node and returns its data
        :param w: Node type; the Node that must be eliminated from the list
        :return: object type; returns the data stored in the Node
        """
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        """
        removes the element at index i of the list and returns it
        :param i: int type; the index of the element to remove
        :return: object type; the element that was removed from the list
        :raises: IndexError if i < 0 or i >=n where n is the number of elements in the list
        """
        if i < 0 or i >= self.n:
            raise IndexError("Index out of range")
        return self._remove(self._get_node(i))

    def size(self):
        """
        returns the number of elements in the list
        :returns: int type;
        """
        return self.n

    def index_of(self, x):
        """
        returns the list index of element x if exists in the list
        or None, otherwise.
        :param x: object type;
        :return: int type; the index of x in the list; None if x is not in the list
        """
        i = 0
        current = self.dummy.next
        while current != self.dummy:
            if current.x == x:
                return i
            i += 1
            current = current.next
        return None

    def append(self, x):
        """
        appends the given element to the end of the list
        :param x: object type; the new element to be added to the end
        """
        self.add(self.n, x)

    def __str__(self):
        s = "["
        u = self.dummy.next

        i = 0
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            i += 1
            if i < self.n:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x

    def __getitem__(self, key):
        if isinstance(key, int):
            # Single index
            if key < 0 or key >= self.n:
                raise IndexError("Index out of range")
            return self.get(key)
        elif isinstance(key, slice):
            # Slice
            start, stop, step = key.indices(self.n)
            result = DLList()
            for i in range(start, stop, step):
                result.append(self.get(i))
            return result
        else:
            raise TypeError("Invalid argument type")
