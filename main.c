#include <stdio.h>
#include <stdlib.h>
struct node
{    char word_str[20];
    char meaning_str[50];
    struct node *next;
}*start;
void create()
{    struct node *newnode, *ptr;
    int c,i=1;
    char str1[20];
    char str2[50];
    printf("Enter no. of words\n");
    scanf("%d",&c);
    printf("Enter the word:\n");
    scanf("%s",&str1);
    printf("enter its meaning:\n");
    scanf("%s",&str2);
    while(i!=c)
    {    newnode=(struct node*)malloc(sizeof(struct node));
        strcpy(newnode->word_str, str1);
        strcpy(newnode->meaning_str, str1);


        if(start==NULL)
        {    newnode->next = NULL;
            start=newnode;
        }
        else
        {    ptr=start;
            while(ptr->next!=NULL)
                ptr=ptr->next;
            ptr->next = newnode;
            newnode->next = NULL;
        }
        printf("Enter the word:\n");
        gets(str1);
        printf("enter its meaning:\n");
        gets(str2);
        i++;
    }
    sorting();
}
void display_full()
{    struct node *ptr;
    ptr = start;
    while(ptr!=NULL)
    {    printf("\t %s", ptr->word_str);
        printf("\t %s", ptr->meaning_str);
        ptr=ptr->next;
    }
    printf("\n");
}





void display()
{    char str[20];
    struct node *ptr;
    ptr = start;
    printf("enter word of which you want to know meaning\n");
    gets(str);
    while(ptr->word_str!=str)
    {ptr=ptr->next;}
    printf("\t %s:-", ptr->word_str);
    printf(" %s", ptr->meaning_str);
    printf("\n");
}




void insert()
{    struct node *newnode,*ptr;
    char str1[20];
    char str2[50];
    printf("Enter the word:\n");
    gets(str1);
    printf("enter its meaning:\n");
    gets(str2);
    newnode=(struct node*)malloc(sizeof(struct node));
        strcpy(newnode->word_str, str1);
        strcpy(newnode->meaning_str, str1);
    ptr = start;
    while(ptr->next!=NULL)
        ptr=ptr->next;
    ptr->next=newnode;
    sorting();

}







void delete_word()
{    char str1[20];
    struct node *ptr,*preptr;
    ptr=start;
    printf("Enter word to be deleted\n");
    gets(str1);
    while(ptr->word_str!=str1)
        {
            preptr=ptr;
            ptr=ptr->next;
        }
        preptr->next=ptr->next;
        free(ptr);
    sorting();
}
//SELF DESTRUCT//
/*void delete_dict()
{    struct node *ptr;
    if(start!=NULL)
    {    ptr=start;
        while(ptr->next!=NULL)
        {    delete_beg();
            ptr=start;
        }
    }
}*/

void search()
{    struct node *ptr;
    char str[20];
    int count=0;
    int flag=0;
    printf("Enter word to be found\n");
    gets(str);
    ptr=start;
    while(ptr!=NULL)
    {    ++count;
        if(ptr->word_str==str)
        {    flag=1;
            break;
        }

        ptr=ptr->next;
    }
    if(flag==1)
    printf("Element found at node %d\n",count);
    else
    printf("Not found");
}



void sorting()
{
    int i, j;
    struct node *temp;
    temp =(struct node*)malloc(sizeof(struct node));
    struct node *ptr1,*ptr2;
    ptr1=start;
    while(ptr1->next!=NULL)
    {
        ptr2=ptr1->next;
        while(ptr2!=NULL)
        {
            if(strcmp(ptr1->word_str,ptr2->word_str)>0)
            {
                         strcpy(temp->word_str,ptr1->word_str);
           		 strcpy(temp->meaning_str,ptr1->word_str);
                         strcpy(ptr1->word_str,ptr2->word_str);
            		strcpy(ptr1->meaning_str,ptr2->word_str);
                  	 strcpy(ptr2->word_str,temp->word_str);
           		 strcpy(ptr2->meaning_str,temp->word_str);
             }
            ptr2=ptr2->next;
        }
        ptr1=ptr1->next;
    }


}
void main()
{    struct node start;
    int ch;
    do
    {    printf("Enter\n");
        printf("1: Create a wordlist\n");
        printf("2: Search and Display the Word with its Meaning\n");
        printf("3: Add word\n");
        printf("4: Delete a word\n");
        printf("5: Sort list\n");
        printf("7: selfdestruct\n");
        //printf("7: display full dictnanory\n");
        printf("8: Exit\n");
        printf("Enter your option\n");
        scanf("%d", &ch);
        switch(ch)
        {    case 1: create();
                break;
            case 2: display();
                break;
            case 3: insert();
                break;
            case 4: delete_word();
                break;
            case 5: sorting();
                break;
            case 6: display_full();
                break;
            /*case 7: delete_dict();
                break;*/
            case 8: exit(1);
                break;

            default:printf("WRONG CHOICE\n");
                break;
        }
    }while(1);
}

