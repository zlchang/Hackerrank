/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/

node * insert(node * root, int value)
{
    node *prev = NULL;
    node *curr = root;
    int flag = 0;
    while(curr != NULL){
        prev = curr;
        if(value > curr->data) {curr = curr->right; flag = 2;}
        else { curr = curr->left; flag = 1;} 
    }
    node *nd = new node;
    nd->data = value;
    nd->left = NULL;
    nd->right = NULL;
    if(flag == 1){ prev->left = nd;}
    else if(flag == 2){ prev->right = nd;}
    else root = nd;
    return root;
}
