#include <iostream>

class Node{
    public:
    int value;
    Node *next;
};

void print_all(Node *head){
    Node *temp = head;

    while (temp!=NULL){
        std::cout<<temp->value<<std::endl;
        temp=temp->next;
    }
}

Node *search_list(Node *l, int val){
    if(l==NULL){
        return NULL;
    }
    if (l->value==val){
        return l;
    }
    else{
        return search_list(l->next, val);
    }
}

Node* insert_at_start(Node *head, int val){
    
    Node* temp = head;
    Node* new_node;
    new_node = new Node;

    new_node->value = val;
    new_node->next=temp;
    head=new_node;
    return head;
}

Node* insert_at_end(Node *head, int val){

    Node* new_node;
    new_node = new Node;
    new_node->value = val;
    new_node->next = NULL;

    Node* temp = head;

    while (temp!=NULL){
        temp = temp->next;
    }
    temp = new_node;
    return head;
}


void delete_val(Node* head, int val){
    Node * temp = head;

    while (temp->next->value!=val){
        temp=temp->next;
    }
    Node* temp2 = temp->next;
    temp=temp2;
}

int main(){
    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    one = new Node;
    two = new Node;
    three = new Node;

    one->value = 1;
    two->value = 2;
    three->value = 3;

    head = one;
    one->next = two;
    two->next = three;
    three->next = NULL;


    // print_all(head);

    // Node* out = search_list(head, 3);
    // std::cout<<"out: "<<out->value<<std::endl;

    head = insert_at_end(head, 4);
    head = insert_at_start(head, 0);

    print_all(head);

    return 0;

}



