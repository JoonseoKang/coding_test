from collections import deque

phone_book = ["119", "97674223", "1195524421"]
phone_book.sort()
phone_book



a = phone_book.popleft()
a
len(a)
phone_book[0][:3] == a

phone_book = ["119", "97674223", "1195524421"]
phone_book = deque(phone_book)

while phone_book:
    a = phone_book.popleft()
    for i in phone_book:
        if a == i[:len(a)]:
            print('false')
        break
    # print('true')
    break

