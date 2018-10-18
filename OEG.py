import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def adj ( e1, e2):
    if ((e1.v1[0]==e2.v2[0]) and (e1.v1[1]==e2.v2[1])):
        return 1
    elif ((e2.v1[0]==e1.v2[0]) and (e2.v1[1]==e1.v2[1])):
        
        return 1

    else:
        return 0


def check_angle(e1,e2):
    flag=1
    if(e1.v2==e2.v1):
        points = [
            e1.v1,
            e1.v2,
            e2.v2]
        flag=1
    else:
        points=[
            e2.v1,
            e1.v1,
            e1.v2]
        flag=0;


    def angle(x1, y1, x2, y2):
        # Use dotproduct to find angle between vectors
        # This always returns an angle between 0, pi
        numer = (x1 * x2 + y1 * y2)
        denom = math.sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))
        return math.acos(numer / denom) 



    def cross_sign(x1, y1, x2, y2):
            # True if cross is positive
            # False if negative or zero
            return x1 * y2 > x2 * y1


    p1 = points[0]
    ref = points[1]
    p2 = points[2]
    x1, y1 = p1[0] - ref[0], p1[1] - ref[1]
    x2, y2 = p2[0] - ref[0], p2[1] - ref[1]

    angle=[angle(x1,y1,x2,y2)]
    if cross_sign(x1, y1, x2, y2):
        s=1
        angle.append(s)
        return angle
    else:
        s=0;
        angle.append(s)
        return angle









def check_inter(e1,e2,polygon,m1,l1,c1):
    for poly in polygon:
        if poly == e1 or poly ==e2:
            continue
        else:
            ret=poly.intersect(e1,e2,m1,l1,c1)
            if(ret==0):
                return 0;

    return 1;








def check_point(x,Y,e1,e2,polygon,cur_edge):
    count=0
    slope=0
    flag=0
    c1=x
    for poly in polygon:
        if ((poly.v1==cur_edge.v1) and (poly.v2==cur_edge.v2)) or ((poly.v1==cur_edge.v2) and (poly.v2==cur_edge.v1)):
            return 1

    print("The X value is  :",x)
    for poly in polygon:       
        y=poly.m *x + poly.c
        if((y<=poly.v1[1] and y>=poly.v2[1]) or (y>=poly.v1[1] and y<=poly.v2[1]) ) and ((x<=poly.v1[0] and x>=poly.v2[0]) or (x>=poly.v1[0] and x<=poly.v2[0])) and (y>=Y):
            print("The points (",x," ,",y,") is intersected by  :")
            poly.view()
            if((y==poly.v1[1] and x==poly.v1[0]) or (y==poly.v2[1] and x==poly.v2[0])):
                return 5
            count=count+1

    print("The count for vertices are  :",count)
    if(count%2==0):
        return 0
    else:
        return 1
   



def cond_satisfied(e1,e2,polygon):

    print("                              submain edge.....:")
    e2.view()

    if((e1.v1[0]-e2.v1[0])==0):
        m1=None
        c1=None
    else:
        m1=(e1.v1[1]-e2.v1[1])/(e1.v1[0]-e2.v1[0])
        c1=e1.v1[1] - m1*e1.v1[0]
        if e1.v1[0]<e2.v1[0]:
            
            x=(e2.v1[0]-e1.v1[0])*0.5 + e1.v1[0]
        else:
            
            x=(e1.v1[0]-e2.v1[0])*0.5 + e2.v1[0]
        repeat=1
        while repeat==1:
            y=m1*x + c1
            cur_edge=edge()
            cur_edge.add((e1.v1[0], e1.v1[1]),(e2.v1[0], e2.v1[1]))
            ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
            if(ret_value!=5):
                repeat=0
            else:
                x=x+0.1
        print("Returned from case 111   :",e1.v1[0]," ",e2.v1[0])
        if(ret_value==0):
            
            return 0
        
    l1=[(e1.v1[0], e2.v1[0]),(e1.v1[1], e2.v1[1])]

    if(e1.v1[0]-e2.v2[0])==0:
        m2=None
        c2=None
    else:
        m2=(e1.v1[1]-e2.v2[1])/(e1.v1[0]-e2.v2[0])
        c2=e1.v1[1] - m2*e1.v1[0]
        if e1.v1[0]<e2.v2[0]:
            
            x=(e2.v2[0]-e1.v1[0])*0.5 + e1.v1[0]
        else:
            
            x=(e1.v1[0]-e2.v2[0])*0.5 + e2.v2[0]
        repeat=1
        while repeat==1:
            y=m2*x + c2
            cur_edge=edge()
            cur_edge.add((e1.v1[0], e1.v1[1]),(e2.v2[0], e2.v2[1]))
            ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
            if(ret_value==5):
                x=x+0.1
            else:
                repeat=0
        print("Returned from case 2222  :",e1.v1[0]," ",e2.v2[0])
        if(ret_value==0):
            
            return 0
        
    l2=[(e1.v1[0], e2.v2[0]),(e1.v1[1], e2.v2[1])]

    if(e1.v2[0]-e2.v2[0])==0:
        m3=None
        c3=None
    else:
        m3=(e1.v2[1]-e2.v2[1])/(e1.v2[0]-e2.v2[0])
        c3=e1.v2[1] - m3*e1.v2[0]
        if e1.v2[0]<e2.v2[0]:
            
            x=(e2.v2[0]-e1.v2[0])*0.5 + e1.v2[0]
        else:
            
            x=(e1.v2[0]-e2.v2[0])*0.5 + e2.v2[0]
        repeat=1
        while repeat==1:
            y=m3*x + c3
            cur_edge=edge()
            cur_edge.add((e1.v2[0], e1.v2[1]),(e2.v2[0], e2.v2[1]))
            ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
            if(ret_value==5):
                x=x+0.1
            else:
                repeat=0
        print("Returned from case 333  :",e1.v2[0]," ",e2.v2[0])
        if(ret_value==0):
            
            return 0
        
    l3=[(e1.v2[0], e2.v2[0]),(e1.v2[1], e2.v2[1])]

    if(e1.v2[0]-e2.v1[0])==0:
        m4=None
        C4=None
    else:
        m4=(e1.v2[1]-e2.v1[1])/(e1.v2[0]-e2.v1[0])
        c4=e2.v1[1] - m4*e2.v1[0]
        if e1.v2[0]<e2.v1[0]:
            
            x=(e2.v1[0]-e1.v2[0])*0.5 + e1.v2[0]
        else:
            
            x=(e1.v2[0]-e2.v1[0])*0.5 + e2.v1[0]
        repeat=1
        while repeat==1:
            y=m4*x + c4
            cur_edge=edge()
            cur_edge.add((e1.v2[0], e1.v2[1]),(e2.v1[0], e2.v1[1]))
            ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
            if(ret_value==5):
                x=x+0.1
            else:
                repeat=0
        print("Returned from case44  :",e1.v2[0]," ",e2.v1[0])
        if(ret_value==0):
            
            return 0
        
    l4=[(e1.v2[0], e2.v1[0]),(e1.v2[1], e2.v1[1])]

    m=[m1,m2,m3,m4]
    l=[l1,l2,l3,l4]
    c=[c1,c2,c3,c4]

    for i in range(len(m)):
        if((m[i]==e1.m and c[i]==e1.c) or (m[i]==e2.m and c[i]==e2.c)):
            return 0

    return check_inter(e1,e2,polygon,m,l,c)



def adj_cond(e1,e2,polygon):
    if(e1.v1==e2.v2):
        if(e1.v2[0]-e2.v1[0])==0:
            m=None
            c=None
        else:
            m=(e1.v2[1]-e2.v1[1])/(e1.v2[0]-e2.v1[0])
            c=e1.v2[1] - m*e1.v2[0]
            if e1.v2[0]<e2.v1[0]:
                
                x=(e2.v1[0]-e1.v2[0])*0.5 + e1.v2[0]
            else:
                
                x=(e1.v2[0]-e2.v1[0])*0.5 + e2.v1[0]
            repeat=1
            while repeat==1:
                y=m*x + c
                cur_edge=edge()
                cur_edge.add((e1.v2[0], e1.v2[1]),(e2.v1[0], e2.v1[1]))
                ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
                if(ret_value==5):
                    x=x+0.1
                else:
                    repeat=0
            print("Returned from case 111   :",e1.v1[0]," ",e2.v1[0])
            if(ret_value==0):
            
                return 0
        l=[(e1.v2[0],e2.v1[0]),(e1.v2[1],e2.v1[1])]

    else:
        if(e1.v1[0]-e2.v2[0])==0:
            m=None
            c=None
        else:
            m=(e1.v1[1]-e2.v2[1])/(e1.v1[0]-e2.v2[0])
            c=e1.v1[1] - m*e1.v1[0]
            if e1.v1[0]<e2.v2[0]:
                
                x=(e2.v2[0]-e1.v1[0])*0.5 + e1.v1[0]
            else:
                
                x=(e1.v1[0]-e2.v2[0])*0.5 + e2.v2[0]
            repeat=1
            while repeat==1:
                y=m*x + c
                cur_edge=edge()
                cur_edge.add((e1.v1[0], e1.v1[1]),(e2.v2[0], e2.v2[1]))
                ret_value=check_point(x,y,e1,e2,polygon,cur_edge)
                if(ret_value==5):
                    x=x+0.1
                else:
                    repeat=0
            print("Returned from case 111   :",e1.v1[0]," ",e2.v1[0])
            if(ret_value==0):
                
                return 0
        l=[(e1.v1[0],e2.v2[0]),(e1.v1[1],e2.v2[1])]

    m1=[m]
    c1=[c]
    l1=[l]
    return check_inter(e1,e2,polygon,m1,l1,c1)






class edge:
    def _init_ (self):
        self.data = []
        self.v1 = ()
        self.v2 = ()
        self.m=0
        self.c=0
        self.max_seen=0
        self.marker=0
        self.prev_angle=0
        self.post_angle=0
        self.prev_edge=edge()
        self.post_edge=edge()


    def add(self,a,b):
        self.v1=a
        self.v2=b
        if(self.v1[0]-self.v2[0]!=0):
            self.m=(self.v1[1]-self.v2[1])/(self.v1[0]-self.v2[0])
            self.c=self.v1[1] - self.m*self.v1[0]
            
        else:
            self.m=None;
            self.c=None;
        self.data=[]
        self.marker=0
        self.max_seen=0
        self.prev_angle=0
        self.post_angle=0
        self.post_edge=edge()
        self.prev_edge=edge()


    def view(self):
        print(self.v1,self.v2)

    def insert(self,e):
        if self.max_seen ==0:
            self.data=[e]
            self.max_seen=self.max_seen+1
        else:
            self.data.append(e)
            self.max_seen=self.max_seen+1

    def seen_edges(self,polygon):
        print("Edges seen from edge ",self.v1,self.v2,"are  :")
        axes=plt.gca()
        for i in range(len(self.data)):
            e=self.data[i]
            print(e.v1,e.v2," ")
        
            axes.add_patch(Polygon([self.v1,self.v2,e.v1,e.v2],closed=True,facecolor='green'))
            axes.add_patch(Polygon([self.v1,self.v2,e.v2,e.v1],closed=True,facecolor='green'))
        
        for poly in polygon:
            if(poly==self):
                plt.plot([poly.v1[0],poly.v2[0]],[poly.v1[1],poly.v2[1]],color='black',linewidth=3)
                continue
            plt.plot([poly.v1[0],poly.v2[0]],[poly.v1[1],poly.v2[1]],color='blue',linewidth=2)
        string="EDGES SEEN FROM EDGE "+str(self.v1)+", "+str(self.v2)
        plt.title(string)
        
        




    def intersect(self,e1,e2,m1,l1,c1):
        
        for i in range(len(m1)): 

            p=l1[i]
            X=p[0]
            Y=p[1]
            if(self.m==None):
                if(m1[i]==None):
                    continue
                else:
                    x=self.v1[0]
                    y=m1[i]*x + c1[i]
                    if((y<Y[0] and y>Y[1]) or (y>Y[0] and y<Y[1])) and ((y<self.v1[1] and y>self.v2[1]) or (y>self.v1[1] and y<self.v2[1])):
                        return 0
                continue

            if(m1[i]==None):
                x=X[0]
                y=self.m*x + self.c
                if((y<Y[0] and y>Y[1]) or (y>Y[0] and y<Y[1])) and ((y<self.v1[1] and y>self.v2[1]) or (y>self.v1[1] and y<self.v2[1])):
                        return 0
                continue;



            if(m1[i]== self.m):
                continue;
            else:
                x=(self.c-c1[i])/(m1[i] - self.m)
                x=round(x,3)
                
                
                if((x<X[0] and x>X[1]) or (x>X[0] and x<X[1])) and ((x<self.v1[0] and x>self.v2[0]) or (x>self.v1[0] and x<self.v2[0])):

                    y=self.m*x + self.c
                    
                    y=round(y,3)
                    
                    if ((y<Y[0] and y>Y[1]) or (y>Y[0] and y<Y[1])) and ((y<self.v1[1] and y>self.v2[1]) or (y>self.v1[1] and y<self.v2[1])):
                        print("FOUND AN INTERSECTING EDGE INSIDE POLYGON meeting with drawn line with limit...")
                        print(l1[i])
                        print("and slope= ",m1[i]," constant= ",c1[i])
                        print("The edge is ...")
                        self.view()
                        print("the slope of edge is...:",self.m," the constant is  :",self.c)
                        print("is intersected with ",x," ",y)
                        return 0

        
        return 1



def real_angle(r):
    if(r[1]==1):
        return 2*3.14159-round(r[0],5)
    else:
        return round(r[0],5)
def adjecent_angle(e1,e2):
    if(e1.v1==e2.v2):
        if(e1.prev_angle>3.14159):
            return 0
        else:
            return 1
    else:
        if(e1.post_angle>3.14159):
            return 0
        else:
            return 1

def find_marker(e,polygon):
    for poly in polygon:
        if (e.v1==poly.v1) and (e.v2==poly.v2):
            return poly.marker
polygon=[]
v=[]


n=int(input("Enter the number of vertex  :"))
print("We round the edge value into 3 decimal places")


for i in range(0,n):
    print ("Enter Data of vertex ",i+1,"  :")
    x=float(input("Enter X  :"))
    x=round(x,3)
    y=float(input("Enter Y  :"))
    y=round(y,3)
    p=(x,y)
    v.append(p)

e=edge()
e.add(v[n-1],v[0])
polygon.append(e)


for i in range(0,n-2):
    e=edge()
    e.add(v[i],v[i+1])
    polygon.append(e)
e=edge()
e.add(v[n-2],v[n-1])
polygon.append(e)

#printing all edges of polygon
'''
for i in range(len(polygon)):
    print(polygon[i].v1," ",polygon[i].v2)
'''
ang=check_angle(polygon[n-1],polygon[0])
polygon[n-1].post_edge=polygon[0]
polygon[0].prev_edge=polygon[n-1]
polygon[n-1].post_angle=real_angle(ang)
polygon[0].prev_angle=real_angle(ang)

for i in range(0,n-1):
    jk=check_angle(polygon[i],polygon[i+1])
    jk1=real_angle(jk)
    polygon[i].post_angle=jk1
    polygon[i+1].prev_angle=jk1
    polygon[i].post_edge=polygon[i+1]
    polygon[i+1].prev_edge=polygon[i]


for i in range(len(polygon)):
    print("                                             Main Edges ...............")
    polygon[i].view()
    for j in range(len(polygon)):
        if i==j:
            continue
        if(adj(polygon[i],polygon[j])):
            
            if(adjecent_angle(polygon[i],polygon[j])==1):
                polygon[j].view()
                if adj_cond(polygon[i],polygon[j],polygon):
                    polygon[i].insert(polygon[j])
            continue;
       

        if cond_satisfied(polygon[i],polygon[j],polygon):
            polygon[i].insert(polygon[j])



###########                  CALCULATIONS COMPLETED         ################################################

#showing all edges
plt.figure()
for poly in polygon:
    plt.plot([poly.v1[0],poly.v2[0]],[poly.v1[1],poly.v2[1]],color='black',linewidth=3)
ax=plt.gca()
ax.add_patch(Polygon(v,closed=True,facecolor='white'))
plt.title("THE GIVEN POLYGON IS SHOWN BELOW")


for i in range(len(polygon)):
    plt.figure()
    polygon[i].seen_edges(polygon);

maxi=0
for i in range(len(polygon)):
    if(polygon[i].max_seen>maxi):
        index=i
        maxi=polygon[i].max_seen





seen_ed=polygon[index].data
seen_ed.append(polygon[index])
polygon[index].marker=1
cnt=0

print("\n\nthe Required edges are  :")
polygon[index].view()


for i in range(len(seen_ed)):
    for poly in polygon:
        if(poly==seen_ed[i]):
            poly.marker=1

ver=[]
for i in range(len(seen_ed)):
    ver.append(seen_ed[i].v1)
    ver.append(seen_ed[i].v2)
plt.figure()
axes = plt.gca()
for poly in polygon:
    plt.plot([poly.v1[0],poly.v2[0]],[poly.v1[1],poly.v2[1]],color='brown',linewidth=2)
axes.add_patch(Polygon(ver,
                       closed=True, facecolor=[.2,.3,.4]))
plt.plot([polygon[index].v1[0],polygon[index].v2[0]],[polygon[index].v1[1],polygon[index].v2[1]],color='black',linewidth=3)
    

while(len(seen_ed)<n):
    colorcode=3

    maxi=0
    cnt=0
    for i in range(len(polygon)):
        for j in range(len(polygon[i].data)):
            if(find_marker(polygon[i].data[j],polygon)==0):
                cnt=cnt+1

        if(cnt>maxi):
            maxi=cnt
            index=i
        cnt=0

    polygon[index].view()
    polygon[index].marker=0
    new_seen=polygon[index].data
    new_seen.append(polygon[index])
    vere=[]
    for i in range(len(new_seen)):
        if find_marker(new_seen[i],polygon)==0:
            vere.append(new_seen[i].v1)
            vere.append(new_seen[i].v2)
    polygon[index].marker=1

    axes.add_patch(Polygon(vere,
                       closed=True, facecolor=[random.randint(0,10)/10,random.randint(0,5)/5,random.randint(0,15)/15]))
    plt.plot([polygon[index].v1[0],polygon[index].v2[0]],[polygon[index].v1[1],polygon[index].v2[1]],color='black',linewidth=3)



    for i in range(len(new_seen)):
        for poly in polygon:
            if(poly==new_seen[i]):
                poly.marker=1

    seen_ed=list(set(seen_ed + new_seen))

plt.title("THE BLACK EDGES ARE REQUIRED OPEN GUARDS ")
plt.grid(True)
plt.show()











