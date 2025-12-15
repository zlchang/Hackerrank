/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method.
    Node *currA = headA;
    int countA = 0;
    while(currA != NULL){
        countA++;
        currA = currA->next;
    }
    Node *currB = headB;
    int countB = 0;
    while(currB != NULL){
        countB++;
        currB = currB->next;
    }
    
    int diff = countA - countB;
    Node* lng = headA;
    Node* sht = headB;
    if(diff < 0){
        diff = diff * -1;
        lng = headB;
        sht = headA;
    }
    for(int i = 0; i < diff; i++){
        lng = lng->next;
    }
    while(sht != NULL){
        if(sht == lng) break;
        lng = lng->next;
        sht = sht->next;
    }
    return sht->data;
}
