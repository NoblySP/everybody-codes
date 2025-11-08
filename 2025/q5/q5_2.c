#include <stdio.h>
#include <stdlib.h>


int main() {
    typedef struct NODE {
        int left;
        int right;
        int seg;
        struct NODE *child;
    } node;

    int swords_count;
    scanf("%d", &swords_count);

    for (int swords_num = 0; swords_num < swords_count; swords_num++) {
        int n;
        scanf("%d", &n);

        int *lst = malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            scanf("%d", &lst[i]);
        }


        node *root = malloc(sizeof(node));
        root->seg = lst[0];
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

        node *curr = root;
        while (curr != NULL) {
            printf("%d", curr->seg);

            curr = curr->child;
        }
        printf("\n");
    }
}

