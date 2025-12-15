
/*The tree node has data, left child and right child 
struct node
{
    int data;
    node* left;
    node* right;
};

*/
int height(node * root)
{
    if(root == NULL) return -1;
    int hl = height(root->left) + 1;
    int hr = height(root->right) + 1;
    if(hl > hr) return hl;
    else return hr;
}
  
