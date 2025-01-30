rabbit = head
tortoise = head
while rabbit and rabbit.next:
    tortoise = tortoise.next
    rabbit = rabbit.next.next
    if tortoise == rabbit:
        print(True)
print(False)