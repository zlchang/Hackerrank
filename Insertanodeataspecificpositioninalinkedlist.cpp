/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
  // Complete this method only
  // Do not write main function. 
  Node *nd = new Node;
  nd->data = data;
    
  Node *curr = NULL;
  Node *next = head;
  for(int i = 0; i < position; i++){
        curr = next;
        next = curr->next;
  }
  nd->next = next;
  if(curr != NULL){
      curr->next = nd;    
      return head;
  }
  else{
    return nd;
  }

}
