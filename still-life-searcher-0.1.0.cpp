#include<cstdlib>
#include<ctime>
#include<cstring>
#include<cstdio>
const int m=6,n=5;
const double p=0.5;
bool flag;
int neighbor,cnt;
int main() {
	FILE* fp=fopen("still.txt","w");
	int grid[m+4][n+4];
	srand(time(0));
	while(true) {
		flag=true;
		memset(grid,0,sizeof(grid));
		for(int i=2;i<m+2;i++) {
			for(int j=2;j<n+2;j++) {
				grid[i][j]=rand()/(double)RAND_MAX<p?1:0;
			}
		}
		for(int i=1;i<m+3;i++) {
			for(int j=1;j<n+3;j++) {
				neighbor=
				grid[i-1][j-1]+
                grid[i-1][j]+
                grid[i-1][j+1]+
                grid[i][j-1]+
                grid[i][j+1]+
                grid[i+1][j-1]+
                grid[i+1][j]+
                grid[i+1][j+1];
                if(grid[i][j]==1) {
                	if(neighbor!=2&&neighbor!=3) {
                		flag=false;
                		break;
					}
				} else {
					if(neighbor==3) {
						flag=false;
						break;
					}
				}
			}
			if(!flag) break;
		}
		if(flag) {
			for(int i=0;i<m+4;i++) {
				for(int j=0;j<m+4;j++) {
					fputc(grid[i][j]==1?'o':'.',fp);
				}
				fputc('\n',fp);
			}
			cnt++;
			printf("%d\n",cnt);
			if(cnt>=10) return 0;
		}
	}
} 
