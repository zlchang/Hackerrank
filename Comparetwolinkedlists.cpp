/*
  Compare two linked lists A and B
  Return 1 if they are identical and 0 if they are not. 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int CompareLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method
  Node *currA = headA;
  Node *currB = headB;
  while(currA != NULL && currB != NULL){
      if(currA->data != currB->data) return 0;
      currA = currA->next;
      currB = currB->next;
  }
  if(currA == NULL && currB == NULL) return 1;
  return 0;
}
