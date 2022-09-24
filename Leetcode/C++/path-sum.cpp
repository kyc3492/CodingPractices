/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <utility>
using namespace std;

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        queue<pair<TreeNode *, int>> q;
        
        if (root != NULL){
            q.push(make_pair(root, 0));
            
            while (!q.empty()){
                TreeNode * current = q.front().first;
                int sum = q.front().second;
                
                q.pop();
                
                if (current->left == NULL && current->right == NULL){
                    if (sum + current->val == targetSum){
                        return true;
                    }
                }
                
                if (current->left != NULL){
                    q.push(make_pair(current->left, sum + current->val));
                }
                if (current->right != NULL){
                    q.push(make_pair(current->right, sum + current->val));
                }
            }
        }
        return false;
    }
};