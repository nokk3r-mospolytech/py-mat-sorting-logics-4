class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        diff = 0
        while True:
            if not l1 and not l2:
                if diff > 0:
                    curr.next = ListNode(1)
                break
            summ = 0
            if l1 and l2:
                summ = l1.val + l2.val
            elif l1:
                summ = l1.val
            else:
                summ = l2.val
            summ += diff

            if summ > 9:
                diff = 1
            else:
                0
            curr.next = ListNode(summ % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next