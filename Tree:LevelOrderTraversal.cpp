
/*
struct node
{
    int data;
    node* left;
    node* right;
}*/
#include <queue>

void LevelOrder(node * root)
{
  queue<node*> que;
  if(root != NULL)  que.push(root); 
  while(que.empty() == 0){
    node* tmp = que.front();
    if(tmp != NULL){
        cout<<tmp->data<<" ";
        if(tmp->left != NULL) que.push(tmp->left);
        if(tmp->right != NULL) que.push(tmp->right);
    }
    que.pop();
      
  }
  
}
