/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head,int positionFromTail)
{
  // This is a "method-only" submission. 
  // You only need to complete this method.
  int n = 0;
  Node *curr = head;  
  while(n <= positionFromTail){
      n++;
      curr = curr->next;
  }
  Node* copy = head;
  while(curr != NULL){
      curr = curr->next;
      copy = copy->next;
  }
  return copy->data;
}
