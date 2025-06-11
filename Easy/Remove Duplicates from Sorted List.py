def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    itr = head
    while itr.next:
        if itr.val == itr.next.val:
            itr.next = itr.next.next
        else:
            itr = itr.next
    return head
