/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method.
  Node *prev = NULL;
  Node *curr = head;
  while(curr != NULL){
    if(prev != NULL && curr->data == prev->data){
          prev->next = curr->next;
          delete curr;
          curr = prev->next;
    }else{
        prev = curr;
        curr = curr->next;
    }
  }
  return head;  
}
