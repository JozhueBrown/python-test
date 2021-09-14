#include <iostream>
using namespace std;

void binario(int n){
	int i=0, j, a[1000];
	
	while (n>0)
	{
		a[i] =n%2;
		n/=2;
		i++;
	}
	cout<<"normal \n";
	for (j=i-1;j>=0;--j)
	{
		cout<<a[j];
	}
	
	cout<<"\ninverso \n";
	for (j=0;j<i;j++)
	{
		cout<<a[j];
	}
}

int main(int argc, char *argv[]){
	int n=0;
	cout<<"ingrese valor a convertir: ";
	cin>>n;
	binario(n);
	
	cout<<"\n";
	
	system ("pause");
}
