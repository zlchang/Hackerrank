/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/
node * lca(node * root, int v1,int v2)
{
    int data = root->data;
    if(data == v1 || data == v2) return root;
    if((v1 < data && v2 > data)
        || (v1 > data && v2 < data)){
        return root;
    }
    if(v1 < data && v2 < data) return lca(root->left, v1, v2);
    return lca(root->right, v1, v2);
}

