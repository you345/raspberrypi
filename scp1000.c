####
# $ gcc -Wall -o scp1000 scp1000.c -lwiringPi
####

#include<wiringPiSPI.h>
#include<wiringPi.h>
#include<stdio.h>
#include<time.h>

#define SPI_CHANNEL 0
#define SPI_CLK 500000

int main(void){
        setvbuf(stdout, (char *)NULL, _IONBF, 0);
	double temp = 0;
	double pressure = 0;
	unsigned char buf[3];
	char str[24];
	time_t time_now;
	struct tm *local_time;
	int i,flag1=0, flag2=0;

        //wiringPiライブラリの初期化
        if (wiringPiSetup () == -1){
                return (1) ;
	}

	//SPIデバイスの初期化
	if((wiringPiSPISetup(SPI_CHANNEL, SPI_CLK))<0){
		printf("error SPI\n");
	}

	//初期処理。失敗した場合は繰り返す。
	while(1){
		flag1 = 0;
		flag2 = 0;

		//時間の表示
		time_now = time(NULL);
		local_time = localtime(&time_now);
		strftime(str, sizeof(str), "%Y/%m/%d %a %H:%M:%S", local_time);
		printf("%s\n", str);

		//ソフトリセットコード
		buf[0] = 0x1a;
		buf[1] = 0x01;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 2);
		printf("delay...\n");
		delay(60);

		//STATUS確認
		buf[0] = 0x1c;
		buf[1] = 0xff;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 2);
		printf("STATUS:%02x\n", buf[1]);
		i= buf[1]&0x01;
		if(i == 0){
			flag1 = 1;
			printf("STATUS OK!\n");
		}

		//DATARD8確認
		buf[0] = 0x7c;
		buf[1] = 0xff;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 2);
		printf("DATARD8:%02x\n", buf[1]);
		i= buf[1]&0x01;
		if(i == 1){
			flag2 = 1;
			printf("DATARD8 OK!\n");
		}

		if(flag1==1 && flag2==1){
			printf("START...\n");
			break;
		}
	}


	//オペレーションレジスタに高精度測定モードを設定
	buf[0] = 0x0e;
	buf[1] = 0x0a;
	wiringPiSPIDataRW(SPI_CHANNEL, buf, 2);

        //logfileopen
        FILE *file;
        file=fopen("/home/pi/pressurelog","a");
        fprintf(file, "aaaa");

	//メインループ
	while(1){
		//温度の測定
		buf[0] = 0x84;
		buf[1] = 0x00;
		buf[2] = 0x00;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 3);
		temp = (double)((buf[1] << (8+2)) + (buf[2] << 2)) / 20 / 4;

		//気圧の測定
		buf[0] = 0x7c;
		buf[1] = 0x00;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 2);
		pressure = buf[1] << 16;
		buf[0] = 0x80;
		buf[1] = 0x00;
		buf[2] = 0x01;
		wiringPiSPIDataRW(SPI_CHANNEL, buf, 3);
		pressure += (buf[1] << 8) + buf[2];
		pressure = pressure / 4 / 100;

		//時間の取得
		time_now = time(NULL);
		local_time = localtime(&time_now);

		//LCD表示
       		//lcdClear(fd);
	        //lcdPosition(fd,0,0);
		//strftime(str, sizeof(str), "%Y/%m/%d %a", local_time);
		//lcdPrintf(fd, "DATE=%s", str);
	        //lcdPosition(fd,0,1);
		//strftime(str, sizeof(str), "%H:%M:%S", local_time);
		//lcdPrintf(fd, "TIME=%s", str);
	        //lcdPosition(fd,0,2);
       		//lcdPrintf(fd, "TEMP=%2.2f[C]", temp);
	        //lcdPosition(fd,0,3);
       		//lcdPrintf(fd, "PRESS=%4.4f[hPa]", pressure);

		strftime(str, sizeof(str), "%Y/%m/%d %a", local_time);
		printf("DATE=%s, ", str);
		fprintf(file,"DATE=%s, ", str);
		strftime(str, sizeof(str), "%H:%M:%S", local_time);
		printf("TIME=%s, ", str);
		fprintf(file,"TIME=%s, ", str);
       		printf("TEMP=%2.2f[C], ", temp);
       		fprintf(file,"TEMP=%2.2f[C], ", temp);
       		printf("PRESS=%4.4f[hPa]\n", pressure);
       		fprintf(file,"PRESS=%4.4f[hPa]\n", pressure);

		delay(1000*10);
	}
        fclose(file);
}
