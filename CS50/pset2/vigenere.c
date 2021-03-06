# include <stdio.h>
# include <cs50.h>
# include <ctype.h>
# include <string.h>


int main(int argc, char *argv[]){
    int len;
    char *key, *plaintext;

    if (argc>2||argv[1]==NULL){    //这个if循环用来检查输入个数
        printf("Error!\n");
        return 1;
    }
    else { //检查输入是否满足条件
        key = argv[1];
        len = strlen(key);
        for (int i=0;i<len;i++)
        { 
            if (key[i]<'A'||key[i]>'z'||(key[i]>'Z'&&key[i]<'a')) //使用ASCII码值进行检查非数字
            {   printf("invalid input:%c\n", key[i]);
                return 1;
            }
        }
    }
    printf("plaintext:\n");
    plaintext = GetString();
    printf("ciphertext:\n");
    for(int i=0, j=0, n=strlen(plaintext);i<n;i++){
        if ((plaintext[i]>='A'&&plaintext[i]<='Z')||(plaintext[i]>='a'&&plaintext[i]<='z')){  //检查plaintext是否为大小写字母
            if (j==len&&i!=0) //key长度不足时回到开头
                j = 0;
            if (key[j]>='A'&&key[j]<='Z') //使A(a)表示0,B(b)表示1...
                key[j] -= 'A';
            if (key[j]>='a'&&key[j]<='z') 
                key[j] -= 'a';
            if (plaintext[i]>='A'&&plaintext[i]<='Z'){ //大写部分
                if (plaintext[i]+key[j]>'Z'){
                        while (plaintext[i]+key[j]>'Z') //控制ASC码值
                            plaintext[i]-= 26;
                }
                plaintext[i] = plaintext[i]+key[j];
                printf("%c", plaintext[i]);
            }   

            if (plaintext[i]>='a'&&plaintext[i]<='z'){ //小写部分
                if (plaintext[i]+key[j]>'z'){
                        while (plaintext[i]+key[j]>'z') //控制ASC码值
                            plaintext[i]-=26;
                }
                plaintext[i] = plaintext[i]+key[j];
                printf("%c", plaintext[i]);
            }
            j+=1;    
        }else{ //输出非字符
                printf("%c",  plaintext[i]);
         }
    }
    printf("\n");
    return 0;
}
