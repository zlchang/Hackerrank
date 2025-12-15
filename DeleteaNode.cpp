/*
  Delete Node at a given position in a linked list 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
  // Complete this method
  Node *curr = NULL;
  Node *next = head;
  for(int i = 0; i < position; i++){
      curr = next;
      next = curr->next;
  }
  if(curr != NULL){
    curr->next = next->next;
  }else{
      head = next->next;
  }
  delete next;
  return head;
}
