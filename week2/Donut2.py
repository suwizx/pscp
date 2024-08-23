"""ijeifjsifiejs"""

donut_price = int(input())
dount_pro_number = int(input())
donut_pro_get_free = int(input())
all_donut_want = int(input())

box_set = dount_pro_number + donut_pro_get_free
box_price = donut_price * dount_pro_number

# Donut ยังมีรูแล้วเมื่อไรยูจะมีใจ :3

if all_donut_want > box_set:
    need_box = all_donut_want // box_set
    buy_topup = all_donut_want - (need_box * box_set)
    if buy_topup >= dount_pro_number:
        print(((need_box+1) * (box_price) ),((need_box+1) * (box_set)))
    else:
        print((need_box * box_price) + (buy_topup * donut_price),(need_box * box_set) + buy_topup)
else:
    if all_donut_want < dount_pro_number:
        print(all_donut_want * donut_price , all_donut_want)
    else :
        print(box_price , box_set)
