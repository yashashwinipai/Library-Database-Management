#include <stdio.h>
#include<stdlib.h>

 int a[10][10],s[10],n;

 void bfs(int u)

{

 int f,r,q[10],v;
printf("the nodes visited from %d ",u);
f=0,r=-1;
q[++r]=u;
s[u]=1;
printf("%d ",u);
while(f<=r)
{
u=q[f++];
for(v=0;v<n;v++)
{
if(a[u][v]==1)
{
if(s[v]==0)
{

printf(" %d ",v);
s[v]=1;
q[++r]=v;
}
}
}
}
printf("\n");
 }

void dfs(int u)

{

int v;
s[u]=1;


printf(" %d ",u);

for(v=0;v<n;v++)
{

if(a[u][v]==1&&s [v]==0)
dfs(v);
}
 }

void main()

{

int i,j,choice,source,s1;

printf("enter the no of nodes\n");
scanf("%d",&n);
printf("enter the adjacency matrix\n");

for(i=0;i<n;i++)
{

for(j=0; j<n; j++)
scanf("%d",&a[i][j]);

}

for(;;)
{
printf("\n1: reachable nodes using bfs \n 2:reachable nodes using dfs\n3:exit\n");
scanf("%d",&choice);

switch(choice)

{

case 1: printf("enter the source node\n");
scanf("%d",&s1);
bfs(s1);
break;
case 2:for(source=0;source<n;source++)
{
    for(i=0;i<n;i++)
     s[i]=0;
   printf("\n reachable node from %d\n: ", source);
   dfs(source);
}
break;
case 3:exit(0);
}
}
}
