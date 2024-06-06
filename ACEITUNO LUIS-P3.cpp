
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
	string nombre[100],aux2;
	int notas[100],n=0,alumnos_desaprobados=0,aux=0;
	float suma_notas=0.0,prom=0.0,	PROMEDIO[100],nota_1=0.0,nota_2=0.0,nota_3=0.0;
	do{	
		cout<<"Digite la cantidad de estudiantes: ";cin>>n;
	}while(n<0);
	for(int i=0;i<n;i++){
		suma_notas=0;
		nota_1=0;
		nota_2=0;
		nota_3=0;
		cout<<"\nDigite el nombre del "<<i+1<<char(99)<<" estudiante: ";cin>>nombre[i];
		do{
			cout<<"\nDigite la nota #1:";cin>>nota_1;
		}while(nota_1<0||nota_1>20);
		do{
			cout<<"Digite la nota #2:";cin>>nota_2;	
		}while(nota_2<0||nota_2>20);
		do{
			cout<<"Digite la nota #3:";cin>>nota_3;	
		}while(nota_3<0||nota_3>20);
		
		suma_notas=nota_1+nota_2+nota_3;
		PROMEDIO[i]=suma_notas/3;
		if(	PROMEDIO[i]<11){
			alumnos_desaprobados++;
		}
	}

	for(int i=0;i<n-1;i++){
		for(int j=0;j<n-1;j++){
			if(	PROMEDIO[j]>PROMEDIO[j+1]){
				aux=PROMEDIO[j];
				PROMEDIO[j]=PROMEDIO[j+1];
				PROMEDIO[j+1]=aux;
				
				aux2=nombre[j];
				nombre[j]=nombre[j+1];
				nombre[j+1]=aux2;
			}
		}
	}
	cout<<"ORDEN ASCENDENTE"<<endl;
	cout<<setfill('-')<<setw(60)<<"-"<<endl;
	for(int i=n-1;i>=0;i--){
		cout<<setw(30)<<left<<nombre[i]<<setw(30)<<left<<PROMEDIO[i]<<endl;
	}
		cout<<"\n"<<endl;

	cout<<"ORDEN DESCENDENTE"<<endl;
	cout<<setw(30)<<left<<"NOMBRES"<<setw(30)<<left<<"PROMEDIOS"<<endl;
	for(int i=0;i<n;i++){
		cout<<setw(30)<<left<<nombre[i]<<setw(30)<<left<<	PROMEDIO[i]<<endl;
	}
	cout<<"\nTOTAL DE ALUMNOS DESAPROBADOS: "<<alumnos_desaprobados;
	
}
