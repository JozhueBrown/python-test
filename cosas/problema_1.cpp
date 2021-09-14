#include <iostream>
using namespace std;

void arreglo(int * arr, int n, int sum){
	int* brr = arr;
	int* crr = new int[n];
	int cont=0;
	
	/*for(int i= 1; i<=n; i++)
	{
		cont=cont+brr[i];
		if (cont<=sum)
		{
			crr[i]=brr[i];
		}
		else
			if(cont-brr[i-1]==sum)
		{
			crr[i-1]=crr[i];
			crr[i]=brr[i];
		}
		
	}
	cout<<"\n";
	for(int i= 1; i<=n; i++){
		cout<<crr[i]<<" ";
	}*/
	int  aux;
	for(int i= 1; i<=n; i++){
		aux=arr[i];
		if(aux==sum)
			cout<<aux<<"\n";
		for(int j= 1; j<=n; j++)
		{
			if(aux+arr[j]==sum)
				cout<<aux<<" "<<arr[j]<<"\n";
		}
	}
	cout<<"\n";
}

int main(int argc, char *argv[]) {
	int n, sum;
	cout<<"tamaño del arreglo?: ";
	cin>>n;
	int* arr = new int[n];
	for(int i= 1; i<=n; i++)
	{
		arr[i]=i;
	}
	cout<<"ingrese suma: ";
	cin>>sum;
	
	arreglo(arr, n, sum);
	
	delete [] arr;
	system("pause");
}

