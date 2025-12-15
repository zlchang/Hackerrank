/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // Complete this function
    // Do not write the main method.
    Node *curr = head;
    
    while(curr != NULL){
        Node *pp = curr->prev;
        Node *nn = curr->next;
        curr->prev = nn;
        curr->next = pp;
        head = curr;
        curr = nn;
    }
    return head;
}
