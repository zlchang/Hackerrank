/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method
  if(headA == NULL){
      return headB;
  }
  if(headB == NULL){
      return headA;
  }
  Node* head = NULL;
  if(headA != NULL && headB != NULL){
      if(headA->data < headB->data){
          headA->next = MergeLists(headA->next, headB);
          head = headA;
      }
      else{
          headB->next = MergeLists(headA, headB->next);
          head = headB;
      }
  }
  return head;
}
