from datetime import datetime, timedelta


class Node:
    def __init__(self, key):
        start_time_str, duration_str, job_task = key.split(',')
        self.name_of_job = job_task.rstrip()
        start_time = datetime.strptime(start_time_str, "%H:%M")
        duration = int(duration_str)
        end_time = start_time + timedelta(minutes=duration)
        self.data = start_time.time()
        self.duration = duration
        self.end_time = end_time.time()
        self.left = None
        self.right = None

    def print_out(self, is_added):
        if is_added:
            print('{0:<20}{1}'.format('Added:', self.name_of_job))
            print('{0:<20}{1}'.format('Begin:', self.data))
            print('{0:<20}{1}'.format('End:', self.end_time))
            print('-'*50)
        else:
            print('{0:<20}{1}'.format('Rejected:', self.name_of_job))
            print('{0:<20}{1}'.format('Begin:', self.data))
            print('{0:<20}{1}'.format('End:', self.end_time))
            print('{0:<20}{1}'.format('Reason', 'Time slot overlap, please verify'))
            print('-' * 50)

    def __str__(self):
        return f"Time: {self.data}, Duration: {self.duration}, End: {self.end_time}, Jobname: {self.name_of_job}"


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root is None:
            self.root = key
            self._print_added(key)
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.end_time <= curr.data:
            if curr.left is None:
                curr.left = key
                self._print_added(key)
            else:
                self._insert(curr.left, key)
        elif key.data >= curr.end_time:
            if curr.right is None:
                curr.right = key
                self._print_added(key)
            else:
                self._insert(curr.right, key)
        else:
            self._print_rejected(key)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left)
            print(curr, end="\n")
            self._in_order(curr.right)

    def _print_added(self, key):
        self.size += 1
        key.print_out(True)

    def _print_rejected(self, key):
        key.print_out(False)

    # def pre_order(self):
    #     self._pre_order(self.root)
    #     print("")
    #
    # def _pre_order(self, curr):
    #     if curr:
    #         print(curr.data, end=" ")
    #         self._pre_order(curr.left)
    #         self._pre_order(curr.right)
    #
    # def post_order(self):
    #     self._post_order(self.root)
    #     print("")
    #
    # def _post_order(self, curr):
    #     if curr:
    #         self._post_order(curr.left)
    #         self._post_order(curr.right)
    #         print(curr.data, end=" ")

    def find_val(self, data):
        return self._find_val(self.root, data)

    def _find_val(self, curr, data):
        if curr:
            if data == curr.data:
                return curr
            elif data < curr.data:
                return self._find_val(curr.left, data)
            elif data > curr.data:
                return self._find_val(curr.right, data)
        return None

    def min_right_subtree(self, curr):
        if curr.left == None:
            return curr
        else:
            return self.min_right_subtree(curr.left)

    def delete_val(self, data):
        self._delete_val(self.root, None, None, data)

    def _delete_val(self, curr, prev, is_left, data):
        if curr:
            if data == curr.data:
                # 1. There is parent, with no child
                if curr.left is None and curr.right is None:
                    if prev:
                        if is_left:
                            prev.left = None
                        else:
                            prev.right = None
                    else:
                        self.root = None
                # 2. There is right child
                elif curr.left is None:
                    if prev:
                        if is_left:
                            prev.left = curr.right
                        else:
                            prev.right = curr.right
                    else:
                        self.root = curr.right
                # 3. There is left child
                elif curr.right is None:
                    if prev:
                        if is_left:
                            prev.left = curr.left
                        else:
                            prev.right = curr.left
                    else:
                        self.root = curr.left
                # 4. There are both children
                else:
                    min_child = self.min_right_subtree(curr.right)
                    curr.data = min_child.data
                    self._delete_val(curr.right, curr, False, min_child.data)

            elif data < curr.data:
                self._delete_val(curr.left, curr, True, data)
            elif data > curr.data:
                self._delete_val(curr.right, curr, False, data)

        else:
            print(f"{data} not found in tree")

