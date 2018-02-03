ans = 'P3\n500 500\n255\n'
for y in range(500):
    for x in range(500):
        r = y/2
        g = x/2
        b = (x+y)%255
        ans += str(r) + ' ' + str(g) + ' ' + str(b) + ' '
    ans += '\n'
f = open('picmaker.ppm','w')
f.write(ans)
f.close()
