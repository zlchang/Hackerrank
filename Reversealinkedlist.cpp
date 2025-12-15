/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method
  Node *prev = NULL;
  Node* curr = head;
  while(curr != NULL){
      Node *tmp = curr->next;
      curr->next = prev;
      prev = curr;
      curr = tmp;
  }
    return prev;
}
