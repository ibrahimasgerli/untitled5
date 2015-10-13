__author__ = 'ibrahimasgerli'
genre=dict()
file=open("u.item.txt","r")
a=list(file)
b=["movie_id","movie_title","release_date","video_release_date","url","unkown","action","adventure","animation","children's","comedy","crime,documentary","drama","fantasy","film-noir","horror","musical","mystery","romance","sci-fi","thriller","war","western"]

for line in open("u.item.txt"):
    line.split("|")
    for num in b:
        if a[num]==1:
            b[num]=

