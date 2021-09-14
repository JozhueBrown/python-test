#include <iostream>
using namespace std;

void match(int * arr, int * brr, int n){
	int aux;
	cout<<"\n";
	for(int i= 1; i<=n; i++){
		aux=arr[i];
		for(int j= 1; j<=n; j++)
		{
			if(aux==brr[j])
				cout<<aux<<" ";
		}
	}
}

int main(int argc, char *argv[]){
	int n;
	cout<<"tamaño de los arreglos?: ";
	cin>>n;
	int* arr = new int[n];
	int* brr = new int[n];
	cout<<"\nArreglo 1 \n";
	for(int i= 1; i<=n; i++)
	{
		cout<<"valor "<<i<<": ";
		cin>>arr[i];
	}
	cout<<"\nArreglo 2 \n";
	for(int i= 1; i<=n; i++)
	{
		cout<<"valor "<<i<<": ";
		cin>>brr[i];
	}
	
	match(arr, brr, n);
	cout<<"\n";
	delete [] arr;
	delete [] brr;
	
	system ("pause");
}
