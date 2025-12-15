/*
  Detect loop in a linked list 
  List could be empty also
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int HasCycle(Node* head)
{
   // Complete this function
   // Do not write the main method
   Node *pos1 = head;
   Node *pos2 = head;
   while(pos1 != NULL && pos2 != NULL && pos2->next != NULL){
       pos1 = pos1->next;
       pos2 = pos2->next->next;
       if(pos1 == pos2) return 1;
   }
    return 0;
}
