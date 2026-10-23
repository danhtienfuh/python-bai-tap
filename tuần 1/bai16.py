a,b = map(int,input().split())
tbcn = (a + b * 2) / 3
if tbcn >= 8 :
    print(f"{tbcn:.1f}","\nGioi")
elif 6.5 <= tbcn < 8 :
    print(f"{tbcn:.1f}","\nKha")
elif  5.0 <= tbcn < 6.5 :
    print(f"{tbcn:.1f}","\nTrung binh")
elif 3.5 <= tbcn < 5 :
    print(f"{tbcn:.1f}","\nYeu")
else :
    print(f"{tbcn:.1f}","\nKem")