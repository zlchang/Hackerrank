/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
  Node *curr = head;
  Node *prev = NULL;  
  while(curr != NULL){
      prev = curr;
      curr = curr->next;
  }
  Node *newnode = new Node;
  newnode->data = data;
  if(prev != NULL){
      prev->next = newnode;
  }else
      head = newnode;
    
  return head;
}
