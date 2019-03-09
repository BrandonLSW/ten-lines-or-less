p1 >> zap([0, 2], dur=8, sus=16, amp=linvar([1, 3], 9), amplify=2)

p2 >> karp([0, 3, 5, 4], dur=1/4, oct=6).every(3, "mirror").every(5, "offadd", 2)

p3 >> viola(var([0, 3, 5, 4], 8), dur=8, oct=5, amp=0.75)

d1 >> play("X ")

d2 >> play("*", dur=1/4, amp=var([0, 1], [15, 1]))

d3 >> play("b", dur=1/4, amp=var([0, 1], [8, 1]))

d4 >> play("  h ")
