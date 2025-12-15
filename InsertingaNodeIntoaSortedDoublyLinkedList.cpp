/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head,int data)
{
    // Complete this function
   // Do not write the main method.
   Node *prev = NULL;
   Node *curr = head;
   while(curr != NULL){
       if(data < curr->data) break;
       prev = curr;
       curr = curr->next;
   }
   Node *nd = new Node;
   nd->data = data;
   nd->prev = prev;
   nd->next = curr;
    
   if(prev != NULL) prev->next = nd;
   if(curr != NULL) curr->prev = nd;
    
   if(prev == NULL)  head = nd;
   return head;
}
