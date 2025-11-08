#include <stdio.h>
#include <stdlib.h>


int main() {
    typedef struct NODE {
        int left;
        int right;
        int seg;
        struct NODE *child;
    } node;


    int lst[] = {5,1,2,9,6,8,2,4,9,8,5,7,2,1,1,2,5,8,4,2,7,9,1,8,6,4,8,3,1,9};
    size_t n = sizeof(lst) / sizeof(lst[0]);


    node *root = malloc(sizeof(node));
    root->seg = lst[0];  // 1st element is 1st segment
    root->left = -1;
    root->right = -1;
    root->child = NULL;


    for (int i = 1; i < n; i++) { 
        int num = lst[i];

        node *curr = root;
        
        while (1) {
            if (num < curr->seg && curr->left == -1) {
                curr->left = num;
                break;
            }
            else if (num > curr->seg && curr->right == -1) {
                curr->right = num;
                break;
            }
            else {
                // Create a new segment
                if (curr->child == NULL) {
                    node *new = malloc(sizeof(node));

                    new->seg = num;
                    new->left = -1;
                    new->right = -1;
                    new->child = NULL;

                    curr->child = new;

                    break;
                }
                // Go to next segment
                else {
                    curr = curr->child;
                }
            }
        }
    }

    // Print all segments
    node *curr = root;
    while (curr != NULL) {
        printf("%d", curr->seg);

        curr = curr->child;
    }
    printf("\n");
}

